import re
import os


text =" seinfeld.s05e22.dvdrip.xvid-saphire"






for root, dirs, files in os.walk("/home/cada/mnt/ssh/cada@servern/media/tank/orginalrellar/series"):
    head, tail = os.path.split(root)

    series_match = re.compile("(.*)\.s[0-9][0-9]")


    matches =  series_match.match(tail.lower())

    if matches:

        print matches.group(1)


    series_match = re.compile("(.*s)[0-9][0-9]")

    #print series_match.match(tail.lower())

    #print tail
    # print dirs
    # print files

    # print "====="
    # print root
    # print dirs
    # print files
    # print "====="

