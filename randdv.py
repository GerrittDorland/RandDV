import webbrowser, win32api, win32con, time, random, urllib2

doit = 0


while(1):
        if(win32api.GetAsyncKeyState(win32con.VK_RCONTROL)):
           doit = 1

        if doit is 1:
            doit = 0
            m = random.randint(1, 12)
            d = random.randint(1, 31)
            y = random.randint(7, 18)

            if y < 10:
                stry = "0" + str(y)
            else:
                stry = str(y)
            if d < 10:
                strd = "0" + str(d)
            else:
                strd = str(d)
            if m < 10:
                strm = "0" + str(m)
            else:
                strm = str(m)

            try:
                    response = urllib2.urlopen("http://www.distortednews.com/podshows/dv_" + strm + strd + stry + "_64.mp3")
                    
            except urllib2.HTTPError:
                    doit = 1
                    print "No Show / Bad generation. Trying again..."

            if doit is 0:
                print "Loading show: " + "dv_" + strm + strd + stry + "_64.mp3"
                webbrowser.open("http://www.distortednews.com/podshows/dv_" + strm + strd + stry + "_64.mp3")

        else:
            time.sleep(5)
            
