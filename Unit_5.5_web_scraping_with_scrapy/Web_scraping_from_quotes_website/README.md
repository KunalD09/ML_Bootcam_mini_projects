# Code Description

  1. The file "manual_extraction_of_data_using_scrapy.py" file contains the commands used for scraping data from the website quotes.toscrape.com using scrapy package.
  2. It contains the commands such as response.css() to extract some piece of information from the entire HTML text.
  3. The file "quotes_spider.py" file contains the python code to extract the Quote, Author name and tags by specifying multiple URL's

The quotes.json file contains all the information in a python dictionary format, i.e. Quote, Author name and Tags from all the URL's specified in the code.

# The following command generates quotes.json file
scrapy crawl quotes -O quotes.json

