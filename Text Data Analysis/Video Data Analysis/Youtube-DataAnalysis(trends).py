#importing the used libraris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re #for cleaning the strings
from wordcloud import WordCloud,STOPWORDS #to make the wordcloud

#importing the data
video = pd.read_csv('USvideos.csv', error_bad_lines=False)
video.head()

#filtering the df
video["tags"]
tags_complete = " ".join(video["tags"]) #truning the data in a string

#but since the string still needs some cleaning we do the following
tags = re.sub("[^a-zA-Z]", " ",tags_complete) #replace everything with a space apart from alphabet.
tags = re.sub(" +", " ",tags_complete)

#since our string as all clean and ready now we create our word cloud
wordcloud= WordCloud(width=1000,height=500,stopwords=set(STOPWORDS)).generate(tags)

#Analying and visualizing the data using the likes, views and Dislikes as a base (remove the "#" when compiling)
#sns.regplot(data=video,x="views",y="likes")
#plt.title("Regression plot for vies and likes")

#sns.regplot(data=video,x="views",y="dislikes")
#plt.title("Regression plot for vies and dislikes")

#finding the correlation of views, likes and dislikes
df_corr=video[["views","likes","dislikes"]]
print(df_corr.corr()) #to see the correlation values
sns.heatmap(df_corr.corr(),annot=True)#to visualize the values using a heatmap

#Visualizing the Word cloud
plt.figure(figsize=(15,5))
plt.imshow(wordcloud)
plt.axis("off")
