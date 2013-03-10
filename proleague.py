# TODO  --  dates and incomplete checking

import sys
import re
import pycurl
import cStringIO
from random import randint

# globals
spoilers = False
season = 'sanity'

def getPageMatches(page = 1):
    """ Gets a list, matches, with the matches found in the page requested
        arguments: Page number :- page
        returns: A list of  
    """
    import pycurl
    import cStringIO

    buf = cStringIO.StringIO()
    src = 'http://www.twitch.tv'
    src2 = src
    if page == 1:
        src2 = src + '/sc2proleague/videos'
    else:
        src2 = src + '/sc2proleague/videos?page='+str(page)

    c = pycurl.Curl()
    c.setopt(c.URL, src2)
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    
    data = buf.getvalue()
    
    ro = re.compile(r'<a href=(.*SPL.*)</a>')
    mo = re.finditer(ro, data)

    matches = list()
    if mo:
        for r in mo:
            m_str = r.group()
            vid_url = src + m_str[9:32]
            game = m_str[67:-4]
#                                      p1     t1    p2    t2      set
            a = re.compile(r'.*\[SPL\](.*)\[(.*)\](.*)\[(.*)\].*(\d{1}SET).*')
            b = re.search(a, game)
            if b:
                match = (b.group(2) + ' vs ' + b.group(4), b.group(1) + b.group(3), b.group(5), vid_url)
                matches.append(match)
            else:
                print "broke"
    return matches

def getSeason():
    """Returns the current season and next game"""
    url = 'http://www.twitch.tv/sc2proleague/videos'
    buf = cStringIO.StringIO()
    
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    
    data = buf.getvalue()
    
    ti_re = re.compile(r'\"(Proleague Season .*)\"')
    ti_mo = re.finditer(ti_re, data)
    season = ''
    if ti_mo:
        for ti in ti_mo:
            curr = ti.group()
            season = curr[1:-1]
    else:
        season = 'OGN Proleague'
    return season

def uniquify(seq):
    """Returns the list without repeats (order perserving)"""
   # order preserving
    checked = []
    for e in seq:
        if e not in checked:
            checked.append(e)
    return checked

def getGames(pages = 2):
    """ Wrapper for getPageMatches """
    matches = list()
    for i in range(0, pages):
        matches.extend( getPageMatches(i+1) )

    season = getSeason()
    print "\n"+season
        
    series = list()
    series = uniquify([x[0] for x in matches])

    splut = matches[0][3].split('/')
    base = int(splut[-1])

    if spoilers:
        for siri in series:
            print (' ')
            print siri
            for i in range(1, 8):
                for match in matches:
                    if match[0] == siri and match[2] == str(i)+'SET':
                        print str(i)+'SET' + "\t" + match[-1] + "\t" + match[1]

    else:
        for siri in series:
            print (' ')            
            print siri
            for i in range (1, 8):
                flag = False
                for match in matches:
                    if  match[0] ==  siri and match[2] == str(i)+'SET':
                        print match[2] + "\t" + match[-1]
                        flag = True                        
                if flag == False:
                    x = randint(2, 200)
                    x += base
                    print str(i)+'SET' + "\t" + "http://www.twitch.tv/sc2proleague/c/" + str(x)
                    
    print " "

def usage():
    print "python proleague4.py [page number to parse up to] [s - will include spoilers]"

if __name__ == "__main__":
    if len(sys.argv) == 1:
        getGames()
    elif len(sys.argv) in (2, 3):
        if 's' in sys.argv:
            spoilers = True
            if len(sys.argv) == 2:
                getGames()
        for arg in sys.argv:
            if re.match(r'\d', arg):
                getGames(int(arg))
    else:
        usage()
        sys.exit()

    print 'Note: Last series may be incomplete!\n'
    
