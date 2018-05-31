#!/usr/bin/perl
#
# Simple perl script
# Fetches each publication RSS feed, find the link to the publication page, and fetches the bib
# No API for RIS, so this is EXTREMELY HACKY! Worlds may collide!

use 5.10.0;
use Data::Dumper;
use WWW::Mechanize;
use File::Fetch;
use Getopt::Std;
use XML::Feed;

use strict;
use warnings;
# Time out after 30 seconds if a download doesn't succeed
# $File::Fetch::TIMEOUT = 30;

# Options
my %options = ();
getopts("hdcitf:", \%options);

if (defined $options{h})
{
    print("check-new-pubs-on-ris.pl: Check RIS for new publications\n\n");
    print("OPTIONS:\n");
    print("-h: print help and exit\n");
    print("-d: delete older files (unimplemented)\n");
    print("-c: check only, do not download torrent files\n");
    exit 0;
}

my $RIS_root_URL = "http://researchprofiles.herts.ac.uk/portal/en/persons";

# Need to be hard coded. Hard to post to the search box, and then find the right people.
my @user_URLs = (
    "michael-schmuker(fda08dd2-790b-4871-92cb-324b9f1e4267)",
    # "volker-steuber(43b1e474-9894-40d4-8eed-470dd7a7f29e)"
);



foreach my $user_URL (@user_URLs)
{
    my $pub_rss_URL = "$RIS_root_URL/$user_URL/publications.rss";
    print("-> Fetching rss feed: $pub_rss_URL\n");
    my $feed = XML::Feed->parse(URI->new($pub_rss_URL))
            or die XML::Feed->errstr;
    for my $entry ($feed->entries)
    {
        # print $entry->title, "\n", $entry->link, "\n\n";
        my $title = $entry->title;
        my $link = $entry->link;
        $link =~ s/\.html$/\/export\.html/g;

        print("$title: $link\n\n");
    }
}
