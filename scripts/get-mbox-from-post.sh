#!/bin/bash
# Takes an rst file and generates an mbox that can be easily sent out using an
# e-mail client

TO_ADDRESS="com-bio@herts.ac.uk"
SUBJECT=""
POST_HEADER=""
AUTHOR=""
INPUT_FILE=""
SESSION_DATE=$(date -d 'this Friday 4PM' '+%H%M %A %d %B %Y')
SESSION_LOCATION="D449"
ADMIN="Admin <someone at herts.ac.uk>"

function usage ()
{
    cat << EOF
    usage: $0 options -i <rst post file>

    Script that takes an rst post file and generates an e-mail in mbox to send out.
    Requires the linux "mail" command.

    OPTIONS:
    -h  Show this help message and quit

    -t  To (default: com-bio@herts.ac.uk)

    -a Author of post (default: taken from :Author: tag in rst)

EOF
}

function go_fetch ()
{
    POST_HEADER=$(head -n 1 $INPUT_FILE)
    AUTHOR=$(grep -E '^:author:' $INPUT_FILE | sed 's/:author: //')
    SUBJECT="[Journal club] - $AUTHOR - $POST_HEADER - $SESSION_DATE in $SESSION_LOCATION"
}


function generate_mbox ()
{
    MESSAGE=$(sed -n "9,$ p" $INPUT_FILE | sed '/\*\*Date:\*\*/,$ d')
    GREETING="Hello,\n\n$AUTHOR will present at the journal club this $SESSION_DATE in $SESSION_LOCATION.\n\n"
    SECONDLINE="Title and abstract of the talk is below:\n$POST_HEADER\n\n"
    UNDERLINE=$(printf '%0.s-' $(seq 1 40))

    #echo -e "$GREETING""$SECONDLINE""$UNDERLINE""$MESSAGE" | mail -s "$SUBJECT" -r "from=$ADMIN" to-addr "$TO_ADDRESS"
    echo -e "$SUBJECT""$GREETING""$SECONDLINE""$UNDERLINE""$MESSAGE" >> new_mail.txt
    echo "Output file is called 'com-bio'. Run 'evolution com-bio' and that should be it."
    echo "NOTE: Please verify the e-mail before sending it. This is only a convenience tool and may have made errors."
}

function generate_mbox_new ()
{
   # Parse the data info into paper title, zoom link, current date, papers, abstract, next 3 speakers
    SEPARATOR=$(printf '%0.s=' $(seq 1 40))

    PRESENTER_INFO="Hello everyone,\n\n$AUTHOR will present at the Journal Club this $SESSION_DATE.\n\n"
    PAPER_INFO="He will talk about a paper . Please see the abstract below.\n\n"
    ZOOM_INFO="The meeting is held online on Zoom, please follow this link to join:\n\n\n\n "
    REMINDER="A reminder on the next three Journal Club speakers:\na)\nb)\nc)\n"
    TITLE="$SEPARATOR\n\n title \n\n$SEPARATOR"
    MESSAGE=$(sed -n "9,$ p" $INPUT_FILE | sed '/\*\*Date:\*\*/,$ d')

    FINAL_MESSAGE="$PRESENTER_INFO$PAPER_INFO$ZOOM_INFO$REMINDER$TITLE"

    #echo -e "$GREETING""$SECONDLINE""$UNDERLINE""$MESSAGE" | mail -s "$SUBJECT" -r "from=$ADMIN" to-addr "$TO_ADDRESS"
    # echo -e "$SUBJECT""$GREETING""$SECONDLINE""$UNDERLINE""$MESSAGE" >> new_mail.txt
    echo -e "$FINAL_MESSAGE" >> new_mail.txt
    echo "Output file is called 'com-bio'. Run 'evolution com-bio' and that should be it."
    echo "NOTE: Please verify the e-mail before sending it. This is only a convenience tool and may have made errors."
}

if [ "$#" -eq 0 ]; then
    usage
    exit 0
fi

while getopts "a:i:t:h" OPTION
do
    case $OPTION in
        t)
            TO_ADDRESS=$OPTARG
            ;;
        a)
            AUTHOR=$OPTARG
            ;;
        h)
            usage
            exit 0
            ;;
        i)
            INPUT_FILE=$OPTARG
            ;;
        ?)
            usage
            exit 0
            ;;
    esac
done

if [[ -n "$INPUT_FILE" ]]  && [[ -e "$INPUT_FILE" ]]
then
    go_fetch
    generate_mbox
else
    echo "File $INPUT_FILE not found. Exiting."
    exit 1 
fi
