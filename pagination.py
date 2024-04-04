from bs4 import BeautifulSoup
import requests
import pandas as pd

#This whole code needs to be in a loop.

#html_text = requests.get('http://books.toscrape.com/').text
# this is only the first page to the site.

html_text = requests.get('http://books.toscrape.com/catalogue/page-n.html').text
#Adding the page-n.html 

titles = soup.find_all("h3")

rating_to_int = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5,
}

title_collection = []
price_collection = []
rating_collection = []

for page_num in range (1, 51):
    html_text = requests.get(f'http://books.toscrape.com/catalogue/page-{page_num}.html').text
    soup = BeautifulSoup(html_text, 'lxml')
    titles = soup.find_all('h3')
# press tab to move all highlighted.
    for book_title in titles:
        print("Title : ", book_title.find('a').get('title').strip())
        title_collection.append(book_title.find('a').get('title').strip())
        # this grabs all the titles.
        price = book_title.find_next('p', class_="price_color")
        #this grabs all the prices.
        print("Price: ", price.text.strip('Â'))
        #It auto will put the A before a special character so we need to remove it.
        price_collection.append(float(price.text.strip('Â£')))
        #This changes it from a sting to intager.
        rating = book_title.find_previous('p', class_='star-rating').get('class')[1]
        print(rating_to_int.get(rating))
        rating_collection.append(rating_to_int.get(rating))
    #this whole code only prints out a page at a time, we need to add info for all the 50 other pages.

df = pd.DataFrame({
    "Title" : title_collection,
    "Price": price_collection,
    "Rating / 5" : rating_collection
})

#print(df)

df.to_excel("Books.xlsx", index=False)
# generates spreadsheet.

#for i in range (1, 51):
    #it has to be to 51 as it counts up to the one below eg.50
 #   print (f"You are looking at page {i}")

 ## ACTIVITY 2

df = pd.read_excel("Books.xlsx")

max_book_price = df["Price"].max()
#print (max_book_price)

four_star_books = df.query("`Rating / 5` == 4")
print ("Number of books rated 4 stars:")
print(four_star_books.shape[0])

mean_book_price = df["Price"].mean()
print(mean_book_price)

