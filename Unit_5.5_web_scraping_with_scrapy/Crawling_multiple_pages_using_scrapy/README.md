1. The crawling_pages.py contains python code that imports scrapy package.
2. The python code calls the page-1 of the website quotes.toscrape.com and extracts Quote, Authir name and Tags.
3. The parse method is a callback method that extracts 'page-2' from the current page (page-1) and crawls to page 2 and extracts the same information.
4. The crawling process continues till the last page.

The quotes.json file contains all the information, Quote, Author name and Tags from all the pages of the website quotes.toscrape.com in a dictionary format.

# The following command generates the quotes.json 
scrapy crawl quotes -O quotes.json
