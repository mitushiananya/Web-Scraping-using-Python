import pandas as pd
from bs4 import BeautifulSoup
import requests

no_pages = 2  # There are total 2 pages of the bestseller books (That's 100 books)

def get_data(pageNo):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    r = requests.get('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_'+str(pageNo)+'?_encoding=UTF8&pg='+str(pageNo), headers=headers)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content, "html.parser")

    alls = []
    for d in soup.findAll('div', attrs={'class':'a-section a-spacing-none aok-relative'}):
        name = d.find('span', attrs={'class':'zg-text-center-align'})  # Name of the book
        n = name.find_all('img', alt=True)   # Image of the book
        author = d.find('a', attrs={'class':'a-size-small a-link-child'})  # Name of the author of the book
        rating = d.find('span', attrs={'class':'a-icon-alt'})  # Rating of the book
        users_rated = d.find('a', attrs={'class':'a-size-small a-link-normal'})  # Number of customers that rated the book
        price = d.find('span', attrs={'class':'p13n-sc-price'})  # Price of the book
        all1 = []

        if name is not None:
            all1.append(n[0]['alt'])
        else:
            all1.append("unknown-product")

        if author is not None:
            all1.append(author.text)
        elif author is None:
            author = d.find('span', attrs={'class':'a-size-small a-color-base'})
            if author is not None:
                all1.append(author.text)
            else:
                all1.append('0')

        if rating is not None:
            all1.append(rating.text)
        else:
            all1.append('-1')

        if users_rated is not None:
            all1.append(users_rated.text)
        else:
            all1.append('0')

        if price is not None:
            all1.append(price.text)
        else:
            all1.append('0')
        alls.append(all1)
    return alls

results = []

for i in range(1, no_pages+1):
    results.append(get_data(i))

flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Book Name','Author','Rating','Customers_Rated', 'Price'])
df.to_csv('amazonbooks.csv', index=False, encoding='utf-8')  # Saving the data to a CSV file
print("Shape of the data: ",df.shape)
print("\nFirst 5 rows of the scraped data:")
print(df.head(5))

