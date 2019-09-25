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

    echo -e "$GREETING""$SECONDLINE""$UNDERLINE""$MESSAGE" | mail -s "$SUBJECT" -S "from=$ADMIN" -F "$TO_ADDRESS"
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
