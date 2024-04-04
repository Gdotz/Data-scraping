import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")

#print(df.describe())
#this if for the avg values.
# brackets mean its a function.

df = df.set_index("Transaction ID")
#Changes name of the index.
df = df.drop(columns=("Till ID"))
#This is to remove a column or columns by name.
df = df.drop([16,17,18])
#             ^^^^^^^^ These rows will be removed which is default to remove NaN values.
##df = df.reset_index(drop=True)
# This cleans up the index after changes have been made.
df = df.drop_duplicates()
# Self explanitory it removes all duplicates only works if you change the name of the index to make two values the same.


df.at[12,"Amount"] = 3.10
# This will change the value from 31 to 3.10

def float_to_time(stamp):
    #             ^^^^^ time stamp
    stamp = str(stamp)
    #convert the number into a string.
    stamp = stamp.replace(".", ":")
    #Replace decimal.
    stamp = "0" + stamp
    #conctanates the string.
    if len(stamp) != 5:
        stamp = stamp + "0"
        #Adding the 0 to the end of the stamp.
    return stamp 

#Now we add it to all out values 
df["Time"] = df["Time"].apply(float_to_time)
#                            ^^^^ Return function
#If there are double 0's then some numbers may not appear in full, we need to fix that, adding the if statement to the def fixed it.
df["Time"] = pd.to_datetime(df["Time"])
#Updates them to actual dates and time.
#print (df["Time"])
#print out the time value of every column.

################## Activity 1 #################

print ("\nAverage price of item")
sum_amount = df["Amount"].sum()
#                         ^^^^ sums up every value from column.
sum_items = df["Items"].sum()

average_item_price = sum_amount/sum_items
print (average_item_price)
#print(df.describe()["Amount"])

################# ACTIVITY 2 ################

#print (df)
# Check columns.

print ("\nAverage basket price")
df["Amount"].mean()
average_basket = sum_amount/len(df)
print (average_basket)


################# ACTIVITY 3 ###############

print ("\nMax spend")
print (df["Amount"].max())

print ("\nMin spend")
print (df["Amount"].min())

################# ACTIVITY 4 ###################

print ("\nMost common spend amount")
print (df["Amount"].mode())

################# ACTIVITY 5 ##################

print ("\nMost common payment type")
print (df["Currency"].mode()[0])





