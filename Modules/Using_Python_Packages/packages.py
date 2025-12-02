"""
Introduction to BeautifulSoup
Beautiful soup is a web scraping tool. It can parse HTML formatted text data, and allows the user
navigate through the HTML tree easily. You can search for elements by tag, class, or other features.
It can strip the tags and other HTML markup to leave you with just the data you want.

The most recent iteration is BS4.


Advantages: It's significantly easier to navigate complex HTML trees using this software, and it's ability
to strip HTML markup is very helpful.

Disadvantages: It cannot navigate the web on its own. You need additional libraries (like requests)
to send/receive requests from the server. It also can't interact with the webpage. Javascript isn't execute
with the requests/bs4 workflow either, so if there is any dynamically generated data after the HTML is loaded
BS4 won't have access to that. If you use software like Selenium which can be a headed or headless browser, you
have a much more robust ability to scrape webpages in an automated fashion.

Below is a sample scraping of wikipedia (allowed and legal use).
"""



import requests
from bs4 import BeautifulSoup
import time
import sys

headers = {"User-Agent": "WebScrapingExample/1.0 (Educational purpose;)"}
            # there are many other options here. depending on what you're scraping
            # you would add additional headers to get the website to give you want you wanted

url = "https://en.wikipedia.org/wiki/Web_scraping" #url to get

time.sleep(1)

#performs a request (GET,POST etc... here it's a GET request) to the URL using headers.
response = requests.get(url, headers=headers)

if response.status_code != 200: #makes sure the website actually responded with an okay.
    print(f"Failed to retrieve page: {response.status_code}")
    sys.exit(1) #exit the program with an error exit code 1

# you supply the text part of the response, or the HTML code. you tell BS4 that it should expect
# HTML with "html.parser" key argument.
soup = BeautifulSoup(response.text, "html.parser")


# this finds a tag "h1" with a class "firstHeading" and gets the values contained inside of it.
title = soup.find("h1", class_="firstHeading").get_text()
print(f"Title: {title}\n") #print the title

# this looks for a "div" tag with a class of
# "mw-parser-output" and then from the div finds all paragraph tags <p>
intro = soup.find("div", class_="mw-parser-output").find_all("p")
print("=== Introduction ===\n")

#let's print the first paragraph in the array of "intro"

print(intro[0].get_text().strip())
