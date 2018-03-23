import webbrowser, time, random, urllib2, urllib, sys, os
from HTMLParser import HTMLParser
import xml.etree.ElementTree as ET

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
            if tag == 'a':
                    for name, show in attrs:
                            if show[0] != "/":
                                showlist.append(show)

sideshowRss = "www.superfreaksideshow.com/members3/wp-content/plugins/s2member-files/s2member-file-inline/s2member-file-remote/"
success = 0
isSShowMember = False
ssUname = ""
ssPw = ""
showlist = []
sshowlist = []
sshowdatelist = []
todays_show = time.strftime("%m%d%y")
btodays_show_available = False
todays_show_index = -1
bloadShow = False
showlink = ""
parser = MyHTMLParser()
TLD = "http://www.distortednews.com/podshows/"

def usage():
    print '---------------------'
    print 'Enter \"superfreak\" or \"s\" to enter your Sideshow credentials.'
    print '   After the first time, login will be automatic.\n'
    print 'Enter \"help\" or \"?\" to pull this menu up again.'
    print '---------------------'

def findSShowMember():
    global ssUname
    global ssPw
    #If you are on Windows, change this "/" to "\\"
    file = os.getcwd() + "/" + "freak.lgn"
    try:
        f = open(file, 'r')
        ssUname = f.readline()
        ssUname = ssUname.strip('\n')
        ssPw = f.readline()
        ssPw = ssPw.strip('\n')
        f.close()
        return True
    except:
        "You don't seem to have a login file prepared."
        print '---------------------'
        return False

def validateFreak():
    global ssUname
    global ssPw
    global isSShowMember
    print 'Testing Login...'
    print 'If your Terminal requests additional login information,'
    print 'you fucked up. Close this script and try again you careless fairy.'
    print '   KNOWN BUG: If you fuck this up, go to the CWD of this script and delete'
    print '   freak.lgn. Otherwise you\'ll be stuck in this hell forever.'

    try:
        result = urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "podcast.xml")
    except:
        os.remove(os.getcwd() + "/" + "freak.lgn")
        print 'Unable to log in with provided credentials. TRY AGAIN.'
        print '---------------------'
        return False
    isSShowMember = True
    return True

def createFreak(uname,pw):
    #If you are on Windows, change this "/" to "\\"
    file = os.getcwd() + "/" + "freak.lgn"
    if isSShowMember is True:
        try:
            f = open(file, 'w+')
            f.write(uname + "\n" + pw)
            f.close()
        except:
            print 'Unable to write file. Please move the script somewhere with write permission.'
            print '---------------------'
            return False
        return True
    return False

def getMonth(inmo):
    if inmo.upper() == "JAN":
        return "01"
    elif inmo.upper() == "FEB":
        return "02"
    elif inmo.upper() == "MAR":
        return "03"
    elif inmo.upper() == "APR":
        return "04"
    elif inmo.upper() == "MAY":
        return "05"
    elif inmo.upper() == "JUN":
        return "06"
    elif inmo.upper() == "JUL":
        return "07"
    elif inmo.upper() == "AUG":
        return "08"
    elif inmo.upper() == "SEP":
        return "09"
    elif inmo.upper() == "OCT":
        return "10"
    elif inmo.upper() == "NOV":
        return "11"
    elif inmo.upper() == "DEC":
        return "12"
    return "01"

def parseXmlBullshit(xml):
    global sshowlist
    global sshowdatelist
    count = 0
    for rss in xml:
        count = count + 1
        print 'Parsing year... ' + str(count) + ' of ' + str(len(xml)) + '...'
        e = ET.parse(rss).getroot()
        for child in e:
            for kiddie in child.findall('item'):
                date = kiddie.find('pubDate').text
                date = date.split(' ')
                day = date[1]
                month = getMonth(date[2])
                year = date[3][-2:]

                detectLateShow = date[4].split(':')
                if int(detectLateShow[0]) < 5:
                    day = str(int(day) - 1)
                    if len(day) < 2:
                        day = "0" + day

                for lilbaby in kiddie.findall('enclosure'):
                    sshowlist.append(lilbaby.get('url'))
                sshowdatelist.append(month+day+year)
    del e

