
# coding: utf-8

# # above command is to open scrapy shell that contains response object pointing to the data in the URL

# # scrapy shell 'http://quotes.toscrape.com'

# # The following commands are used to extract Author name, quote and tags 

# # quote = response.css("div.quote")[0]
# # text = quote.css("span.text::text").get()
# # text
'“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
# # author = quote.css("small.author::text").get()
# # author
# 
'Albert Einstein'
# # tags = quote.css("div.tags a.tag::text").getall()
# # tags
['change', 'deep-thoughts', 'thinking', 'world']
# # for quote in response.css("div.quote"):
# # ...     text = quote.css("span.text::text").get()
# # ...     author = quote.css("small.author::text").get()
# # ...     tags = quote.css("div.tags a.tag::text").getall()
# # ...     print(dict(text=text, author=author, tags=tags))
# 
# 
{'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'author': 'Albert Einstein', 'tags':
 ['change', 'deep-thoughts', 'thinking', 'world']}
{'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'author': 'J.K. Rowling', 'tags': ['abilities', 'choices']}       
{'text': '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'author': 'Albert Ei
nstein', 'tags': ['inspirational', 'life', 'live', 'miracle', 'miracles']}
{'text': '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'author': 'Jane Austen', 'tags': ['aliteracy', 
'books', 'classic', 'humor']}
{'text': "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", 'author': 'Marilyn Monroe', 'tags': ['be
-yourself', 'inspirational']}
{'text': '“Try not to become a man of success. Rather become a man of value.”', 'author': 'Albert Einstein', 'tags': ['adulthood', 'success', 'value']}
{'text': '“It is better to be hated for what you are than to be loved for what you are not.”', 'author': 'André Gide', 'tags': ['life', 'love']}
{'text': "“I have not failed. I've just found 10,000 ways that won't work.”", 'author': 'Thomas A. Edison', 'tags': ['edison', 'failure', 'inspirational', 'paraphra
sed']}
{'text': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'author': 'Eleanor Roosevelt', 'tags': ['misattributed-eleanor-roo
sevelt']}
{'text': '“A day without sunshine is like, you know, night.”', 'author': 'Steve Martin', 'tags': ['humor', 'obvious', 'simile']}