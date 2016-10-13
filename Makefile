PY?=python3
PELICAN?=pelican-3
PELICANOPTS=
DATE := $(shell date +'%Y-%m-%d %H:%M:%S')
DATEYYMMDD := $(shell date +'%Y%m%d')
SLUG := $(shell echo '${NAME}' | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)
EXT ?= rst
AUTHOR := Volker Steuber

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

FTP_HOST=homepages.herts.ac.uk
FTP_USER=biocomp
FTP_TARGET_DIR=./public_html
FTP_PORT=21

SSH_HOST=homepages.herts.ac.uk
SSH_PORT=22
SSH_USER=biocomp
SSH_TARGET_DIR=./public_html

S3_BUCKET=my_s3_bucket

CLOUDFILES_USERNAME=my_rackspace_username
CLOUDFILES_API_KEY=my_rackspace_api_key
CLOUDFILES_CONTAINER=my_cloudfiles_container

DROPBOX_DIR=~/Dropbox/Public/

GITHUB_PAGES_BRANCH=gh-pages

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make rota                           (re)generate the rota              '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          start/restart develop_server.sh    '
	@echo '   make stopserver                     stop local server                  '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make dropbox_upload                 upload the web site via Dropbox    '
	@echo '   make ftp_upload                     upload the web site via FTP        '
	@echo '   make s3_upload                      upload the web site via S3         '
	@echo '   make cf_upload                      upload the web site via Cloud Files'
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

rota:
	python3 scripts/generateRota.py
	mv rota*ics content/files/ -v
	mv rota*txt content/pages/ -v
	

html: rota
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate: rota
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	cd $(OUTPUTDIR) && $(PY) -m pelican.server $(PORT)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server
endif

serve-global:
ifdef SERVER
	cd $(OUTPUTDIR) && $(PY) -m pelican.server 80 $(SERVER)
else
	cd $(OUTPUTDIR) && $(PY) -m pelican.server 80 0.0.0.0
endif


devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	$(BASEDIR)/develop_server.sh stop
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'

publish: rota
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

ssh_upload: publish
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

dropbox_upload: publish
	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

ftp_upload: publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -p $(FTP_PORT) -e "set ftp:ssl-force on; set ftp:ssl-protect-data on; set ssl:verify-certificate no; mirror -R --delete --parallel=3 --exclude cgi-bin/ --exclude .htaccess $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

s3_upload: publish
	s3cmd sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl-public --delete-removed --guess-mime-type

cf_upload: publish
	cd $(OUTPUTDIR) && swift -v -A https://auth.api.rackspacecloud.com/v1.0 -U $(CLOUDFILES_USERNAME) -K $(CLOUDFILES_API_KEY) upload -c $(CLOUDFILES_CONTAINER) .

github: publish
	ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)

newpost:
ifdef NAME
	echo "$(NAME)" >  $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo -n "$(NAME)" | sed "s/./#/g" >>  $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo >>  $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo ":date: $(DATE)" >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo ":author: $(AUTHOR)" >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo ":category: " >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo ":tags: " >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo ":slug: $(SLUG)" >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo ":status: draft" >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo ":summary: " >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo ""              >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	echo ""              >> $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	${EDITOR} ${INPUTDIR}/$(DATEYYMMDD)-${SLUG}.${EXT}
else
	@echo 'Variable NAME is not defined.'
	@echo 'Do make newpost NAME='"'"'Post Name'"'"
endif

.PHONY: html help clean regenerate serve serve-global devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github newpost
