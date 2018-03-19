import webbrowser, win32api, win32con, time, random, urllib2
from HTMLParser import HTMLParser

doit = 0
success = 0
linklist = []

class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
                if tag == 'a':
                        for name, show in attrs:
                                
                                linklist.append(show)

parser = MyHTMLParser()
TLD = "http://www.distortednews.com/podshows/"
website = urllib2.urlopen(TLD)
html = website.read()
parser.feed(html)

while(1):
        if(win32api.GetAsyncKeyState(win32con.VK_RCONTROL)):
                doit = 1
                print 'trying...'

        if doit is 1:
                doit = 0
                showlink = TLD + linklist[random.randint(1,len(linklist))]
                print showlink

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
                        time.sleep(5)
            
