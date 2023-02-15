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

# from datetime import date
from pybtex.database.input import bibtex
from textwrap import wrap
import os
import csv
from pathlib import Path
from string import ascii_lowercase


def prune_text(some_text):
    some_text = some_text.replace("{", "")
    some_text = some_text.replace("}", "")
    some_text = some_text.replace("\textemdash", "-")
    return some_text


def produce_reference_entry(bib_entry, formatting="post"):
    """
    Year, journal, author, doi have to be included in the reference.
    """
    newline = "\n"
    b = bib_entry.fields

    # TODO add check for all required keys and inform whenever they are not present

    # TODO this has to be refactored- variables should not be allocated within try-catch
    all_authors = ""

    # try:
    # deal with multiple authors
    for author in bib_entry.persons["author"]:
        author_full_name = ""
        for names in author.first_names:
            author_full_name += f"{prune_text(names[0])}. "
        for lnames in author.last_names:
            author_full_name += f"{prune_text(lnames)}, "
        all_authors += author_full_name

    # Prepare additional info about the paper
    # TODO Change the error output for crucial keys
    paper_reference = f" {b['year']}, {b['journal']}, "
    try:  # field may not exist for a reference
        paper_reference += f"{b['volume']}, "
    except (KeyError):
        pass
    try:  # field may not exist for a reference
        paper_reference += f"{b['pages']}"
    except (KeyError):
        pass

    # Check if doi link is correct
    prefix = ""
    if not ("https" in b["doi"]):
        prefix += "https://"
    if not ("doi.org/" in b["doi"]):
        prefix += "doi.org/"
    b["doi"] = prefix + b["doi"]

    # Format lines according to where will it be used
    if formatting == "post":
        papers_line1 = f"- {all_authors}`\"{b['title']}\"" + newline
        papers_line2 = f"  <{b['doi']}>`__, {paper_reference}" + newline
    elif formatting == "email":
        papers_line1 = f"- {all_authors} \"{b['title']}\""
        papers_line2 = f"  {paper_reference}, doi: {b['doi']}" + newline
    else:
        print("Unknown reference formatting, using default one")
        papers_line1 = f"- {all_authors} \"{b['title']}\"" + newline
        papers_line2 = f"  <{b['doi']}>`__, {paper_reference}" + newline

    papers_line1 = prune_text(papers_line1)
    papers_line2 = prune_text(papers_line2)

    return papers_line1 + papers_line2

    # except(KeyError):  # field may not exist for a reference
    #     pass


# ===-
# Modify Rota file
def find_speaker(rota_list, author):
    for (index, line) in enumerate(rota_list):
        line_sections = line.split(",")

        # Find author
        if line_sections[0] == author:

            # Check if the title for his talk is set (omit overwritting prevoius talks)
            if len(line_sections[2]) < 3:
                return index


def prepare_rota_info(rota_line, title, slug_info):
    line_fragments = rota_line.split(",")
    line_fragments[1] = title
    line_fragments[2] = slug_info

    return ",".join(line_fragments)


def add_quotation(text):
    return '"' + text + '"'


# Read file into list
def get_rota_file(rota_data_file):
    rota_list = []
    with open(rota_data_file) as file:
        for line in file:
            line.strip()
            rota_list.append(line)
    return rota_list


def get_next_speakers(rota_file, speaker_index):
    if len(rota_file[speaker_index::]) < 3:
        last_speaker = len(rota_file)
    else:
        last_speaker = speaker_index + 3

    speakers_list = rota_file[speaker_index:last_speaker]
    speakers = []
    for a_line in speakers_list:
        line = a_line.split(",")
        speakers.append(line[0])
    return speakers


def get_speaker_line(speakers_list):
    speaker_lines = []
    alphabet = list(ascii_lowercase)

    for index, person in enumerate(speakers_list):
        speaker_lines.append(f"{alphabet[index]}) {person} -- somedate")

    return speaker_lines


# ===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-
# Argument parsing
parser = argparse.ArgumentParser()
# parser.add_argument("-t", "--title",
#                         # type=string,
#                         required=True,
#                         action="append",
#                         help="Title of the talk")

