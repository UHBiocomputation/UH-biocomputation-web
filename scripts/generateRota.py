#!/usr/bin/env python3
# vim: set fileencoding=utf-8
"""
Generate rst rota to be included into the seminar page.

This script takes a csv file as input. The csv file should have the following
format:

"Speaker name","Title of talk","Name of blog post rst file","Date of
talk","Time talk starts","Time talk ends","Location of talk","Whether talk
should be added
to master list on seminar page or not (0/1)"

For fields such as date, start and end times, and the location of the talk, one
can use a "0", which will set it to the default value that's set in this script
below.

If the last field is set to 0, the session will still be added to the ICS
calendar, but it will not be added to the seminar page on the website. This
permits us to list other ad-hoc events to the biocomputation calendar without
also adding them to our seminar list, for example - colloquium sessions.
Basically, set it to 1 for Biocomputation sessions, and 0 for others.

File: generateRota.py

Copyright 2016 Ankur Sinha
Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


from datetime import datetime
from datetime import timedelta
from datetime import date
import icalendar
import sys
import textwrap
import pytz
import csv
import logging


class generateRota:

    """
    Generates the rota rst to be included in the website.

    Also generates an ics file that people can subscribe to.
    """

    def __init__(self):
        """Initialise."""
        self.a_week = timedelta(days=7)
        # print("A week is: {}".format(self.a_week))
        self.tz = pytz.timezone("Europe/London")
        # The date this rota starts at

        # ===-===-===-===-===-===-===-===-===-===-===-===-
        # TODO this should be changed to be loaded from the rota csv files
        self.start_date = date(2022, 2, 4)
        # ===-===-===-===-===-===-===-===-===-===-===-===-

        # defaults
        self.year = str(datetime.now().year)

        # if Sept - Dec add b to file name
        if datetime.now().month >= 9:
            self.year += 'b'

        self.rota_time_start = 14
        self.rota_time_end = 15
        # default location
        # self.rota_location = ("D449, University of Hertfordshire, " +
        #                       "College Lane, Hatfield, UK, AL10 9AB")

        self.rota_location = ("Online")
        # Update these to change the source csv and the output files
        self.rota_data_file = "scripts/rota-data-{}.csv".format(self.year)

        self.rota_rst = "rota-{}.txt".format(self.year)
        self.rota_ical = "rota-{}.ics".format(self.year)

        # this is the data dictionary we populate
        self.rota_data = []
        # the ad-hoc sessions that are not part of the regular weekly seminar
        # session
        self.additional_sessions = []

        # header for the table that will be generated, and sourced by our
        # seminar page
        self.table_header = """
        .. csv-table::
        \t:header: **#**, **Name**, **Title**, **Date**
        \t:widths: 5, 35, 85, 10
        \t:quote: "
        """

    def get_rota_data(self):
        """
        Load data from csv file.

        This method loads data from the csv file into our list.
        """
        with open(self.rota_data_file) as csvfile:
            data_reader = csv.reader(csvfile)
            rota_data = list(data_reader)

        for aline in rota_data:
            logging.debug("Processing {}".format(aline))
            v1, v2, v3, s_date, stime, etime, location, to_post = aline
            # Only automatically fill in regular seminar sessions
            if to_post == '1':
                if s_date != '0':
                    rota_date = datetime.strptime(s_date, "%Y-%m-%d").date()
                else:
                    rota_date = None

                if stime != '0':
                    rota_time_start = datetime.strptime(stime, "%H%M").time()
                else:
                    rota_time_start = None

                if etime != '0':
                    rota_time_end = datetime.strptime(etime, "%H%M").time()
                else:
                    rota_time_end = None

                if location == '0':
                    location = None

                logging.debug(
                    "Added to rota_data: {}".format(
                        [v1, v2, v3, rota_date, rota_time_start,
                         rota_time_end, location, to_post]))
                self.rota_data.append([v1, v2, v3, rota_date, rota_time_start,
                                       rota_time_end, location, to_post])
            else:
                if s_date != '0':
                    rota_date = datetime.strptime(s_date, "%Y-%m-%d").date()
                else:
                    logging.error(
                        "Date must be provided for all ad-hoc sessions.")

                if stime != '0':
                    rota_time_start = datetime.strptime(stime, "%H%M").time()
                else:
                    logging.error(
                        "Start time must be provided for all ad-hoc sessions.")

                if etime != '0':
                    rota_time_end = datetime.strptime(etime, "%H%M").time()
                else:
                    logging.error(
                        "Start time must be provided for all ad-hoc sessions.")

                if location == '0':
                    logging.error(
                        "Location must be provided for all ad-hoc sessions.")

                logging.debug(
                    "Added to additional_sessions: {}".format(
                        [v1, v2, v3, rota_date, rota_time_start,
                         rota_time_end, location, to_post]))
                self.additional_sessions.append(
                    [v1, v2, v3, rota_date, rota_time_start,
                     rota_time_end, location, to_post])

    def fill_up_dates(self):
        """Fill in missing dates."""
        self.all_events = []
        current_date = self.start_date
        scheduled_dates = []
        skipped_dates = []

        for data in self.rota_data:
            [name, talk_title, title_blog, rota_date, start_time, end_time,
             location, post] = data
            # if a date is given
            if rota_date:
                # if it is marked as a holiday, add it to skip list
                if name == "Holiday":
                    skipped_dates.append(rota_date)
                    logging.info("{} marked as a Holiday".format(rota_date))
                # otherwise, add it to pre-scheduled dates
                else:
                    scheduled_dates.append(rota_date)

        all_skipped = skipped_dates + scheduled_dates
        logging.info("The following dates are pre-occupied: ")
        for adate in sorted(all_skipped):
            logging.info(adate)

        # first fill up our regular sessions
        for data in self.rota_data:
            [name, talk_title, title_blog, rota_date, start_time, end_time,
             location, to_post] = data

            # Fill up defaults for information that hasn't been mentioned in
            # the CSV, but only for Biocomputation seminars
            if not rota_date:
                # if the current week is already occupied, use next week
                rota_date = current_date
                while True:
                    if rota_date in all_skipped:
                        rota_date += self.a_week
                    break

            # if the title is empty, we don't have a talk
            if not talk_title:
                talk_title = "--"
            # if the URL is empty, we add an empty one
            if not title_blog:
                title_blog = "<#>"
            else:
                title_blog = "<{{filename}}/{}>".format(title_blog)

            if not location:
                location = self.rota_location

            if not start_time:
                start_time = timedelta(hours=self.rota_time_start)
            else:
                start_time = timedelta(hours=start_time.hour,
                                       minutes=start_time.minute)

            if not end_time:
                end_time = timedelta(hours=self.rota_time_end)
            else:
                end_time = timedelta(hours=end_time.hour,
                                     minutes=end_time.minute)

            current_date = rota_date + self.a_week

            all_skipped.append(rota_date)
            if name == "---":
                logging.debug("Skipping session on {}".format(rota_date))
            else:
                logging.debug("Added to rota: {}".format(
                    [name, talk_title, title_blog, rota_date, start_time,
                     end_time, location, to_post]))
                self.all_events.append((name, talk_title, title_blog,
                                        rota_date, start_time, end_time,
                                        location, to_post))

        # fill up the ad-hoc sessions
        for data in self.additional_sessions:
            [name, talk_title, title_blog, rota_date, start_time, end_time,
             location, to_post] = data
            start_time = timedelta(hours=start_time.hour,
                                   minutes=start_time.minute)
            end_time = timedelta(hours=end_time.hour,
                                 minutes=end_time.minute)

            logging.debug("Added to additional: {}".format(
                [name, talk_title, title_blog, rota_date, start_time, end_time,
                 location, to_post]))
            self.all_events.append((name, talk_title, title_blog, rota_date,
                                    start_time, end_time, location, to_post))
        # sort by date so that I don't have to
        self.all_events.sort(key=lambda x: x[3])

        for row in self.all_events:
            if row[3] > date.today():
                # TODO replace with f string
                logging.info(
                    "Next session: {} on {} from {} to {} in {}.".format(
                        row[0], row[3].strftime("%d/%m/%y"), row[4], row[5],
                        row[6]))
                break

    def print_to_rst(self):
        """Print an rst file."""
        rst_file = open(self.rota_rst, 'w')
        counter = 1
        if not rst_file:
            logging.critical("Error creating RST file")
            sys.exit(-1)

        print(textwrap.dedent(self.table_header), file=rst_file)
        for data in self.all_events:
            name, talk_title, title_blog, rota_date, start_time, end_time,\
                location, to_post = data
            # Only publish to website if we want it to
            if to_post == '1':
                if name == "Holiday" or name == "Cancelled" or name == "--":
                    # TODO replace with f string
                    print("\t{}, {}, \"`{} {}`__\", {}".format(
                        "--", name, talk_title, title_blog,
                        rota_date.strftime("%d/%m/%y")), file=rst_file)
                else:
                    print("\t{}, {}, \"`{}\ {}`__\", {}".format(
                    # TODO replace with f string
                        counter, name, talk_title, title_blog,
                        rota_date.strftime("%d/%m/%y")), file=rst_file)
                    counter += 1

        print(file=rst_file)
        rst_file.close()
        logging.info("RST file written: {}".format(self.rota_rst))

    def generate_ical(self):
        """Generate an ical file."""
        logging.debug("Printing ics file")
        cal = icalendar.Calendar()
        ical_file = open(self.rota_ical, 'w')
        counter = 1

        if not ical_file:
            logging.error("Error creating ical file.")
            sys.exit(-1)

        for data in self.all_events:
            logging.debug("{}".format(data))
            name, talk_title, title_blog, rota_date, start_time, end_time,\
                location, publish = data
            rota_date = datetime.combine(rota_date, datetime.min.time())
            rota_date = rota_date.replace(tzinfo=self.tz)
            session = icalendar.Event()
            session['uid'] = rota_date.isoformat()
            session['dtstart'] = icalendar.vDatetime(rota_date +
                                                     start_time)
            session['dtend'] = icalendar.vDatetime(rota_date +
                                                   end_time)
            session['location'] = icalendar.vText(location)
            session['summary'] = icalendar.vText("{} - {}".format(name,
                                                                  talk_title))

            cal.add_component(session)

            counter += 1

        new_cal = cal.to_ical().decode('utf-8').replace('\r\n', '\n').strip()
        # print(new_cal)
        print(new_cal, file=ical_file)
        ical_file.close()
        logging.info("ICS file written: {}".format(self.rota_ical))


if __name__ == "__main__":
    logging.basicConfig(
        format='%(funcName)s: %(levelname)s: %(message)s',
        level=logging.INFO)
    generator = generateRota()
    generator.get_rota_data()
    generator.fill_up_dates()
    generator.print_to_rst()
    generator.generate_ical()
