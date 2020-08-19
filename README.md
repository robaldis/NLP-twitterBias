# NLP-twitterBias
## Introduction
This project is a first look into natural language processing and collecting/using big data. I got the insperation for this project by watching a talk on natural language processing in python, by Alice Zhoa. I thought I could take all the tools used to answer my own data science questions. The overal goal for this project is to learn all the tools and understand how the workflow works from collecting big data, organising that data, and analysing it to get meaningful information. 

## The Question
The questions I want answered though this exploration is How positive or negative is twitter? This question is to understand how people interact on twitter, is it a negative place is it more balanced.

## Collecting the data
  To collect all of the data I wanted to have as much of information as possible so that i'm not restricted later on in the project. To collect all this data I had to user the twitter API and a python library to connect to the API, for this I used tweepy. The first hurdle that I had to get though was what users did I want to collect the data from, for this I thought about collecting all the people that I follow and collecting all the people they follow, I could go as many layers as I wanted to for this, theoreticly collecting all twitter accounts. The next problem is twitters rate limiting, you can only send 200 requests to the API every 15 minutes. this means that the code has to wait when this rate limit hits and carry on when finished.
  
After running the code storing all the data in one larger variable I ran into a memory overflow error, this was that the variable got too large for the memory. At first I was holding al the information in one variable and saving it out to a file at the end. This obvioulsy isnt the correct way to do this. Next idea was to collect each users tweets and save that to a file before moving onto another user overwrighting the variable. This means that the memory doesn't get filled up and can keep going to fill up the drive. This worked and I was able to collect 15GB worth of data.
  
### Organising the data
the tweets for each user has a lot of extra data that I didn't need for analyzing the data. The first way to cut down on the data is to only collect the text of the tweets which cut the size down a lot.
