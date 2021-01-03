# Web Scraping using Python

There are three Jupyter Notebooks (as of now). And they are:
1. GoogleWebScrape.ipynb - Here, the result will return first page of the Google search result of whatever input query you put. For example, I have put "J. Cole" as the query input. You can put anything and see for yourself. The result will return the title and the link of the Google search result. 
2. NBAWebScrape.ipynb - Here, the input url is the [Basketball Reference](https://www.basketball-reference.com/playoffs/). Using BeautifulSoup we will scrape the data from the site and save the data into a CSV file, called NBAFinalsChampions.csv. Run the Jupyter Notebook and the output of it will be the CSV file, NBAFinalsChampions.csv. 
3. AmazonBooksWebScrape.ipynb - Here, the input url is [Amazon Books Bestseller](https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1). If you cannot access the Amazon Books Bestseller link, this is the [Parent Link](https://www.amazon.com/gp/bestsellers/books/) (You will for sure be able to access the parent link). I would recommend you to access the parent link. Click on the parent link, then go to the bottom page with the page numbers. After this, click on page 1 and then take the URL. Before scraping the data, inspect the page as shown below. 


![](Screenshots_Ignore/AmazonBooksSS1.png) 
