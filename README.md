Proleague
=========

Do you hate getting your starcraft 2 proleague spoiled? This command line utility can help!

# Description
This program curls the starcraft 2 proleague page and organizes the games in a spoiler free way.    

    WOONGJIN vs SAMSUNG
    1SET  http://www.twitch.tv/sc2proleague/c/1990818
    2SET	http://www.twitch.tv/sc2proleague/c/1990861
    3SET	http://www.twitch.tv/sc2proleague/c/1990866
    4SET	http://www.twitch.tv/sc2proleague/c/1990924
    5SET	http://www.twitch.tv/sc2proleague/c/1990940
    6SET	http://www.twitch.tv/sc2proleague/c/1990968
    7SET	http://www.twitch.tv/sc2proleague/c/1990949
     
    CJ vs 8TH
    1SET	http://www.twitch.tv/sc2proleague/c/1990533
    2SET	http://www.twitch.tv/sc2proleague/c/1990633
    3SET	http://www.twitch.tv/sc2proleague/c/1990674
    4SET	http://www.twitch.tv/sc2proleague/c/1990669
    5SET	http://www.twitch.tv/sc2proleague/c/1991119
    6SET	http://www.twitch.tv/sc2proleague/c/1991112
    7SET	http://www.twitch.tv/sc2proleague/c/1991024
     
    EGTL vs SKT
    1SET	http://www.twitch.tv/sc2proleague/c/1987286
    2SET	http://www.twitch.tv/sc2proleague/c/1987320
    3SET	http://www.twitch.tv/sc2proleague/c/1987330
    4SET	http://www.twitch.tv/sc2proleague/c/1987365
    5SET	http://www.twitch.tv/sc2proleague/c/1991140
    6SET	http://www.twitch.tv/sc2proleague/c/1991013
    7SET	http://www.twitch.tv/sc2proleague/c/1991026
     
    KT vs STX
    1SET	http://www.twitch.tv/sc2proleague/c/1986956
    2SET	http://www.twitch.tv/sc2proleague/c/1986957
    3SET	http://www.twitch.tv/sc2proleague/c/1987066
    4SET	http://www.twitch.tv/sc2proleague/c/1987081
    5SET	http://www.twitch.tv/sc2proleague/c/1987275
    6SET	http://www.twitch.tv/sc2proleague/c/1987278
    7SET	http://www.twitch.tv/sc2proleague/c/1991098
     
    EG-TL vs KT
    1SET	http://www.twitch.tv/sc2proleague/c/1991068
    2SET	http://www.twitch.tv/sc2proleague/c/1991079
    3SET	http://www.twitch.tv/sc2proleague/c/1991070
    4SET	http://www.twitch.tv/sc2proleague/c/1966177
    5SET	http://www.twitch.tv/sc2proleague/c/1991020
    6SET	http://www.twitch.tv/sc2proleague/c/1991110
    7SET	http://www.twitch.tv/sc2proleague/c/1991013
    
It makes up fake (and believable) urls for sets that may not actually exist.

# Running the program
Run this in your command line with 

    python proleague.pyc
    
# Parameters
The s flag displays spoilers, including the proper number of games and and the players

    python proleague.pyc s

A number flag will display that number of "pages" of games. 

    python proleague.pyc 4
    
All combinations work

    python proleague.pyc s 5
