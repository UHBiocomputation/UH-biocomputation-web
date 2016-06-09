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
import icalendar
import sys
import textwrap
import pytz


class generateRota:

    """
    Generates the rota rst to be included in the website.

    Also generates an ics file that people can subscribe to.
    """

    def __init__(self):
        """Initialise."""
        self.a_week = timedelta(days=7)
        self.tz = pytz.timezone("Europe/London")
        # The date this rota starts at
        self.start_date = datetime(2016, 5, 20, tzinfo=self.tz)
        self.year = 2016
        # 4 in the afternoon
        self.rota_time_start = 16
        self.rota_time_end = 17
        self.the_time_start = timedelta(hours=self.rota_time_start)
        self.the_time_end = timedelta(hours=self.rota_time_end)
        self.rota_location = "LB252, University of Hertfordshire, College Lane, Hatfield, AL10 9AB, UK"
        self.rota_rst = "rota-{}.rst".format(self.year)
        self.rota_ical = "rota-{}.ics".format(self.year)

        # this is the data dictionary
        # name, title, rst blog post filename, date if available
        # auto generates the date if missing
        self.rota_data = (
            ("James Bower", "What does the nose know and how does it know it",
             "20160513-what-does-the-nose-know-and-how-does-it-know-it.rst",
             ""),
            ("Jean Petrić", "The jinx on the NASA software defect data sets",
             "20160525-the-jinx-on-the-nasa-software-defect-data-sets.rst",
             ""),
            ("Alex Hocking", "Convolutional neural networks",
             "20160601-convolutional-neural-networks.rst", ""),
            ("Christoph Metzner", "", "", ""),
            ("Guest session", "", "", datetime(2016, 6, 17)),
            ("Gui Valente", "", "", datetime(2016, 6, 24)),
            ("Nathan Beka", "", "", ""),
            ("Ankur Sinha", "", "", ""),
            ("Neil Davey", "", "", ""),
            ("Volker Steuber", "", "", ""),
            ("Rene Boekhorst", "", "", ""),
            ("Benjamin Torben-Nielsen", "", "", ""),
            ("Julia Goncharenko", "", "", ""),
            ("Weam Binjumah", "", "", ""),
            ("Yi Sun", "", "", ""),
            ("Maria Psarrou", "", "", ""),
            ("Jean Petrić", "", "", ""),
            ("Maria Schilstra", "", "", ""),
            ("Edward Wakelam", "", "", ""),
            ("Marco Craveiro", "", "", ""),
            ("Nathan Beka", "", "", ""),
            ("Deepak Panday", "", "", ""),
            ("Roderick Adams", "", "", ""),
            ("Ronak Bhavsar", "", "", ""),
            ("Anuradha Sulane", "", "", ""),
            ("Zaheed Mahmood", "", "", "")
        )

        self.table_header = """
        .. csv-table::
        :header: **#**, **Name**, **Title**, **Date**
        :widths: 5, 35, 85, 10
        """

    def fill_up_dates(self):
        """Fill in missing dates."""
        self.rota = []
        current_date = self.start_date
        scheduled_talks = []
        scheduled_dates = []

        print("Talks already booked: ")
        for data in self.rota_data:
            name, talk_title, title_blog, rota_date = data
            if rota_date:
                scheduled_dates.append((name, talk_title, title_blog,
                                        rota_date))
                print("{}, \"{}\", \"{}\", {}".format(name, talk_title,
                                                      title_blog, rota_date))

        print()
        print("[Output] Completed rota: ")

        for data in self.rota_data:
            name, talk_title, title_blog, rota_date = data
            if not talk_title:
                talk_title = "--"
            if not title_blog:
                title_blog = "<#>"
            else:
                title_blog = "<{{filename}}/{}>".format(title_blog)
            if not rota_date:
                rota_date = current_date
                while True:
                    if rota_date in scheduled_dates:
                        rota_date += self.a_week
                    else:
                        break

            current_date = rota_date + self.a_week
            self.rota.append((name, talk_title, title_blog, rota_date))
            print("{}, \"{}\", \"{}\", {}".format(name, talk_title,
                                                  title_blog, rota_date))

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
            print("{}, {}, `{} {}`__, {}".format(counter, name, talk_title,
                                                 title_blog, rota_date),
                  file=rst_file)
            counter += 1

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
    generator.fill_up_dates()
    generator.print_to_rst()
    generator.generate_ical()
