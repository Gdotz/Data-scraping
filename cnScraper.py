from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get("https://wearecodenation.com/2024/01/23/data-course-playground/").text
# URL of the website to scrape .text to add only the HTML code.

#response = requests.get(html_text)
#Make a GET request
soup = BeautifulSoup(html_text, "lxml")
# HTML content of the website
#print (soup)

h5s = soup.find_all("h5", class_="elementor-heading-title elementor-size default")
# Find all the titles and dates on the website.

course_dates = {}

for h5Tag in h5s:
    if ":" in h5Tag.text:
        print(h5Tag.text)
        course_dates[h5Tag.text] = []
        dates = h5Tag.find_next("h6")
        for single_date in dates.strings:
            print (single_date)
            course_dates[h5Tag.text].append(single_date)

#print (course_dates)

# ACTIVITY 2

#mySeries = pd.Series([""])
#auto fills in null content

updated_dates = { key: pd.Series(value) for key, value in course_dates.items() }

df = pd.DataFrame(updated_dates)

print(df)
# to match dates with the courses
# #<h6> "date" <br> "date" </h6> this is how it will be shown in the terminal.
#       for single_date in h6_match.strings:
#           print(single_date)

#h6s = soup.find_all("h6")

#months = [
#    "January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "December"
#]

#course_dates = []

#for h6Tags in h6s:
#    if any(month in h6Tags.text for month in months):
#        course_dates.append(h6Tags.text)

#print (course_dates)

