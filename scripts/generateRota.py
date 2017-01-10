#!/usr/bin/env python3
# vim: set fileencoding=utf-8
"""
Generate rst rota to be included into the seminar page.

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
        self.start_date = date(2016, 5, 20)
        # print("A week after current is: {}".format(self.start_date +
        #                                            self.a_week))
        self.year = 2016
        # 4 in the afternoon
        self.rota_time_start = 16
        self.rota_time_end = 17
        self.the_time_start = timedelta(hours=self.rota_time_start)
        self.the_time_end = timedelta(hours=self.rota_time_end)
        self.rota_location = ("LB252, University of Hertfordshire, " +
                              "College Lane, Hatfield, UK, AL10 9AB")
        # since it'll be run using the makefile
        self.rota_data_file = "scripts/rota-data-{}.csv".format(self.year)
        self.rota_rst = "rota-{}.txt".format(self.year)
        self.rota_ical = "rota-{}.ics".format(self.year)

        # this is the data dictionary
        # name, title, rst blog post filename, date if available
        # auto generates the date if missing
        self.rota_data = []

        self.table_header = """
        .. csv-table::
        \t:header: **#**, **Name**, **Title**, **Date**
        \t:widths: 5, 35, 85, 10
        \t:quote: "
        """

    def get_rota_data(self):
        """Load data from text file."""
        with open(self.rota_data_file) as csvfile:
            data_reader = csv.reader(csvfile)
            rota_data = list(data_reader)

        for v1, v2, v3, s_date in rota_data:
            if s_date != '0':
                rota_date = datetime.strptime(s_date, "%Y-%m-%d").date()
            else:
                rota_date = None

            self.rota_data.append([v1, v2, v3, rota_date])

    def fill_up_dates(self):
        """Fill in missing dates."""
        self.rota = []
        current_date = self.start_date
        # print("Current date: {}".format(current_date))
        scheduled_dates = []
        skipped_dates = []

        for data in self.rota_data:
            name, talk_title, title_blog, rota_date = data
            if rota_date:
                if name == "Holiday":
                    skipped_dates.append(rota_date)
                else:
                    scheduled_dates.append(rota_date)
                # print("{}, \"{}\", \"{}\", {}".format(
                #    name, talk_title, title_blog,
                #    rota_date.strftime("%d/%m/%y")))

        print("Occupied dates: ")
        all_skipped = skipped_dates + scheduled_dates
        for date in sorted(all_skipped):
            print(date)

        # print()
        # print("[Output] Completed rota: ")

        for data in self.rota_data:
            name, talk_title, title_blog, rota_date = data

            if not rota_date:
                # print("Current date: {}".format(current_date))
                rota_date = current_date

                while rota_date in skipped_dates or \
                        rota_date in scheduled_dates:
                    # print("Date {} occupied.  Skipping".format(
                        # rota_date))
                    rota_date += self.a_week
                    continue

            if not talk_title:
                talk_title = "--"
            if not title_blog:
                title_blog = "<#>"
            else:
                title_blog = "<{{filename}}/{}>".format(title_blog)

            scheduled_dates.append(rota_date)
            self.rota.append((name, talk_title, title_blog, rota_date))
            # print("Added: {}, \"{}\", \"{}\", {}".format(
            #    name, talk_title, title_blog,
            #    rota_date.strftime("%d/%m/%y")))

            current_date = rota_date + self.a_week

        # sort by date so that I don't have to
        self.rota.sort(key=lambda x: x[3])

        for row in self.rota:
            if row[3] > date.today():
                print("{} is to take the next session on {}.".format(
                    row[0], row[3].strftime("%d/%m/%y")))
                break

    def print_to_rst(self):
        """Print an rst file."""
        rst_file = open(self.rota_rst, 'w')
        counter = 1
        if not rst_file:
            print("Error creating rst file.", file=sys.stderr)
            sys.exit(-1)

        print(textwrap.dedent(self.table_header), file=rst_file)
        for data in self.rota:
            name, talk_title, title_blog, rota_date = data
            if name == "Holiday" or name == "Cancelled" or name == "--":
                print("\t{}, {}, \"`{} {}`__\", {}".format(
                    "--", name, talk_title, title_blog,
                    rota_date.strftime("%d/%m/%y")), file=rst_file)
            else:
                print("\t{}, {}, \"`{}\ {}`__\", {}".format(
                    counter, name, talk_title, title_blog,
                    rota_date.strftime("%d/%m/%y")), file=rst_file)
                counter += 1

        print(file=rst_file)
        rst_file.close()
        print()
        print("[Output] Rst file written: {}".format(self.rota_rst))

    def generate_ical(self):
        """Generate an ical file."""
        cal = icalendar.Calendar()
        ical_file = open(self.rota_ical, 'w')
        counter = 1

        if not ical_file:
            print("Error creating ical file.", file=sys.stderr)
            sys.exit(-1)

        for data in self.rota:
            name, talk_title, title_blog, rota_date = data
            rota_date = datetime.combine(rota_date, datetime.min.time())
            rota_date = rota_date.replace(tzinfo=self.tz)
            session = icalendar.Event()
            session['uid'] = rota_date.isoformat()
            session['dtstart'] = icalendar.vDatetime(rota_date +
                                                     self.the_time_start)
            session['dtend'] = icalendar.vDatetime(rota_date +
                                                   self.the_time_end)
            session['location'] = icalendar.vText(self.rota_location)
            session['summary'] = icalendar.vText("{} - {}".format(name,
                                                                  talk_title))

            cal.add_component(session)

            counter += 1

        new_cal = cal.to_ical().decode('utf-8').replace('\r\n', '\n').strip()
        # print(new_cal)
        print(new_cal, file=ical_file)
        ical_file.close()
        print("[Output] ics file written: {}".format(self.rota_ical))


if __name__ == "__main__":
    generator = generateRota()
    generator.get_rota_data()
    generator.fill_up_dates()
    generator.print_to_rst()
    generator.generate_ical()
