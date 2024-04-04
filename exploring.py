import pandas as pd

df = pd.read_csv("results.csv")

#print (df)
#This is to print out the CSV file but its not very helpful.
#print (df.info())
# .info() gives us useful information we might need, this prints out in columns and shows us how many values are not 'null'.

#print(df.describe())
#This shows descriptive statistics we can use.
# Gives us the mean, standard deviation, min and percentages.
#Mean is the average number of goals scored.
#std (standard deviation) tells us the average distance from a random data point to the mean.
#The range shows us how far the data is spread out, it only takes two values intpo account, the two extremes, we know nothing about the data inbetween. so with std we learn more about data inside its vairability it shows us the bulk of our info.
#median is middle value '50%'with 1 goal scored, and the max is 31 goals which would make it an outlier especially when 75% scored most 2.

#print(df["home_score"].value_counts(normalize=True)* 100)
#we can see after 6 goals, higher scores only make up 1%. 

mask = df["home_score"] > 6
#checking if everythin in column is greater than 6.
df = df[mask]
# the '~' flips the meaning of true and false will search below 6 without it, it will give us values above 6.
print(df)
#print(df["home_score"].mean())
# will find the mean between 1 and 6.


