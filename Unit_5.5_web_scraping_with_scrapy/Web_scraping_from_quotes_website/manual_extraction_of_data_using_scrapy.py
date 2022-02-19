
# coding: utf-8

# # scrapy crawl quotes

2022-02-18 18:59:15 [scrapy.utils.log] INFO: Scrapy 2.5.1 started (bot: example)
2022-02-18 18:59:16 [scrapy.utils.log] INFO: Versions: lxml 4.8.0.0, libxml2 2.9.12, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 22.1.0, Python 3.10.2 (tag
s/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)], pyOpenSSL 22.0.0 (OpenSSL 1.1.1m  14 Dec 2021), cryptography 36.0.1, Platform Windows-10-10.0
.19041-SP0
2022-02-18 18:59:16 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
2022-02-18 18:59:16 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'example',
 'NEWSPIDER_MODULE': 'example.spiders',
 'ROBOTSTXT_OBEY': True,
 'SPIDER_MODULES': ['example.spiders']}
2022-02-18 18:59:17 [scrapy.extensions.telnet] INFO: Telnet Password: 16db570b2ed81e73
2022-02-18 18:59:18 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.logstats.LogStats']
2022-02-18 18:59:22 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
 'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2022-02-18 18:59:22 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2022-02-18 18:59:22 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2022-02-18 18:59:22 [scrapy.core.engine] INFO: Spider opened
2022-02-18 18:59:26 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2022-02-18 18:59:26 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2022-02-18 18:59:26 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
2022-02-18 18:59:27 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
2022-02-18 18:59:27 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/2/> (referer: None)
2022-02-18 18:59:27 [quotes] DEBUG: Saved file quotes-1.html
2022-02-18 18:59:27 [quotes] DEBUG: Saved file quotes-2.html
2022-02-18 18:59:27 [scrapy.core.engine] INFO: Closing spider (finished)
2022-02-18 18:59:27 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 681,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2022, 2, 19, 2, 59, 26, 463530)}
2022-02-18 18:59:27 [scrapy.core.engine] INFO: Spider closed (finished)
   
   
# # scrapy shell command extracts data from the URL mentioned and generates the response object that points to the data extracted from the URL. It also opens the scrapy shell to wrangle the extracted data.   
# # scrapy shell "http://quotes.toscrape.com/page/1/"

# 2022-02-18 19:10:23 [scrapy.utils.log] INFO: Scrapy 2.5.1 started (bot: example)
# 2022-02-18 19:10:23 [scrapy.utils.log] INFO: Versions: lxml 4.8.0.0, libxml2 2.9.12, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 22.1.0, Python 3.10.2 (tag
# s/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)], pyOpenSSL 22.0.0 (OpenSSL 1.1.1m  14 Dec 2021), cryptography 36.0.1, Platform Windows-10-10.0
# .19041-SP0
# 2022-02-18 19:10:23 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.selectreactor.SelectReactor
# 2022-02-18 19:10:23 [scrapy.crawler] INFO: Overridden settings:
# {'BOT_NAME': 'example',
#  'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
#  'LOGSTATS_INTERVAL': 0,
#  'NEWSPIDER_MODULE': 'example.spiders',
#  'ROBOTSTXT_OBEY': True,
#  'SPIDER_MODULES': ['example.spiders']}
# 2022-02-18 19:10:23 [scrapy.extensions.telnet] INFO: Telnet Password: 4ca651a0c10e9f8b
# 2022-02-18 19:10:24 [scrapy.middleware] INFO: Enabled extensions:
# ['scrapy.extensions.corestats.CoreStats',
#  'scrapy.extensions.telnet.TelnetConsole']
# 2022-02-18 19:10:24 [scrapy.middleware] INFO: Enabled downloader middlewares:
# ['scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware',
#  'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
#  'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
#  'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
#  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
#  'scrapy.downloadermiddlewares.retry.RetryMiddleware',
#  'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
#  'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
#  'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
#  'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
#  'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
#  'scrapy.downloadermiddlewares.stats.DownloaderStats']
# 2022-02-18 19:10:24 [scrapy.middleware] INFO: Enabled spider middlewares:
# ['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
#  'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
#  'scrapy.spidermiddlewares.referer.RefererMiddleware',
#  'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
#  'scrapy.spidermiddlewares.depth.DepthMiddleware']
# 2022-02-18 19:10:24 [scrapy.middleware] INFO: Enabled item pipelines:
# []
# 2022-02-18 19:10:24 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
# 2022-02-18 19:10:24 [scrapy.core.engine] INFO: Spider opened
# 2022-02-18 19:10:25 [scrapy.core.engine] DEBUG: Crawled (404) <GET http://quotes.toscrape.com/robots.txt> (referer: None)
# 2022-02-18 19:10:25 [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
# [s] Available Scrapy objects:
# [s]   scrapy     scrapy module (contains scrapy.Request, scrapy.Selector, etc)
# [s]   crawler    <scrapy.crawler.Crawler object at 0x0000025951C166E0>
# [s]   item       {}
# [s]   request    <GET http://quotes.toscrape.com/page/1/>
# [s]   response   <200 http://quotes.toscrape.com/page/1/>
# [s]   settings   <scrapy.settings.Settings object at 0x0000025951C16BF0>
# [s]   spider     <DefaultSpider 'default' at 0x25951f10a30>
# [s] Useful shortcuts:
# [s]   fetch(url[, redirect=True]) Fetch URL and update local objects (by default, redirects are followed)
# [s]   fetch(req)                  Fetch a scrapy.Request and update local objects
# [s]   shelp()           Shell help (print this help)
# [s]   view(response)    View response in a browser
# 

# # response object and css method can be used to extract piece of information from the extracted data from URL.
# # The following commands are executed in scrapy shell 

# 
# # CMD1 - response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

# # CMD 2 is used to extract text from the title.
# # CMD 2 - response.css('title::text').getall()
['Quotes to Scrape']


# # Following commands are previous command variation

# # CMD 3 - response.css('title').getall()
['<title>Quotes to Scrape</title>']

# # CMD 4 - response.css('title::text').get() 
'Quotes to Scrape'

# # CMD 5 - response.css('title::text')[0].get()
'Quotes to Scrape'

# # Following commands use regular expressions to extract the piece of information from the extracted data
# # CMD 6 - response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']

# # CMD 7 - response.css('title::text').re(r'Q\w+')
['Quotes']

# # CMD 8 - response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']

# # XPATH can be used to extract piece of information from extracted data
# # CMD 9 - response.xpath('//title')
[<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]

# # CMD 10 - response.xpath('//title/text()').get()
'Quotes to Scrape'
