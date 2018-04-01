import subprocess
import sys
import re
import os
import os.path
import glob
from io import BytesIO
import requests
import tweepy
from PIL import Image
from PIL import ImageFile

from secrets import *

##create OAuthHandler instance
#Twitter reqs all requests use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#constuct API instance
api = tweepy.API(auth)

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

def tweettweet(username, status_id, stat):
    #filename = 'temp.png'
    #send a get request
    #request = requests.get(url, stream=True)
    print('checking status?')
    #if request.status_code == 200:
        #i = Image.open(BytesIO(request.content))
        #save image under given filename
        #i.save(filena
    #statusstr = '@{0}'.format(username)+' '+stat[0]
    statusstr = '@exfann '+stat[0]

    #statusstr = 'hey this is just some text im puttin out there to show that this actually works sorta woo'
    #api.update_status(status = statusstr, in_reply_to_status_id = status_id)
    api.update_with_media(stat[1], status = statusstr)
    print("sent")
    #sys.exit()

def tweettweet2(webn, stat):
    #filename = 'temp.png'
    #send a get request
    #request = requests.get(url, stream=True)
    print('checking status?')
    #if request.status_code == 200:
        #i = Image.open(BytesIO(request.content))
        #save image under given filename
        #i.save(filena
    #statusstr = '@{0}'.format(username)+' '+stat[0]
    statusstr = '@exfann '+ webn +' '+ stat[0]

    #statusstr = 'hey this is just some text im puttin out there to show that this actually works sorta woo'
    #api.update_status(status = statusstr, in_reply_to_status_id = status_id)
    if stat[1]:
        api.update_with_media(stat[1], status = statusstr)
    else:
        api.update_status(status = statusstr)
    print("sent")

#def searchy()

def getlink(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    #match = re.search(r'href=[\'"]?([^\'" >]+)', text)
    match = re.search(regex, text)
    if match:
        print (match.group())
        matchy = ''.join(match.group())
        return matchy
    return ''

def RDC(text):
    args = ['java', '-Xmx1024m', '-jar', '/../home/fanne/redecheck/target/redecheck-jar-with-dependencies.jar', '--url', text]
    p = subprocess.Popen(args)
    p.communicate()

def prior():
    owd = os.getcwd()
    subs2 = []
    subs3 = []
    ret = []
    path = '~/testbot/reports/'
    path2 = '/home/fanne/testbot/reports/'
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    #print all_subdirs
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    #print latest_subdir
    os.chdir(os.path.abspath(os.path.expanduser(path)))
    #args = ['ls']
    #p = subprocess.Popen(args, shell=True)
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    path = path+latest_subdir+'/'
    path2 = path2+latest_subdir+'/'
    os.chdir(os.path.abspath(os.path.expanduser(path)))
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    path = path+latest_subdir+'/'
    path2 = path2+latest_subdir+'/'
    os.chdir(os.path.abspath(os.path.expanduser(path)))
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    if all_subdirs:
        latest_subdir = max(all_subdirs, key=os.path.getmtime)
        subs = getsubs('.')
        subs = sorted(subs)
        print subs
        for i in range(len(subs)):
            subsplit = subs[i].split('**')
            subs2.append(int(subsplit[1]))
            subs3.append(int(subsplit[2]))
        print subs2
        print subs3

        #mindex = min(xrange(len(subs2)), key=subs2.__getitem__)
        mindex = subs2.index(min(subs2))
        print mindex
        fr = open('fault-report.txt', 'r')
        reps = fr.read()
        #print reps
        reps = reps.split('\n\n')
        #print reps
        stat = reps[mindex]
        print stat
        path = path+subs[mindex]+'/'
        path2 = path2+subs[mindex]+'/'
        path3  = path2
        #print path
        os.chdir(os.path.abspath(os.path.expanduser(path)))
        datfile = [f for f in os.listdir('.') if os.path.isfile(f)]
        #print datfile
        path = path+datfile[0]+'/'
        path2 = path2+datfile[0]
        #print path
        print path2
        #ret = [stat, path2]
        print ret
        im = Image.open(path2)
        width, height = im.size
        print width, height
        #write the code to crop and such here remember tomorrow but sleep now kay
        im2 = im.crop((0, 0, width, subs3[mindex]+100))
        im2.save("im2.png")
        path3 = path3+"im2.png"
        print path3
        ret = [stat, path3]
        os.chdir(owd)
        return ret
    else:
        fr = open('fault-report.txt', 'r')
        stat = fr.read()
        ret = [stat, None]
        os.chdir(owd)
        return ret

def getsubs(a_dir):
    return [name for name in os.listdir(a_dir)
        if os.path.isdir(os.path.join(a_dir, name))]

class Streamer(tweepy.StreamListener):
    #called when new status arrives
    def on_status(self, status):
        print('status')
        username = status.user.screen_name
        status_id = status.id
        text = status.text
        link = getlink(text)
        if link != '':
            RDC(link)
            ret = prior()
            tweettweet(username, status_id, ret)


#com = raw_input("Search or Stream? \n")
#com = com.upper()
#com = 'STREAM'
com = 'LIST'

if com == 'SEARCH':
    com2 = raw_input("enter search \n")
    for status in tweepy.Cursor(api.search, q = com2, lang = 'en').items():
        #print(status.text)
        if not status.retweeted_status:
            print(status.retweet_count)

elif com == 'STREAM':
    myListener = Streamer()
    #construct new stream
    print('new stream')
    stream = tweepy.Stream(auth, myListener)
    print('filter')
    stream.filter(track=['@TWCaN_Bot', 'new website'])

elif com == 'LIST':
    fil = open('sites.txt', 'r')
    wlist = fil.read()
    wlist = wlist.split('\n')
    for i in range(len(wlist)):
        RDC(wlist[i])
        ret = prior()
        tweettweet2(wlist[i], ret)