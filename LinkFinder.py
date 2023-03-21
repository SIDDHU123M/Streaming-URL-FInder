import os

required_modules = ["beautifulsoup4" , "re" , "requests"]
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"{module} not found. Installing now...")
        os.system(f"pip install {module}")
        __import__(module)

import re, requests
from bs4 import BeautifulSoup

url = input("Enter URL to Scrape : ")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

iframes = soup.find_all("iframe")
videos = soup.find_all("video")

video_urls = []
for iframe in iframes:
    src = iframe.get("src")
    if src:
        match = re.search(r"^(?:https?:)?//.+?\.(mp4|webm|ogg|ogv)", src)
        if match:
            video_urls.append(match.group(0))
for video in videos:
    src = video.get("src")
    if src:
        match = re.search(r"^(?:https?:)?//.+?\.(mp4|webm|ogg|ogv)", src)
        if match:
            video_urls.append(match.group(0))

for video_url in video_urls:
    print(video_url)
