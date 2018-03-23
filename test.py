import os
import subprocess
from PIL import Image


def prior():
    subs2 = []
    subs3 = []
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
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    subs = getsubs('.')
    subs = sorted(subs)
    print subs
    for i in range(len(subs)):
        subsplit = subs[i].split('**')
        subs2.append(subsplit[1])
        subs3.append(subsplit[2])
    print subs2
    print subs3

    mindex = min(xrange(len(subs2)), key=subs2.__getitem__)
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
    ret = [stat, path2]
    print ret
    im = Image.open(path2)
    width, height = im.size
    print width, height
    #write the code to crop and such here remember tomorrow but sleep now kay
    im2 = im.crop((0, 0, width, int(subs3[mindex])+100))
    im2.save("im2.png")
    path3 = path3+"im2.png"
    print path3
    return ret
    


def getsubs(a_dir):
    return [name for name in os.listdir(a_dir)
        if os.path.isdir(os.path.join(a_dir, name))]

prior()