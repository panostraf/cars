This is a crawler to scrap from a website all the details about cars

It requires to enter the links to crawl and it will follow. (this has to be added at the car_spider.py)
At the settings.py it is set to delay 0-5seconds between each request, and not allow multiple requests in order to protect the website




cd into the directory of the project and run:
scrapy crawl car_spider -o <name>.csv