parser.add_argument(
    "-a",
    "--author",
    # type=String,
    required=True,
    action="append",
    help="Author of the talk",
)
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
parser.add_argument(
    "-d",
    "--date",
    # type=String,
    required=True,
    help="Seminar date",
)
parser.add_argument(
    "-f",
    "--file_name",
    # type=String,
    required=True,
    help="Name of the file where seminar post will be written",
)
parser.add_argument(
    "-s",
    "--seminar_file",
    # type=String,
    required=True,
    help="Name of the BibTex file from which data about the paper will be exported",
)
parser.add_argument(
    "-k",
    "--citation_key",
    # type=String,
    help="Citation key, from which main information about the talk has to be extracted",
)
parser.add_argument(
    "-n",
    "--paper_name",
    # type=String,
    help="Paper name, from which main information about the talk has to be extracted",
)
parser.add_argument(
    "-g",
    "--slug",
    # type=String,
    help="Formated name of the file in which post content is located",
)


# ===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-
# Generate message elements
args = parser.parse_args()

author_name = args.author[0]
author = author_name
seminar_date = args.date
full_file_name = args.file_name
creation_date = datetime.now().strftime("%Y-%m-%d")
creation_hour = datetime.now().strftime("%H:%M:%S")

slug_info = args.slug

year = str(datetime.now().year)
# if Sept - Dec add b to file name
if datetime.now().month >= 9:
    year += "b"

rota_data_file = "scripts/rota-data-{}.csv".format(year)
zoom_data_file = "scripts/zoom_info.txt"

# ===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-
# Get rota list

rota_list = get_rota_file(rota_data_file)

speaker_index = find_speaker(rota_list, author)

if speaker_index is None:
    print("\n!WARNING! Speaker was not found on the rota list!\n\n")
    error()

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
    target_title = args.paper_name.lower()
    target_title = prune_text(target_title)
    # print("target: {}".format(target_title))

    for (k, bib_id) in enumerate(bibdata.entries):
        entry_title = bibdata.entries[bib_id].fields["title"].lower()
        entry_title = prune_text(entry_title)
        # print("entry_title: {}".format(entry_title))

        if entry_title == target_title:  # or k == 1:
            # if bib_id == args.citation_key:
            bib_entry = bibdata.entries[bib_id]
            break

if bib_entry == "":
    raise ValueError(
        "For multiple entries in library, -k option (main paper citation key) has to be specified"
    )
else:
    print("Selected bib entry with title: ", bib_entry.fields["title"])

# ===-===-
b = bib_entry.fields

try:
    title = prune_text(b["title"])
except (KeyError):
    raise KeyError("Following key was missing but necessary: title.")

try:
    paper_abstract = wrap(prune_text(b["abstract"]), width=90)
except (KeyError):
    raise KeyError("Following key was missing but necessary: abstract.")

try:
    paper_link = b["doi"]
except (KeyError):
    raise KeyError("Following key was missing but necessary: doi.")

paper_tags = ""
try:
    paper_tags = b["keywords"]
except (KeyError):
    print("Kwywords are missing, continuing without them.")
    pass


# find next speaker in rota
# if False:
#     speaker_index = -1
#     for (index, line) in enumerate(rota_list):
#         line_fragments = line.split(",")
#         title_and_slug = ",".join(line_fragments[1:2])
#         if len(title_and_slug) < 5:  # lenght of apostrohpes and a coma in between
#             if line_fragments[0] != author_name:
#                 print("Skipping empty line, presenter does not match.")
#                 continue
#
#             date = line_fragments[3]
#             speaker_index = index
#             break
#     next_speakers = get_next_speakers()

# ===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-
# Generate lines of text
# ===-===-
# For website >>>
newline = "\n"
empty_line = "\n"

post_title = f"{title}" + newline
title_underline = "#" * len(post_title) + newline
post_date = f":date: {creation_date} {creation_hour}" + newline
post_author = f":author: {author_name}" + newline
post_category = ":category: Seminar" + newline
post_tags = f":tags: {paper_tags[:-1]}" + newline
full_slug = full_file_name.split(".")[0]
full_slug = full_slug.split("/")[-1]
slug = "-".join(full_slug.split("-")[1:])
post_slug = f":slug: {slug}" + newline
post_sumamry = (
    f':summary: {author_name}\'s Journal Club session where he will talk about a paper "{title}"'
    + newline
)
post_description = (
    f'This week on Journal Club session {author_name} will talk about a paper "{title}".'
    + newline
)
separator = "------------" + newline
vertical_separator = "|" + newline
papers_section = "Papers:" + newline

# BIB2 >>>
# loop through the individual references
all_references = []
for bib_id in bibdata.entries:
    bib_entry = bibdata.entries[bib_id]
    all_references.append(produce_reference_entry(bib_entry))
# BIB2 <<<

footer_date = f"**Date:** {seminar_date} |br|" + newline
footer_time = "**Time:** 14:00 |br|" + newline
footer_location = "**Location**: online" + newline
footer_html1 = ".. |br| raw:: html" + newline
footer_html2 = "	<br />"

