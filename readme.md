This is a crawler to scrap from a website all the details about cars

There are two spiders, one to scrap all the links of cars, and one to scrap all the details of cars.
In order to use, create a file <file_name>.csv which will be populate with the links.

In the terminal run scrapy crawl car_urls -o <file_name>.csv
This will download all links of cars in the site

Then run the second spider, by executing the following command in the same directory of the terminal:
scrapy crawl car_spider -o <the_file_name_you_prefer>.csv

The spider will read all the links at and will scrap each page it founds, and store the info in a csv.



