from bs4 import BeautifulSoup
import requests
import pandas as pd
# run file using python main.py

html_text = requests.get("https://www.scrapethissite.com/pages/simple/")

souped_html = BeautifulSoup(html_text.text, "lxml")

countries = souped_html.find_all("h3")

#print(countries)

#for country in countries:
    #print (country.text.strip())
    #This jus prints out the text of the contry name.
    #The .strip() cleans the white space ands lists items.

df = pd.DataFrame([country.text.strip() for country in countries])
#This puts all the data into a frame into the terminal.
#print (df)

country_capitals = souped_html.find_all("span", class_="country-capital")

#print (country_capitals)

#for capital in country_capitals:
#    print(capital.text)

########## Needs completing. #######
# country_pop = souped_html.find_all("span", class_="country-population")

# country_pop = {}

# for population in country_pop:
#     if ":" in h5Tag.text:
#         print(h5Tag.text)
#         course_dates[h5Tag.text] = []
#         dates = h5Tag.find_next("h6")
#         for single_date in dates.strings:
#             print (single_date)
#             course_dates[h5Tag.text].append(single_date)

# df = pd.DataFrame({
#     "Country" : country_capitals,
#     "Population": country_pop,
# })

# print(df)



# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# html_text = requests.get("https://www.scrapethissite.com/pages/simple/")

# souped_html = BeautifulSoup(html_text.text, "lxml")

# countries = souped_html.find_all("h3")

# country_capitals = souped_html.find_all("span", class_="country-capital")

# country_pop = souped_html.find_all("span", class_="country-population")

# for country in countries:
#     print(countries)
#     for capital in country_capitals:
#         print(country_capitals)
#         for population in country_pop:
#             print(country_pop)

# df = pd.DataFrame.strip()({
#     "County" : countries,
#     "Capital": country_capitals,
#     "Population" : country_pop
# })

# print(df)
