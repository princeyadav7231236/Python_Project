import re

mystr = """IN
Search

Avatar image
Home
Explore
Subscriptions
Library
History
Watch later
Liked videos
Python Data Science and Big Data Tutorials In Hindi
Show more
SUBSCRIPTIONS

CodeWithHarry

BB Ki Vines

VEDANTU NEET MADE EJEE

SONU SHARMA

Life Motivation

A2 Motivation {Arvind Arora}

A2 {Amazing Facts}
Show 18 more
MORE FROM YOUTUBE
YouTube Premium
Movies
Gaming
Live
Fashion & Beauty
Learning
Adityakaur456565@gmail.com
Sports
Settings
Report history
Help
Send feedback
AboutPressCopyrightContact usCreatorsAdvertiseDevelopers
TermsPrivacyPolicy & SafetyHow YouTube worksTest new features
© 2021 Google LLC

CodeWithHarry 
1.62M subscribers


Website

Uploads

1:42
NOW PLAYING
C++ Cheatsheet 🧾 for Beginners 🔥🔥
19K views
1 day ago


15:01
NOW PLAYING
Software Interview Rejection - How to handle Failure! 🔥🔥
51K views
3 days ago


2:25
NOW PLAYING
Java Cheatsheet 🧾 for Beginners 🔥🔥
24K views
4 days ago


15:27
NOW PLAYING
Perfect Final Year Project Selection Tips & Tricks (Copy These) 🔥🔥
63K views
6 days ago


2:15
NOW PLAYING
C Language Cheatsheet 🧾 for Beginners 🔥
31K views
6 days ago


2:47
NOW PLAYING
Python Cheatsheet 🧾 for Beginners 🔥🔥
33K views
1 week ago


Popular uploads

11:52:24
NOW PLAYING
Python Tutorial For Beginners In Hindi (With Notes) 🔥
5.1M views
10 months ago


15:13:24
NOW PLAYING
C Language Tutorial For Beginners In Hindi (With Notes) 🔥
5M views
11 months ago


1:13:40
NOW PLAYING
Android Development Tutorial in Hindi
2M views
1 year ago
farhanghos456123@gmail.com

58:48
NOW PLAYING
Project 1: Iron Man Jarvis AI Desktop Voice Assistant | Python Tutorials For Absolute Beginners #120
1.9M views
2 years ago


18:27
NOW PLAYING
Introduction to HTML, CSS, JavaScript & How websites work? | Web Development Tutorials #1
1.7M views
1 year ago


1:45:03
NOW PLAYING
Python Tutorial In Hindi 🔥
1.5M views
1 year ago


Created playlists
7
NOW PLAYING
Coding CheatSheets 🧾 by CodeWithHarry
Updated yesterday
VIEW FULL PLAYLIST
13
NOW PLAYING
Server Configuration, Deployment & VPS Tutorials For Beginners
VIEW FULL PLAYLIST
4
NOW PLAYING
amitshukla123456@gmail.com
Complete Roadmaps by Code With Harry
VIEW FULL PLAYLIST
113
NOW PLAYING
Java Tutorials For Beginners In Hindi
Updated yesterday
VIEW FULL PLAYLIST
7
rohanverma457245@gmail.com
NOW PLAYING
Projects Using HTML, CSS & JavaScript in Hindi
VIEW FULL PLAYLIST
17
NOW PLAYING
C Language Practice Programs
VIEW FULL PLAYLIST
nitinshukla4512452145@gmail.com
All Me :)
ProgrammingWithHarry
80.5K subscribers•75 videos
Programming With Harry is a place where you can learn various concepts related to programming for free. ProgrammingWithHarry is a beginner friendly place for you to start with your coding journey. I will hold your hands and walk you through various concepts of programming in a very friendly manner. Make sure you subscribe to this channel for free programming tutorials

"""
a = 0

email = re.findall(r"\w+@\S+\w", mystr)
print(email)
with open("Email_collector.txt", "a") as f:
        for item in email:
            a += 1
            f.write(f"Email {a} :     {item}  \n")


