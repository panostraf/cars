# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarGrItem(scrapy.Item):
    # define the fields for your item here like:
    maker = scrapy.Field()
    model_number= scrapy.Field()
    condition= scrapy.Field()
    price= scrapy.Field()
    category= scrapy.Field()
    registration= scrapy.Field()
    mileage= scrapy.Field()
    fuel_type= scrapy.Field()
    cc= scrapy.Field()
    hp= scrapy.Field()
    transmission= scrapy.Field()
    color= scrapy.Field()
    kteo= scrapy.Field()
    euro_standard= scrapy.Field()
    number_plate= scrapy.Field()
    previous_owners= scrapy.Field()
    drive_type= scrapy.Field()
    airbags= scrapy.Field()
    doors= scrapy.Field()
    seats= scrapy.Field()
    modified= scrapy.Field()
    views= scrapy.Field()
    link= scrapy.Field()
    phone= scrapy.Field()
    extras= scrapy.Field()
    description= scrapy.Field()
    name= scrapy.Field()
    address= scrapy.Field()
    phone2= scrapy.Field()
    interior_color = scrapy.Field()
    interior_type = scrapy.Field()
    wheels_size = scrapy.Field()

class CarLinks(scrapy.Item):
    link = scrapy.Field()
