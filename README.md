# NLP-twitterBias
## Introduction
This project is a first look into natural language processing and collecting/using big data. I got the insperation for this project by watching a talk on natural language processing in python, by Alice Zhoa. I thought I could take all the tools used to answer my own data science questions. The overal goal for this project is to learn all the tools and understand how the workflow works from collecting big data, organising that data, and analysing it to get meaningful information. 

## The Question
The questions I want answered though this exploration is How positive or negative is twitter? This question is to understand how people interact on twitter, is it a negative place is it more balanced.

## Collecting the data
  To collect all of the data I wanted to have as much of information as possible so that i'm not restricted later on in the project. To collect all this data I had to user the twitter API and a python library to connect to the API, for this I used tweepy. The first hurdle that I had to get though was what users did I want to collect the data from, for this I thought about collecting all the people that I follow and collecting all the people they follow, I could go as many layers as I wanted to for this, theoreticly collecting all twitter accounts. The next problem is twitters rate limiting, you can only send 200 requests to the API every 15 minutes. this means that the code has to wait when this rate limit hits and carry on when finished.
  
After running the code storing all the data in one larger variable I ran into a memory overflow error, this was that the variable got too large for the memory. At first I was holding al the information in one variable and saving it out to a file at the end. This obvioulsy isnt the correct way to do this. Next idea was to collect each users tweets and save that to a file before moving onto another user overwrighting the variable. This means that the memory doesn't get filled up and can keep going to fill up the drive. This worked and I was able to collect 15GB worth of data.
  
### Organising the data
the tweets for each user has a lot of extra data that I didn't need for analysing the data. The first way to cut down on the data is to only collect the text of the tweets which cut the size down a lot.


## Representing the data
### Most common words
From the top 25 words used by all the accounts doesn't look very interesting, all the words seem to be either very nuteral and words youd expect to be the most common in the English language. This hopefully proves that the data gathered would be whats expected, mainly there are not anomalies. The only one that could be seen as a bit off would be 'gracias' being that it's another language. Not all the accounts would have been English speakers however so this is also understandable.

![commonWords](/images/commonWords.png)

### Most used accounts
Looking at this graph it is very clear to see that very few accounts will have a lot of influence on any of the information gathered from this data as they will have more words. This could present a problem due to the fact the goal was to find a representation from many accounts from twitter. However, it may not be too bad as there are still many account above 750 words each.

Another thought is that the accounts with less words for all thier tweets are more likely to be bot accounts on twitter which could make some of the information useless, so getting rid of all the accounts under 500 may help stop this from happening.

![usedAccounts](/images/mostUsedAccounts.png)

### Most common words for top account
after analysing the most used words for the top few accounts I think it is clear that the data gathered is not large enough to give a significant view of how people comunicate on twitter. The account with the highest words only had a highest common word used at most 4 times. Either the cleaning of data has not been sucessful and words have been muddled up in the process or that data gathered is not enough. 

![CommonWordsTopAccount](/images/commonWordsTopAccount.png)

## Conclusion
To conclude the project to answer how positive or negative twitter is more data collection would be needed over a wider range of popular accounts, the ones that have the most impact on twitter. The data that has been collected doesn't include this type of information after going through to represent that data that was collected. The problem is that there are not enough accounts that have a high enough word count to produce meaning full results in the analysis of the data. Another issue could be due to unsuccesfull cleaning of the data, This is very likely a big factor and would need to be worked on a lot more if being done again.