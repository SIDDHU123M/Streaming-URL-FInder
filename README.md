# Streaming-URL-FInder
***This Python script uses BeautifulSoup to extract video URLs from a given webpage. It looks for iframe and video tags, extracts the video URLs using regular expressions, and prints them to the console. The script includes a user agent header to avoid 403 errors, and supports video formats such as MP4, WebM, OGG, and OGV. It is a useful tool for automating the process of finding video URLs on a webpage.***

## 🔗 Features
- The code is used for web scraping to extract video URLs from a given webpage.
- The user is prompted to enter the URL of the webpage to be scraped.
- The requests library is used to make a request to the specified URL with user agent headers to avoid 403 errors.
- BeautifulSoup is used to parse the HTML of the webpage.
- The script looks for all the iframe and video tags on the page using the find_all() method of BeautifulSoup.
- Regular expressions are used to extract the video URLs from the tags using the re module.
- The script then prints the extracted video URLs using a for loop.