def load_SFSS():
    global showlist
    global ssUname
    global ssPw
    sfssrss = []
    removeme = []

    for show in showlist:
        if(len(show) > 8):
            if str(show[7]+show[8]) != "16":
                removeme.append(show)

    for show in removeme:
        showlist.remove(show)
    del removeme[:]

    print 'loading 0%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "podcast.xml"))
    print 'Current Year downloaded. loading 9%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "2015.xml"))
    print '2015 downloaded. loading 18%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "2014.xml"))
    print '2014 downloaded. loading 27%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "2013.xml"))
    print '2013 downloaded. loading 36%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "2012.xml"))
    print '2012 downloaded. loading 45%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "2011.xml"))
    print '2011 downloaded. loading 54%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "2010.xml"))
    print '2010 downloaded. loading 63%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "2007.xml"))
    print '2007 downloaded. loading 72%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "2006.xml"))
    print '2006 downloaded. loading 81%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "2005.xml"))
    print '2005 downloaded. loading 90%...'
    sfssrss.append(urllib.urlopen("http://" + ssUname + ":" + ssPw + "@" + sideshowRss + "2004.xml"))
    print '2004 downloaded. loading 100%!'

    print 'Parsing the shows...'
    parseXmlBullshit(sfssrss)
    print 'Parsing complete! Enjoy! You can now use the randomizer as you normally would.'
    print '---------------------'

def get_todays_show():
    global showlist
    global btodays_show_available
    global todays_show_index
    if isSShowMember == False:
        for show in showlist:
            if todays_show in show:
                btodays_show_available = True
                todays_show_index = showlist.index(show)
    else:
        if todays_show in sshowdatelist:
            btodays_show_available = True
            todays_show_index = sshowdatelist.index(todays_show)

try:
        website = urllib2.urlopen(TLD)
except urllib2.HTTPError:
        print 'Tim moved the show. This script is broken until I fix it.'
        exit(0)
html = website.read()
parser.feed(html)
print '\n\n---------------------'
print '     RANDDV.PY'
print '---------------------'
print 'Ready. Press [ENTER] while this window is focused to request a new show.'
usage()

if isSShowMember is False:
    if findSShowMember() is True:
        if validateFreak() is True:
            load_SFSS()

while(1):
        data = raw_input()

        if data.find("today") != -1 or data.find("t") != -1 or data.find("fuck") != -1:
            get_todays_show()
            if btodays_show_available:
                bloadShow = True
                if isSShowMember == False:
                    showlink = TLD + showlist[todays_show_index]
                else:
                    showlink = "http://" + ssUname + ":" + ssPw + "@" + sshowlist[todays_show_index].replace('http://', '')
            else:
                bloadShow = False
                print 'Today\'s show is unavailable here.'
                print 'Either it hasn\'t been posted yet, or is a Sideshow Exclusive.'
                print 'Feel free to check here:'
                print 'http://www.superfreaksideshow.com/members3/category/podcasts/'
                print '---------------------'
        elif len(data) < 1:
            bloadShow = True

            if isSShowMember == True:
                sizeFree = len(showlist)
                sizeSshow = len(sshowlist)
                upperBound = sizeFree + sizeSshow
                show = random.randint(1,upperBound)
                if show <= sizeFree:
                    showlink = TLD + showlist[show]
                else:
                    showlink = "http://" + ssUname + ":" + ssPw + "@" + sshowlist[show - sizeFree].replace('http://', '')
            else:
                show = showlist[random.randint(1,len(showlist))]
                showlink = TLD + show
        elif data == "sideshow" or data == "superfreak" or data == "s":
            if isSShowMember is False:
                if findSShowMember() is True:
                    if validateFreak() is True:
                        load_SFSS()
                        get_todays_show()
                else:
                    print 'Looks like you need to set your Sideshow Login Credentials.'
                    print 'Please enter your Username and Password. Remember, these aren\'t encrypted so...'
                    print 'Enter at your own risk.'
                    print 'Username:'
                    ssUname = raw_input()
                    ssUname = ssUname.replace("@", "%40")
                    print 'Password:'
                    ssPw = raw_input()
                    print '---------------------'

                    print 'Testing login...'
                    if validateFreak() is True:
                        if createFreak(ssUname, ssPw) is True:
                            print 'Looks like you\'re ready to go! Let\'s load those shows.'
                            print '---------------------'
                            load_SFSS()
                            get_todays_show()
            else:
                print 'You\'re already logged in, dude'
                print '---------------------'

        elif data == "?" or data == "help":
            usage()

        if bloadShow == True:
            if len(showlink) > 1:
                try:
                        response = urllib.urlopen(showlink)
                        success = 1

                except:
                        success = 0
                        print "No Show / Bad generation. Trying again..."
                        print '---------------------'

                if success is 1:
                        success = 0
                        print "Loading show: " + showlink
                        print '\n---------------------'
                        webbrowser.open(showlink)

            else:
                    print 'Show loading failed.'
                    print '---------------------'
