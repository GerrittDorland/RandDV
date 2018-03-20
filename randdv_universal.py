import webbrowser, time, random, urllib2
from HTMLParser import HTMLParser

success = 0
showlist = []
todays_show = time.strftime("%m%d%y")
btodays_show_available = False
todays_show_index = -1
showlink = ""


class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
                if tag == 'a':
                        for name, show in attrs:

                                showlist.append(show)

parser = MyHTMLParser()
TLD = "http://www.distortednews.com/podshows/"
try:
        website = urllib2.urlopen(TLD)
except urllib2.HTTPError:
        print 'Tim moved the show. This script is broken until I fix it.'
        exit(0)
html = website.read()
parser.feed(html)
print 'Ready. Press [ENTER] while this window is focused to request a new show.'

for show in showlist:
    if todays_show in show:
        btodays_show_available = True
        todays_show_index = showlist.index(show)

while(1):
        data = raw_input()

        if data.find("today") != -1 or data.find("t") != -1 or data.find("fuck") != -1:
            if btodays_show_available:
                showlink = TLD + showlist[todays_show_index]
            else:
                bloadShow = False
                print 'Today\'s show is unavailable here.'
                print 'Either it hasn\'t been posted yet, or is a Sideshow Exclusive.'
                print 'Feel free to check here:'
                print 'http://www.superfreaksideshow.com/members3/category/podcasts/'
        else:
            showlink = TLD + showlist[random.randint(1,len(showlist))]

        if len(showlink) > 1:
            try:
                    response = urllib2.urlopen(showlink)
                    success = 1

            except urllib2.HTTPError:
                    success = 0
                    print "No Show / Bad generation. Trying again..."

            if success is 1:
                    success = 0
                    print "Loading show: " + showlink
                    webbrowser.open(showlink)

        else:
                print 'Show loading failed.'
