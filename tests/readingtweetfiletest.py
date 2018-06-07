"""This is a Program that computes the sentiment values of tweets and prints out
their values based on timezones in the USA"""
# Programmer: Anton Mihail Lachmaniucu
# Date: 2017-11-02

import time as t
# Declaration and setting of global variables
count = 0
# Sentiment Value of 1
lowSent = []
# Sentiment Value of 5
midSent = []
# Sentiment Value of 7
incSent = []
# Sentiment Value of 10
highSent = []


def main():
    # Opening main files
    keywordsFile = fileValid()
    assignKeyValues(keywordsFile)
    tweetsFile = fileValid()
    # Happiness score of tweets from each time-zone
    east, cent, mount, paci, eastAmt, centAmt, mountAmt, paciAmt = readtweetfile(tweetsFile)
    print("The average happiness value for the Eastern timezone from {} tweets, is {}".format(eastAmt,east/eastAmt))
    print("The average happiness value for the Central timezone from {} tweets, is {}".format(centAmt,cent/centAmt))
    print("The average happiness value for the Mountain timezone from {} tweets, is {}".format(mountAmt,mount/mountAmt))
    print("The average happiness value for the Pacific timezone from {} tweets, is {}".format(paciAmt, paci/paciAmt))
    # Gui window with the histogram that was provided in happy_histogram.py
    graphicsFun(east/eastAmt, cent/centAmt, mount/mountAmt, paci/paciAmt)
    # Leave the program running for an extra 10 seconds for console users
    t.sleep(10)


# Reads the tweet file and outputs the numbers of and values of tweets from each timezone
def readtweetfile(file):
    # Happiness score of tweets from each timezone
    east = 0
    cent = 0
    mount = 0
    paci = 0
    # Amount of tweets from each timezone
    eastAmt = 0
    centAmt = 0
    mountAmt = 0
    paciAmt = 0
    # Temporary Variable Denoting The Individual Tweet Sentiment
    tweetSent = 0
    line = file.readline()
    # Reads through file and splits it appropriately
    while line != "":
        coordinatesI, coordinatesX, restOfLine = line.split(" ", maxsplit=2)
        coordinatesI = coordinatesI.strip("[")
        coordinatesX = coordinatesX.strip("]")
        coordinates = [coordinatesI.strip(","), coordinatesX]
        timezone = verfyTimezones(coordinates)
        restOfLine = restOfLine.lower()
        burn1, burn2 , burn3 ,restOfLine = restOfLine.split(" ", maxsplit=3)
        restOfLine = cleanLine(restOfLine)
        #print(restOfLine)
        restOfLine = list(restOfLine.split(" "))
        if timezone == "Eastern":
            tweetSent = tweetSentiment(restOfLine)
            if tweetSent > 0:
                east = east + tweetSent
                eastAmt += 1
        elif timezone == "Central":
            tweetSent = tweetSentiment(restOfLine)
            if tweetSent > 0:
                cent = cent + tweetSent
                centAmt += 1
        elif timezone == "Mountain":
            tweetSent = tweetSentiment(restOfLine)
            if tweetSent > 0:
                mount = mount + tweetSent
                mountAmt +=1
        elif timezone == "Pacific":
            tweetSent = tweetSentiment(restOfLine)
            if tweetSent > 0:
                paci = paci + tweetSent
                paciAmt += 1
        line = file.readline()
    file.close()
    return east, cent, mount, paci, eastAmt, centAmt, mountAmt, paciAmt


# Determines the tweet sentiment of each tweet
def tweetSentiment(tweetLine):
    global lowSent, midSent, incSent, highSent
    tweetSent = 0
    for i in tweetLine:
        if i in lowSent:
            tweetSent += 1
        elif i in midSent:
            tweetSent += 5
        elif i in incSent:
            tweetSent += 7
        elif i in highSent:
            tweetSent += 10
        else:
            pass
    return tweetSent


# Assigns the words from each value category to their own lists
def assignKeyValues(file):
    global lowSent, midSent, incSent, highSent
    for line in file:
        word, sentiment = line.split(",")
        sentiment = int(sentiment)
        if sentiment == 1:
            lowSent.append(word)
        elif sentiment == 5:
            midSent.append(word)
        elif sentiment == 7:
            incSent.append(word)
        elif sentiment == 10:
            highSent.append(word)
    file.close()


# Checks where the coordinates place the tweets relative to given timezones
def verfyTimezones(coordinates):
    timezone = ""
    if 24.660845 <= float(coordinates[0]) <= 49.189787:
        if -87.518395 <= float(coordinates[1]) <= -67.444574:
            timezone = "Eastern"
        elif -101.998892 <= float(coordinates[1]) < -87.518395:
            timezone = "Central"
        elif -115.236428 <= float(coordinates[1]) < -101.998892:
            timezone = "Mountain"
        elif -125.242264 <= float(coordinates[1]) < -115.236428:
            timezone = "Pacific"
    return timezone


# Validate the existence of the file name taken from import, raise exception accordingly
def fileValid():
    global count
    count += 1
    fileType = ""
    if count == 1:
        fileType = "Keywords"
    elif count > 1:
        fileType = "Tweets"
    try:
        filename = input("Please enter the filename for the file containing the {}: ".format(fileType))
        file = open(filename, "r",encoding="utf-8")
    except Exception as e:
        raise FileNotFoundError('File Not Found.')
    return file


# Remove all numbers and special characters from the tweet string
def cleanLine(line):
    line = list(line)
    i = len(line)
    for x in range(i ,1, -1):
        if line[x] != " " and not line[x].isalnum():
            line.remove(line[x])
        if line[x] != " " and line[x].isnumeric():
            line.remove(line[x])
    line = "".join(line)
    return line


# Draw the histogram that contains the average happiness values of the timezones
def graphicsFun(east, cent, mount, paci):
    import happy_histogram as hp
    hp.drawSimpleHistogram(east, cent, mount, paci)


main()
