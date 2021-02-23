#importing the used libraris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob #to be able to analyse the sentiment
from wordcloud import WordCloud,STOPWORDS #to generate the wordcloud

#Reading the Data
comments = pd.read_csv('GBcomments.csv', error_bad_lines=False)
comments.head() # to have a preview on the data

#Preforming analysis on a specific comment from the data
TextBlob("It's more accurate to call it the M+ (1000) be..").sentiment.polarity

comments.isna().sum()#to get the messing values which tells us that there are 28 rows within comment_text that dont have a value

#Imputating the data frame (Removing the NaN values)
comments.dropna(inplace=True)

#now to preform the Analysis on all the comment in the dataframe
polarity=[]
for i in comments['comment_text']:
    polarity.append(TextBlob(i).sentiment.polarity)
#print(polarity)

#Adding it to the data Frame under the new column Polarity
comments["Polarity"] = polarity

#Viewing the dataframe
comments.head(20)

#Filtering the data frame by takint the postive comments
comments_positive=comments[comments["Polarity"] == 1]
comments_positive.head()

stopwords=set(STOPWORDS)#this basically creates a list of words to ignore in the wordcloud (already has some words in it and new ones could be add using stopwords.add("word"))
total_comment = " ".join(comments_positive["comment_text"]) # This will turn our comment_text values in the data frame to a string to deal with using wordcloud lib
wordcloud = WordCloud(width=1000,height=500,stopwords=stopwords).generate(total_comment) #defining our wordcloud while adding the total_comment into it

#visualizing the wordcloud (The bigger the word size is the higher its priority)
plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis("off")

#filtering for the negative ones
comments_negative=comments[comments["Polarity"] == -1]
comments_negative.head()
total_comment= " ".join(comments_negative["comment_text"])

#generating the wordcloud
wordcloud = WordCloud(width=1000,height=500,stopwords=stopwords).generate(total_comment)

#visualizing the wordcloud (The bigger the word size is the higher its priority)
plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis("off")
