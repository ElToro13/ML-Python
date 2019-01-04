# Analysis of prevailing Sentiment in Diabetes Community using Twitter
### Introduction
Since the boom of internet, it has become easier to share our thoughts and feelings regarding any topics with others. Internet has gone from a luxury to fourth essential element of life after water, land and air! Twitter is a social media platform, where users can share their ideas by sending a short message which is known as a "Tweet". Its a place on internet where people just talk about almost any topic happening any part of the world and share their opinions with other. In case of any International or domestic incidnet, Twitter helps set a narrative as how are the people in community feeling about it. Not only Twitter is an excellent tool for just common people, it also helps developers analysis those tweets to make sense of what is going on in the community. There are many libraries out there that helps developers collect tweets from users using a particular Hastags and perform many characteristic analysis from it. 

In this project, A Python based Library - *Tweepy* is used. Here, Sentiment Analysis is down on tweets based on two hashtags *#gbdoc* and  *#doc* in the last seven days. Any tweet that users have posted with those hashtags were scarped from twitter and stored in an CSV file from where further analysis were carried out. To perform Analysis, a simplified text processing library *TextBlob* was used. 

Entire code is written in Python using Jupyter Notebook. 

## Data Collection
Using Tweepy, tweets from date 26/12/2018 uptill 2/1/2019 were collected. **Date and Time of creation of tweet** and **source as from which platorm the user is tweeting** was also collected. All this data was stored in a CSV file. 

## Analysis
Once we have the csv file, we used pandas library, TextBlob, numpy and matplotlib to analysis and display the results. 
Following results were analyzed and plotted.
* Which is the most preferred platform for users
* Frequently occuring words in the tweets. Results were shown using wordcloud
* Sentiment Analysis - Polarity and Subjectivity of the tweet using Textblob
* Preferred time of day to tweet.

## Libraries Used

* Tweepy
* Pandas
* Numpy
* Matplotlib
* TextBlob
* Re
* WordCloud

## Author

* **Yash Soni**
