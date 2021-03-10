#!/usr/bin/env python

# TODO create config file
# TODO load config file
# TODO there might be some errors in email references, verify this
# TODO define get_next_speakers function
# TODO add removal of {} chars from title and abstract
# TODO add removal of latex commands of type \command from title and abstract

import argparse
# import datetime
from datetime import datetime
from datetime import date
from pybtex.database.input import bibtex
from textwrap import wrap


def produce_reference_entry(bib_entry, formatting="post"):
    newline = '\n'
    b = bib_entry.fields

    try:
        # deal with multiple authors
        all_authors = ""
        for author in bib_entry.persons["author"]:
            author_full_name = ""
            for names in author.first_names:
                author_full_name += f"{names[0]}. "
            for lnames in author.last_names:
                author_full_name += f"{lnames}, "
            all_authors += author_full_name

        # Prepare additional info about the paper
        paper_reference = f" {b['year']}, {b['journal']}, "
        try: # field may not exist for a reference
            paper_reference += f"{b['volume']}, "
        except(KeyError):
            pass
        try: # field may not exist for a reference
            paper_reference += f"{b['pages']}"
        except(KeyError):
            pass

        # Format lines according to where will it be used
        if formatting == "post":
            papers_line1 = f"- {all_authors}`\"{b['title']}\"" + newline
            papers_line2 = f"  <{b['doi']}>`__, {paper_reference}" + newline
        elif formatting == "email":
            papers_line1 = f"- {all_authors}`\"{b['title']}\""
            papers_line2 = f"  {paper_reference}, doi:{b['doi']}" + newline
        else:
            print("Unknown reference formatting, using default one")
            papers_line1 = f"- {all_authors}`\"{b['title']}\"" + newline
            papers_line2 = f"  <{b['doi']}>`__, {paper_reference}" + newline


    except(KeyError): # field may not exist for a reference
        pass

    return papers_line1 + papers_line2

# ===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-
# Argument parsing
parser = argparse.ArgumentParser()
# parser.add_argument("-t", "--title",
#                         # type=string,
#                         required=True,
#                         action="append",
#                         help="Title of the talk")
parser.add_argument("-a", "--author",
                        # type=String,
                        required=True,
                        action="append",
                        help="Author of the talk")
# parser.add_argument("--abstract",
#                         # type=String,
#                         action="append",
#                         default=[""],
#                         help="Abstract of the talk. Must be in one line")
# parser.add_argument("--paper_link",
#                         # type=String,
#                         action="append",
#                         default=[""],
#                         help="DOI of the paper")
# parser.add_argument("--paper_reference",
#                         # type=String,
#                         default=[""],
#                         help="Reference to the paper talk")
parser.add_argument("-d", "--date",
                        # type=String,
                        required=True,
                        help="Seminar date")
parser.add_argument("-f", "--file_name",
                        # type=String,
                        required=True,
                        help="Name of the file where seminar post will be written")
parser.add_argument("-s", "--seminar_file",
                        # type=String,
                        required=True,
                        help="Name of the BibTex file from which data about the paper will be exported")
parser.add_argument("-k", "--citation_key",
                        # type=String,
                        help="Citation key, from which main information about the talk has to be extracted")

# ===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-
# Generate message elements
args = parser.parse_args()

author_name = args.author[0]
author = author_name
seminar_date = args.date
full_file_name = args.file_name
creation_date = datetime.now().strftime('%d/%m/%Y')
creation_hour = datetime.now().strftime('%H:%M')


# ===-===-===-===-
# Process bibtex  file
# BIB1 >>>
parser = bibtex.Parser()
print(args.seminar_file)
bibdata = parser.parse_file(f"{args.seminar_file}")

papers_keys = bibdata.entries.keys()
for k in papers_keys:
    print(k)
# BIB1 <<<

bib_entry = ""
if len(papers_keys) == 1:
    for bib_id in bibdata.entries:
        bib_entry = bibdata.entries[bib_id]
    # papers_keys = bibdata.entries.keys()
    # bib_entry = bibdata.entries[bibdata.entries.keys()[0]]
    # bib_entry = bibdata.entries[papers_keys[0]]
else:
    for bib_id in bibdata.entries:
        if bib_id == args.citation_key:
            bib_entry = bibdata.entries[bib_id]
            break
if bib_entry == "":
    raise ValueError("For multiple entries in library, -k option has to be specified")

b = bib_entry.fields

try:
    # Use info from paper to set up variables
    title = b['title']
    paper_abstract = wrap(b['abstract'], width=70)
    paper_link = b['doi']
    paper_tags = ""
    try:
        paper_tags = b['keywords']
    except(KeyError):
        pass
except(KeyError):
    raise KeyError("One of the following keys were missing but necessary: title, abstract, doi.")


# find next speaker in rota
if False:
    speaker_index = -1
    for (index, line) in enumerate(rota_list):
        line_fragments = line.split(",")
        title_and_slug = ",".join(line_fragments[1:2])
        if len(title_and_slug) < 5:  # lenght of apostrohpes and a coma in between
            if line_fragments[0] != author_name:
                print("Skipping empty line, presenter does not match.")
                continue

            date = line_fragments[3]
            speaker_index = index
            break
    next_speakers = get_next_speakers()
# ===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-
# Generate lines of text
# ===-===-
# For website >>>
newline = f"\n"
empty_line = f"\n"

