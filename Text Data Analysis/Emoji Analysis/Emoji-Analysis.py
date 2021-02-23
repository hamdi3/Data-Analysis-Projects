#It's important to know first how emoji work in python
#Every emoji has a Unicode associated with it
# grinning squinting face for example print("\U0001F606") 

#importing the used libraris
import pandas as pd
import emoji #to be able to deal with emojis
import plotly.graph_objects as go 
from plotly.offline import iplot

#importing data
comments = pd.read_csv('GBcomments.csv', error_bad_lines=False)

#Cleaning the df
comments.dropna(inplace=True)

#Filtering the emojis in a specific comment
#comment = comments["comment_text"][1]#getting the comment with emojis
#[i for i in comment if i in emoji.UNICODE_EMOJI] #to get the emoji in a comment for example

#Filtering all the comments
str = ""
for i in comments["comment_text"]:
    list = [c for c in i if c in emoji.UNICODE_EMOJI]
    for ele in list: # this basically turns the list into a string
        str = str + ele 
#print(str) just making sure we got the right results

#now to create a dic of the emojis and how many times they were repeated
results = {}
for i in set(str): #used a set so that mojis wont be repeated (uniqe) in the dic
    results[i] = str.count(i)
#print(results) to check the results

final = {}
for key , value in sorted(results.items(),key= lambda item:item[1]): #the result.items is the get the results in form of a 2 elem tuples and the we use sorted to sort it using the key
    final[key] = value
keys = [*final.keys()] 
#print(keys) to make sure it was right
values = [*final.values()]
#print(values) same thing 

#making a dataframe out of the information we got so far
df = pd.DataFrame({"chars": keys[-20:],"num":values[-20:]}) # to get the last 20 emojis

#now to visualize the informations
trace=go.Bar(x=df["chars"], y=df["num"])
iplot([trace])
