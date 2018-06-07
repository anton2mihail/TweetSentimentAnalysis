"""This is a Program that computes the sentiment values of tweets and prints out
their values based on timezones in the USA"""
# Programmer: Anton Mihail Lachmaniucu
# Date: 2017-11-02
import time as t
# Declaration and setting of global variables
count = 0
# Sentiment Value of 1
lowSent = set()
# Sentiment Value of 5
midSent = set()
# Sentiment Value of 7
incSent = set()
# Sentiment Value of 10
highSent = set()


def main():
    # Opening main files
    KEYWORDSFILE = fileValid()
    assignKeyValues(KEYWORDSFILE)
    TWEETSFILE = fileValid()
    # Happiness score of tweets from each time-zone
    amounts = readtweetfile(TWEETSFILE)
    if amounts[4] > 0:
        print("The average happiness value for the Eastern timezone from {} tweets, is {}".format(amounts[4],amounts[0]/amounts[4]))
    else:
        print("There were no tweets for the Eastern timezone.")
    if amounts[5] > 0:
        print("The average happiness value for the Central timezone from {} tweets, is {}".format(amounts[5],amounts[1]/amounts[5]))
    else:
        print("There were no tweets for the Central timezone.")
    if amounts[6] > 0:
        print("The average happiness value for the Mountain timezone from {} tweets, is {}".format(amounts[6],amounts[2]/amounts[6]))
    else:
        print("There were no tweets from the Mountain timesone.")
    if amounts[7] > 0:
        print("The average happiness value for the Pacific timezone from {} tweets, is {}".format(amounts[7], amounts[3]/amounts[7]))
    else:
        print("There were no tweets from the Pacific timezone.")
    # Gui window with the histogram that was provided in happy_histogram.py
    graphicsFun(amounts[0]/(amounts[4] if amounts[4] > 0 else 1), amounts[1]/(amounts[5] if amounts[5] > 0 else 1), amounts[2]/(amounts[6] if amounts[6] > 0 else 1), amounts[3]/(amounts[7] if amounts[7] > 0 else 1))
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
    line = file.readline()
    # Reads through file and splits it appropriately
    while line != "":
        coordinatesI, coordinatesX, restOfLine = line.split(" ", maxsplit=2)
        coordinatesI = coordinatesI.strip("[")
        coordinatesX = coordinatesX.strip("]")
        coordinates = [coordinatesI.strip(","), coordinatesX]
        restOfLine = restOfLine.lower()
        burn1, burn2, burn3, restOfLine = restOfLine.split(" ", maxsplit=3)
        restOfLine = cleanLine(restOfLine)
        restOfLine = cleanLine(restOfLine)
        restOfLine = list(restOfLine.split(" "))
        timezone = verfyTimezones(coordinates)
        if timezone == "Central":
            tweetSent = tweetSentiment(restOfLine)
            if tweetSent > 0:
                cent += tweetSent
                centAmt += 1
            tweetSent -= tweetSent
        elif timezone == "Eastern":
            tweetSent = tweetSentiment(restOfLine)
            if tweetSent > 0:
                east += tweetSent
                eastAmt += 1
            tweetSent -= tweetSent
        elif timezone == "Mountain":
            tweetSent = tweetSentiment(restOfLine)
            if tweetSent > 0:
                mount += tweetSent
                mountAmt += 1
            tweetSent -= tweetSent
        elif timezone == "Pacific":
            tweetSent = tweetSentiment(restOfLine)
            if tweetSent > 0:
                paci += tweetSent
                paciAmt += 1
            tweetSent -= tweetSent
        line = file.readline()
    file.close()
    return [east, cent, mount, paci, eastAmt, centAmt, mountAmt, paciAmt]


# Determines the tweet sentiment of each tweet
def tweetSentiment(tweetLine):
    global lowSent, midSent, incSent, highSent
    tweetSent = 0
    count = 0
    for i in tweetLine:
        if i in lowSent:
            count += 1
            tweetSent += 1
        elif i in midSent:
            count += 1
            tweetSent += 5
        elif i in incSent:
            count += 1
            tweetSent += 7
        elif i in highSent:
            count += 1
            tweetSent += 10
        else:
            continue
    return tweetSent/(count if count > 0 else 1)


# Assigns the words from each value category to their own lists
def assignKeyValues(file):
    global lowSent, midSent, incSent, highSent
    for line in file:
        word, sentiment = line.split(",")
        sentiment = int(sentiment)
        if sentiment == 1:
            lowSent.add(word)
        elif sentiment == 5:
            midSent.add(word)
        elif sentiment == 7:
            incSent.add(word)
        elif sentiment == 10:
            highSent.add(word)
    file.close()


# Checks where the coordinates place the tweets relative to given timezones
def verfyTimezones(coordinates):
    timezone = ""
    if 24.660845 <= float(coordinates[0]) <= 49.189787:
        if -125.242264 <= float(coordinates[1]) <= -115.236428:
            timezone = "Pacific"
        elif -115.236428 < float(coordinates[1]) <= -101.998892:
            timezone = "Mountain"
        elif -101.998892 < float(coordinates[1]) <= -87.518395:
            timezone = "Central"
        elif -87.518395 < float(coordinates[1]) <= -67.444574:
            timezone = "Eastern"
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
        FILENAME = input("Please enter the FILENAME for the file containing the {}: ".format(fileType))
        file = open(FILENAME, "r", encoding="utf-8")
    except Exception as e:
        raise FileNotFoundError('File Not Found.')
    return file


# Remove all numbers and special characters from the tweet string
def cleanLine(line):
    line = list(line)
    line = ["" if x != " " and not x.isalnum() else x for x in line]
    line = "".join(line)
    return line


# Draw the histogram that contains the average happiness values of the timezones
def graphicsFun(east, cent, mount, paci):
    import happy_histogram as hp
    hp.drawSimpleHistogram(east, cent, mount, paci)


main()
