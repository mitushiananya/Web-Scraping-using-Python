import urllib
import requests
from bs4 import BeautifulSoup

# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

query = "data science"
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"

headers = {"user-agent": USER_AGENT}
resp = requests.get(URL, headers=headers)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []
    for g in soup.find_all('div', class_='g'):
        # anchor div
        rc = g.find('div', class_='rc')
        # description div
        s = g.find('div', class_='s')
        if rc:
            divs = rc.find_all('div', recursive=False)
            if len(divs) >= 2:
                anchor = divs[0].find('a')
                link = anchor['href']
                title = anchor.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                results.append(item)
    print(results)
