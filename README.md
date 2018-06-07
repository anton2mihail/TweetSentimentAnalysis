# TweetSentimentAnalysis

This is a python program that batch processes tweets based on arbitrary sentiment criteria, and outputs the sentiment values for the tweets as aggregates over a us timezone. This is because the tweet information required includes longitude and latitude coordinates, and the program was only used for tweets within a us timezone.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Things you will need to start using the program 
 
```
Python3.6
tweets.txt
keywords.txt
```
_You can go to www.python.org for instructions on installing the python3.6 interpreter._
To check if you have python installed type into your command line
```
python
```
and something like the following should appear
```
Python 3.6.3 |Anaconda, Inc.| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
The _tweets_ file cotains space seperated information about the tweets, including the longitude and latitude coordinates, the date and time of the creation of the tweet, and the tweet text.<br/>
The _keywords_ file contains the keywords the program should be looking for as well as their sentiment values. As these are completely arbitrary feel free to change them to your specifications.
 
### Using

The best way to use the program is through IDLE or something like PyCharm but it can also be run from the command line

Open your program of choice. Be it IDLE or simply using the <b>command line.</b>
Type the following into your command line
```
cd /The-Directory-where-the-file-is/TweetSentimentAnalysis
```

And then run the program with python, like so

```
python sentimentAnalysis.py
```
and then the program will prompt you to enter the names of the two text files required (tweets.txt, keywords.txt).<br/>
Afterwards the program will output the sentiment analysis by timezone, and there will appear a window in the background containing a graphical representaion of the sentiment analysis.