post_title = f"{title}" + newline
title_underline = "#"*len(post_title) + newline
post_date = f":date: {creation_date} {creation_hour}" + newline
post_author = f":author: {author_name}" + newline
post_category = ":category: Seminar" + newline
post_tags = f":tags: {paper_tags[:-1]}" + newline
full_slug = full_file_name.split('.')[0]
full_slug = full_slug.split('/')[-1]
slug = "-".join(full_slug.split('-')[1:])
post_slug = f":slug: {slug}" + newline
post_sumamry = f':summary: {author_name}\'s Journal Club session where he will talk about a paper "{title}"' + newline
post_description = f'This week on Journal Club session {author_name} will talk about a paper "{title}".' + newline
separator = f"------------" + newline
vertical_separator = f"|" + newline
papers_section = f"Papers:" + newline

# BIB2 >>>
# loop through the individual references
all_references = []
for bib_id in bibdata.entries:
    bib_entry = bibdata.entries[bib_id]
    all_references.append(produce_reference_entry(bib_entry))
# BIB2 <<<

footer_date = f"**Date:** {seminar_date} |br|" + newline
footer_time = f"**Time:** 14:00 |br|" + newline
footer_location = f"**Location**: online" + newline
footer_html1 = f".. |br| raw:: html" + newline
footer_html2 = f"	<br />"

# For website <<<
# ===-===-
# For email >>>
message_subject = f"[Journal Club] - {author} - {title} - online"+ newline
greeting = "Hello everyone," + newline
# formated_date = date(seminar_date) + newline
# paragraph1 = f'{author} will present at the journal club this Friday {formated_date.strftime("%-d %B %Y")} at 14:00.' + newline

formated_date = datetime.strptime(seminar_date, "%Y/%m/%d")
print(formated_date )
# formated_date = seminar_date + newline
paragraph1 = f'{author} will present at the journal club this Friday {formated_date.strftime("%-d %B %Y")} at 14:00.' + newline

paragraph1 += f'He will talk about a paper "{title}". Please see the abstract below.' + newline
zoom_notification1 = "The meeting is held online on Zoom, please follow this link to join:" + newline
zoom_notification2 = "XXXXXXXXXXXXXXXXX_LINK_XXXXXXXXXXXXXXXXX" + newline
zoom_notification3 = "Meeting ID: " + newline
zoom_notification4 = "Passcode: " + newline
reminder_part1 = "A reminder on next three Journal Club speakers:" + newline
reminder_part2 = ""
if False:
    for (k, data) in enumerate(next_speakers):
        next_speaker = data["speaker"]
        next_date = data["date"]
        reminder_part2 += f"k) {next_speaker}\t\t\t - {next_date}"
title_separator = "================================================================"
all_references_email = []
for bib_id in bibdata.entries:
    bib_entry = bibdata.entries[bib_id]
    all_references_email.extend(
                            wrap(
                                produce_reference_entry(bib_entry,
                                                        formatting="email"
                                                        ),
                                width=70
                                )
                            )

# For email <<<
# ===-===-
# For rota file >>>
if False:
    date_modifier = 0
    next_modifier = 0
    second_next_mod = 0
    another_modifier = 0
    publication_modifier = 1

    rota_data = f'{author_name},"{title}","{full_slug}.rst",{date_modifier},{next_modifier},{second_next_mod},{another_modifier},{publication_modifier}'
# For rota file  <<<
# ===-===-
# ===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-
# Generate texts
# ===-===-
# Generate post
post_text = [post_title,
                title_underline,
                post_date,
                post_author,
                post_category,
                post_tags,
                post_slug,
                post_sumamry,
                empty_line,
                post_description,
                empty_line,
                separator,
                empty_line]

for line in paper_abstract:
    post_text.append(line + newline)

post_text.extend((
                empty_line,
                vertical_separator,
                empty_line,
                papers_section,
                empty_line))

for reference in all_references:
    post_text.append(reference)

post_text.extend((
                empty_line,
                empty_line,
                footer_date,
                footer_time,
                footer_location,
                empty_line,
                footer_html1,
                newline,
                footer_html2))

# ===-===-
# Generate email
message_text =[message_subject,
                empty_line,
                greeting,
                empty_line]

paragraph1 = wrap(paragraph1)
for line in paragraph1:
    message_text.append(line + newline)

message_text.extend((
                empty_line,
                zoom_notification1,
                zoom_notification2,
                empty_line,
                zoom_notification3,
                zoom_notification4,
                empty_line,
                reminder_part1,
                reminder_part2,
                empty_line,
                title_separator,
                empty_line,
                empty_line,
                title,
                empty_line,
                empty_line,
                title_separator,
                empty_line))

for line in paper_abstract:
    message_text.append(line + newline)

message_text.extend((
                empty_line,
                vertical_separator,
                empty_line,
                papers_section,
                empty_line))

for reference in all_references_email:
    message_text.append(reference)

# ===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-
# File creation and modification
# Save post
with open(full_file_name, "a") as seminar_file:
    seminar_file.writelines(post_text)

# Save email
with open("new_seminar_email.txt", "w") as email_file:
    email_file.writelines(message_text)

# ===-===-
# Modify Rota file

# Read file into list
if False:
    rota_list = []
    with open(rota_file_name) as file:
        for line in file:
            line.strip()
            rota_list .append(line)

    # replace row
    rota_list[speaker_index] = rota_data

    # save new file
    with open(rota_file_name, "w") as rota_file:
        rota_file.writelines(rota_list)

