PY?=python3
PELICAN?=pelican
PELICANOPTS=
DATE := $(shell date +'%Y-%m-%d %H:%M:%S')
DATEYYMMDD := $(shell date +'%Y%m%d')
SLUG := $(shell echo '${NAME}' | sed -e 's/[^[:alnum:]]/-/g' | tr -s '-' | tr A-Z a-z)
EXT ?= rst
AUTHOR := Volker Steuber

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
SCRIPTDIR=$(BASEDIR)/scripts
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

# FTP_HOST=homepages.herts.ac.uk # old server
FTP_HOST=vmcr-la-homep01.herts.ac.uk
FTP_USER=biocomp
FTP_TARGET_DIR=./public_html
# FTP_PORT=21
FTP_PORT=22 # for sftp protocol

# SSH_HOST=homepages.herts.ac.uk # old server
SSH_HOST=vmcr-la-homep01.herts.ac.uk
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
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make dropbox_upload                 upload the web site via Dropbox    '
	@echo '   make ftp_upload                     upload the web site via FTP        '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

rota:
	python3 scripts/generateRota.py
	cp rota-2021.ics rota.ics
	mv -v rota*ics content/files/
	mv -v rota*txt content/pages/


taglist:
	grep -o -h '^:tags:.*' content/*rst  | sed 's/:tags: //' | tr ',' '\n' | sed 's/^[[:space:]]*//' | sort | uniq | sed '/^[[:space:]]*$$/ d' | tr '\n' ',' | sed 's/,/, /g' | sed 's/,[[:space:]]*$$//'

categorylist:
	grep -o -h '^:category:.*' content/*rst  | sed 's/:category: //' | tr ',' '\n' | sed 's/^[[:space:]]*//' | sort | uniq | sed '/^[[:space:]]*$$/ d' | tr '\n' ',' | sed 's/,/, /g' | sed 's/,[[:space:]]*$$//'

html: rota
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate: rota
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
ifdef PORT
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

serve-global:
ifdef SERVER
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b $(SERVER)
else
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT) -b 0.0.0.0
endif


devserver:
ifdef PORT
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -p $(PORT)
else
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)
endif

publish: rota
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

ssh_upload: publish
	scp -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete $(OUTPUTDIR)/ $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR) --cvs-exclude

dropbox_upload: publish
	cp -r $(OUTPUTDIR)/* $(DROPBOX_DIR)

ftp_upload: publish
	lftp sftp://$(FTP_USER)@$(FTP_HOST) -p $(FTP_PORT) -e "set ftp:ssl-force on; set ftp:ssl-protect-data on; set ssl:verify-certificate no; mirror -R --delete --parallel=3 --exclude cgi-bin/ --exclude .htaccess $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

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

newseminar_test:
ifdef NAME
	echo "$(NAME)" >  $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
	SEMINAR_FILE := $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)

	echo "Some more info" >> $(SEMINAR_FILE)
endif

newseminar:
ifdef AUTHOR
	python3 scripts/newseminar.py -a "$(AUTHOR)" -d $(shell date +'%Y/%m/%d') -f $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT) -s "scripts/seminar_file.bib" -n "${NAME}"
	${EDITOR} $(INPUTDIR)/$(DATEYYMMDD)-$(SLUG).$(EXT)
else
	@echo 'Variable NAME is not defined.'
	@echo 'Do make newpost NAME='"'"'Post Name'"'"
endif

.PHONY: html help clean regenerate serve serve-global devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github newpost
