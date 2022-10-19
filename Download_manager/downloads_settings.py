

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml
import json
from dataclasses import dataclass
import sys,os
sys.path.append(os.getcwd())
from Assistant_service.openers import OpenJson
from time import sleep
import difflib

# @dataclass
# class GoogleDriverOption: #вынести в другой модуль
#     ...

# {
#     'headless'
# }



def setting_options(hide_gui=True): # https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
    ''' setting browser :
         show | not - browser window'''
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # chrome_options.headless = hide_gui
    # chrome_options.add_argument('--disable-gpu') # Надо бы прочеать с возможностью вызова ебз доп функций setting_options
    return chrome_options

class DriveOptions:
    def __init__(self, hide=False):
        self.hide = hide
        self._driver = None

        if self._driver == None:
            self.connect_to
    @property
    def connect_to(self):
        browser_settings = setting_options(self.hide)
        driver = webdriver.Chrome(ChromeDriverManager().install(),
            chrome_options=browser_settings)
        self._driver  = driver

class DriverMaker:
    def __init__(self,driver_name,main_link,_main_driver) -> None:

        self.driver_name = driver_name
        self.main_link = main_link
        self._main_driver = _main_driver._driver


        self.main_driver_page = None

        if self.main_driver_page == None:
            self.driver_make_main
    @property
    def driver_make_main(self):
        self.main_driver_page = self._main_driver.get(self.main_link)


# test_2 = DriveOptions()
# _, driver_test_2 = test_2.connect_to , test_2._driver
# b = driver_test_2.get(ynd_2)

class DriverScope:
    def __init__(self,main_driver:DriverMaker) -> None:
        self.chain = []

    def __add__(self,*args,**kwargs):
        ...

class PageInfo:
    ...
options_disclosure = DriveOptions()
yandex_main_link = 'https://yandex.ru/maps/?ll=37.130937%2C55.980951&z=14'
yandex_main = DriverMaker('yandex_main_page',yandex_main_link,options_disclosure)

# yandex_main.driver_make
# a = yandex_main.main_driver_page

# print(
#     yandex_main._main_driver.page_source
# )

# port_('http://127.0.0.1:5500/')

ynd_2 = 'https://yandex.ru/maps/213/moscow/?ll=37.614829%2C55.764589&mode=routes&rtext=55.644887%2C37.519413~55.755930%2C37.681982~55.886650%2C37.703963~55.738100%2C37.658131&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NjY1MjYwNxJJ0KDQvtGB0YHQuNGPLCDQnNC%2B0YHQutCy0LAsINGD0LvQuNGG0LAg0JzQuNC60LvRg9GF0L4t0JzQsNC60LvQsNGPLCAxONC6MiIKDeITFkIVXpReQg%3D%3D~~~ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NjcwMDQ1OBJI0KDQvtGB0YHQuNGPLCDQnNC%2B0YHQutCy0LAsINCS0L7RgNC%2B0L3RhtC%2B0LLRgdC60LDRjyDRg9C70LjRhtCwLCAxOdCQ0YExIgoN7qEWQhXQ815C&z=11.44'



# Nsella_start = 'https://yandex.ru/maps/213/moscow/?ll=37.681982%2C55.755930&mode=routes&rtext=55.755930%2C37.681982&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NjcxNjMxMhJI0KDQvtGB0YHQuNGPLCDQnNC%2B0YHQutCy0LAsINCS0L7Qu9C%2B0YfQsNC10LLRgdC60LDRjyDRg9C70LjRhtCwLCAxMtCQ0YExIgoNWboWQhUTBl9C&z=17.16'
# 'https://yandex.ru/maps/213/moscow/?ll=37.680091%2C55.821315&mode=routes&rtext=55.755930%2C37.681982~55.886650%2C37.703963&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NjcxNjMxMhJI0KDQvtGB0YHQuNGPLCDQnNC%2B0YHQutCy0LAsINCS0L7Qu9C%2B0YfQsNC10LLRgdC60LDRjyDRg9C70LjRhtCwLCAxMtCQ0YExIgoNWboWQhUTBl9C~ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1Njc5ODIwMxI80KDQvtGB0YHQuNGPLCDQnNC%2B0YHQutCy0LAsINCh0YLQsNGA0YLQvtCy0LDRjyDRg9C70LjRhtCwLCA3IgoN29AWQhXui19C&z=12.34'
# DriverMaker('https://yandex.ru/maps/?ll=37.130937%2C55.980951&z=14',On_). \
# page_connection()



# news = 'https://ria.ru/'
# DriverMaker(news,On_). \
# page_connection()




# chrome_options = Options()
# chrome_options.headless = False
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(ChromeDriverManager().install(),
#             chrome_options=chrome_options)





# https://yandex.ru/maps/213/moscow/?ll=37.615882%2C55.764589&mode=routes&rtext=55.755930%2C37.681982~55.886650%2C37.703963~55.738100%2C37.658131~55.644887%2C37.519413&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NjcxNjMxMhJI0KDQvtGB0YHQuNGPLCDQnNC%2B0YHQutCy0LAsINCS0L7Qu9C%2B0YfQsNC10LLRgdC60LDRjyDRg9C70LjRhtCwLCAxMtCQ0YExIgoNWboWQhUTBl9C~~~ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NjY1MjYwNxJJ0KDQvtGB0YHQuNGPLCDQnNC%2B0YHQutCy0LAsINGD0LvQuNGG0LAg0JzQuNC60LvRg9GF0L4t0JzQsNC60LvQsNGPLCAxONC6MiIKDeITFkIVXpReQg%3D%3D&z=11.44
# https://yandex.ru/maps/213/moscow/?ll=37.614829%2C55.764589&mode=routes&rtext=55.644887%2C37.519413~55.755930%2C37.681982~55.886650%2C37.703963~55.738100%2C37.658131&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NjY1MjYwNxJJ0KDQvtGB0YHQuNGPLCDQnNC%2B0YHQutCy0LAsINGD0LvQuNGG0LAg0JzQuNC60LvRg9GF0L4t0JzQsNC60LvQsNGPLCAxONC6MiIKDeITFkIVXpReQg%3D%3D~~~ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NjcwMDQ1OBJI0KDQvtGB0YHQuNGPLCDQnNC%2B0YHQutCy0LAsINCS0L7RgNC%2B0L3RhtC%2B0LLRgdC60LDRjyDRg9C70LjRhtCwLCAxOdCQ0YExIgoN7qEWQhXQ815C&z=11.44
# https://yandex.ru/maps/213/moscow/?ll=37.600834%2C55.698807&mode=routes&rtext=55.644887%2C37.519413&rtt=mt&ruri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg1NjY1MjYwNxJJ0KDQvtGB0YHQuNGPLCDQnNC%2B0YHQutCy0LAsINGD0LvQuNGG0LAg0JzQuNC60LvRg9GF0L4t0JzQsNC60LvQsNGPLCAxONC6MiIKDeITFkIVXpReQg%3D%3D&z=12.55
# @dataclass
# class Parser:

#     open_connection_page : str



#     def page_connection(self,options=True):
#         driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=get_options(options))

#         driver.get(self.open_connection_page)
#         self.page = driver
#         return driver


#     @property
#     def get_page(self):
#         return self.page.page_source

#     @staticmethod
#     def load_page(page) -> str:
#         return (Parser().page_connection(page)).get_page



# class SaveFromInternet:
#     pass


# Parser('https://yandex.ru/maps/213/moscow/?ll=37.622504%2C55.753215&z=10')