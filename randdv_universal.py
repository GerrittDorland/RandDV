import webbrowser, time, random, urllib2, urllib
from HTMLParser import HTMLParser
import xml.etree.ElementTree as ET

sideshowRss = "www.superfreaksideshow.com/members3/wp-content/plugins/s2member-files/s2member-file-inline/s2member-file-remote/"

def usage():
    print '---------------------'
    print 'Enter \"superfreak\" to enter your Sideshow credentials.'
    print 'Enter \"help\" or \"?\" to pull this menu up again.'
    print '---------------------'

def parseXmlBullshit(xml, big_list):
    count = 0
    for rss in xml:
        count = count + 1
        print 'Parsing year... ' + str(count) + ' of ' + str(len(xml)) + '...'
        e = ET.parse(rss).getroot()
        for child in e:
            for kiddie in child.findall('item'):
                for lilbaby in kiddie.findall('enclosure'):
                    big_list.append(lilbaby.get('url'))
    del e

def load_SFSS(uname, pw, sfss_list):
    sshow_list = []
    sfssrss = []
    for show in sfss_list:
        if(len(show) > 8):
            if str(show[7]+show[8]) == "16":
                sshow_list.append(show)

    print 'loading 0%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "podcast.xml"))
    print 'Current Year downloaded. loading 9%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "2015.xml"))
    print '2015 downloaded. loading 18%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "2014.xml"))
    print '2014 downloaded. loading 27%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "2013.xml"))
    print '2013 downloaded. loading 36%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "2012.xml"))
    print '2012 downloaded. loading 45%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "2011.xml"))
    print '2011 downloaded. loading 54%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "2010.xml"))
    print '2010 downloaded. loading 63%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "2007.xml"))
    print '2007 downloaded. loading 72%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "2006.xml"))
    print '2006 downloaded. loading 81%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "2005.xml"))
    print '2005 downloaded. loading 90%...'
    sfssrss.append(urllib.urlopen("http://" + uname + ":" + pw + "@" + sideshowRss + "2004.xml"))
    print '2004 downloaded. loading 100%!'

    print 'Parsing the shows...'
    parseXmlBullshit(sfssrss, show_list)
    print 'Parsing complete! Enjoy! You can now use the randomizer as you normally would.'

class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
                if tag == 'a':
                        for name, show in attrs:
                                if show[0] != "/":
                                    showlist.append(show)

success = 0
showlist = []
sshowlist = []
todays_show = time.strftime("%m%d%y")
btodays_show_available = False
todays_show_index = -1
bloadShow = False
showlink = ""
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
usage()

for show in showlist:
    if todays_show in show:
        btodays_show_available = True
        todays_show_index = showlist.index(show)

while(1):
        data = raw_input()

        if data.find("today") != -1 or data.find("t") != -1 or data.find("fuck") != -1:
            if btodays_show_available:
                bloadShow = True
                showlink = TLD + showlist[todays_show_index]
            else:
                bloadShow = False
                print 'Today\'s show is unavailable here.'
                print 'Either it hasn\'t been posted yet, or is a Sideshow Exclusive.'
                print 'Feel free to check here:'
                print 'http://www.superfreaksideshow.com/members3/category/podcasts/'
                print '---------------------'
        elif len(data) < 1:
            bloadShow = True
            showlink = TLD + showlist[random.randint(1,len(showlist))]
        elif data == "sideshow" or data == "superfreak" or data == "s":
            

            load_SFSS(username, password, sshowlist)

        elif data == "?" or data == "help":
            usage()

        if bloadShow == True:
            if len(showlink) > 1:
                try:
                        response = urllib2.urlopen(showlink)
                        success = 1

                except urllib2.HTTPError:
                        success = 0
                        print "No Show / Bad generation. Trying again..."
                        print '---------------------'

                if success is 1:
                        success = 0
                        print "Loading show: " + showlink
                        print '---------------------'
                        webbrowser.open(showlink)

            else:
                    print 'Show loading failed.'
                    print '---------------------'