# For website <<<
# ===-===-
# For email >>>
formated_date = datetime.strptime(seminar_date, "%Y/%m/%d")
print(formated_date)
formated_date = formated_date.strftime("%-d %B %Y")
seminar_time = "14:00"

message_subject = (
    f"[Journal Club] - {author} - {title} - {formated_date} at {seminar_time} - online"
    + newline
)
greeting = "Hello everyone," + newline
# formated_date = date(seminar_date) + newline
# paragraph1 = f'{author} will present at the journal club this Friday {formated_date.strftime("%-d %B %Y")} at 14:00.' + newline

# formated_date = seminar_date + newline
paragraph1 = (
    f"{author} will present at the journal club this Friday {formated_date} at 14:00."
    + newline
)

paragraph1 += (
    f'She/He will talk about a paper "{title}". For more information, please see the abstract below.'
    + newline
)
zoom_notification1 = (
    "The meeting is held online on Zoom. To join, please use the following link:"
    + newline
)

path = Path(zoom_data_file)
if path.is_file():
    # Read file into list
    zoom_file = []
    with open(zoom_data_file) as file:
        for line in file:
            line.strip()
            zoom_file.append(line)
    zoom_notification2 = zoom_file[0]
    zoom_notification3 = zoom_file[2]
    zoom_notification4 = zoom_file[3]

else:
    zoom_notification2 = "XXXXXXXXXXXXXXXXX_LINK_XXXXXXXXXXXXXXXXX" + newline
    zoom_notification3 = "Meeting ID: " + newline
    zoom_notification4 = "Passcode: " + newline


# TODO Add a method for loading next speakers
reminder_part1 = "A reminder on next three Journal Club speakers:" + newline

if ~(speaker_index is None):
    next_speakers = get_next_speakers(rota_list, speaker_index)
    speakers_list = get_speaker_line(next_speakers)
    reminder_part2 = "\n".join(speakers_list)
else:
    reminder_part2 = ""

# if False:
#     for (k, data) in enumerate(next_speakers):
#         next_speaker = data["speaker"]
#         next_date = data["date"]
#         reminder_part2 += f"k) {next_speaker}\t\t\t - {next_date}"

title_separator = (
    "================================================================" + newline
)

all_references_email = []
for bib_id in bibdata.entries:
    bib_entry = bibdata.entries[bib_id]
    reference_entry = produce_reference_entry(bib_entry, formatting="email")
    print(reference_entry)
    if reference_entry is None:
        print("Empty bib entry- will have to verify this")
    else:
        all_references_email.extend(wrap(reference_entry, width=90))

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
post_text = [
    post_title,
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
    empty_line,
]

for line in paper_abstract:
    post_text.append(line + newline)

post_text.extend(
    (empty_line, vertical_separator, empty_line, papers_section, empty_line)
)

for reference in all_references:
    post_text.append(reference)

post_text.extend(
    (
        empty_line,
        empty_line,
        footer_date,
        footer_time,
        footer_location,
        empty_line,
        footer_html1,
        newline,
        footer_html2,
    )
)

# ===-===-
# Generate email
email_text = [message_subject, empty_line, greeting, empty_line]

paragraph1 = wrap(paragraph1)
for line in paragraph1:
    email_text.append(line + newline)

email_text.extend(
    (
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
        title,
        empty_line,
        empty_line,
        title_separator,
        empty_line,
    )
)

for line in paper_abstract:
    email_text.append(line + newline)

email_text.extend(
    (empty_line, vertical_separator, empty_line, papers_section, empty_line)
)

for reference in all_references_email:
    email_text.append(reference)


# ===-===-
# Prepare rota file

# replace row

rota_list[speaker_index] = prepare_rota_info(
    rota_list[speaker_index], add_quotation(title), add_quotation(slug_info)
)


# ===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-===-
# File creation and modification
# Save post
with open(full_file_name, "a") as seminar_file:
    seminar_file.writelines(post_text)

# ===-===-
# Save email
with open("new_seminar_email.txt", "w") as email_file:
    email_file.writelines(email_text)

# ===-===-
# Change rota file
# ===-
# Move old file for backup
r_file_parts = rota_data_file.split(".")
os.replace(rota_data_file, f"{r_file_parts[0]}_backup.{r_file_parts[1]}")

# ===-
with open(rota_data_file, "w") as rota_file:
    rota_file.writelines(rota_list)

# DONE: zoom link may be loaded from a local file
