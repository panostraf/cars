import scrapy
from bs4 import BeautifulSoup
from ..items import CarGrItem
from ..items import CarLinks
import re
import random
import sys
import os

class CarSpiderSpider(scrapy.Spider):
    # Define the name of the crawler
    name = 'car_spider'
    allowed_domains = ['car.gr']
    
    # # Here are the URL's it will visit
    # start_urls = ['https://www.car.gr/classifieds/cars/view/35414737-peugeot-2008',
    #                 'https://www.car.gr/classifieds/cars/view/33311025-citroen-c4',
    #                 'https://www.car.gr/classifieds/cars/view/30910149-citroen-c4',
    #                 'https://www.car.gr/classifieds/cars/view/34681732-smart-fortwo',
    #                 'https://www.car.gr/classifieds/cars/view/32040189-smart-fortwo']
    #                 # 'https://www.car.gr/classifieds/cars/view/35414737-peugeot-2008']
    start_urls = []
    text_file = open(os.getcwd()+'/car_links.csv','r')
    for row in text_file:
        row = 'https://www.car.gr'+str(row.replace(r'\w',''))
        start_urls.append(str(row))
    

    def parse(self, response,**kwargs):
        # items refers to the fields specified in items.py
        items = CarGrItem()
        # The x path of the table which cointains all the values
        table = response.xpath('//table[@id="specification-table"]').xpath('//tr')

        # Loop through table ( the index 0 is the field name, and index [1:] cointain the values)
        for i in range(len(table)):

            # Give an empty field name 
            field_name=''

            # i referes to the first row of the table
            data = table[i].xpath('td')
            print("------------------------------")
            text = ''

            # j refers to the column ( or the depth of the html code under table tag)
            for j in range(len(data)):

                # Use bs4 to convert data to text
                soup = BeautifulSoup(data[j].extract())
                values = soup.get_text()
                values = values.replace('\n','')

                # If j = 0 the value is the field name
                if j == 0:

                    # Remove \w to match with item fields dictionary
                    values = values.replace(' ','')
                    print(self.field_finder(values))
                    field_name = self.field_finder(values)

                else:
                    # Merge all extracted text into one 
                    text = text + values
            try:
                # in case field_name is '' it will return None
                items[str(field_name)] = text
            except:
                pass
        # return all items
        yield items

        print('going to the next page...\n\n\n\n\n\n\n\n\n')
        # print('------------------')


    def field_finder(self,field_name):
        # this function uses the this dictionary to map the extracted fields with the correct items[field]
        dict_fields = {'Μάρκα-μοντέλο':'maker',
                        "Νούμεροαγγελίας":"model_number",
                        "Κατάσταση":"condition",
                        "Τιμή":"price",
                        "Κατηγορία":"category",
                        "Χρονολογία":"registration",
                        "Χιλιόμετρα":"mileage",
                        "Καύσιμο":"fuel_type",
                        "Κυβικά":"cc",
                        "Ίπποι":"hp",
                        "Σασμάν":"transmission",
                        "Χρώμα":"color",
                        "Χρώμαεσωτερικού":"interior_color",
                        "Επένδυσησαλονιού":"interior_type",
                        "Μέγεθοςζάντας":"wheels_size",
                        "Πινακίδα":"number_plate",
                        "Κίνηση":"drive_type",
                        "Αερόσακοι":"airbags",
                        "Πόρτες":"doors",
                        "Καθίσματα":"seats",
                        "Τελευταίααλλαγή":"modified",
                        "Εμφανίσειςαγγελίας":"views",
                        "Σύνδεσμος":"link",
                        "Τηλέφωνο":"phone",
                        "'Ονομα":"name",
                        "Διεύθυνση":'address',
                        "Τηλέφωνο 1 ":'phone2'}
        try:
            return dict_fields[str(field_name)]
        except:
            pass

class CarSpiderSpider_links(scrapy.Spider):
    # Define the name of the crawler
    name = 'car_urls'
    allowed_domains = ['car.gr']
    # Here are the URL's it will visit
    start_urls = []
    urls = [f'https://www.car.gr/classifieds/cars/?fs=1&pg={i}' for i in range(30)]
    while len(urls) > 1:
        i = random.randint(1,len(urls)-1)
        start_urls.append(urls[i])
        del urls[i]


    
    def parse(self, response,**kwargs):
        # items refers to the fields specified in items.py
        items = CarLinks()

        rule = r'/classifieds/cars/view/.*'
        links = response.xpath('//li//@href').getall()
        for link_ in links:
            print(link_)
            if re.search(rule,link_):
                items['link'] = link_
                yield items

            




