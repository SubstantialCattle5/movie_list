from bs4 import BeautifulSoup
import requests
import re
import prettytable
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
CHROME_WEBDRIVER = 'E:\PROJECTS\chromedriver'


def movies():
    pt = [prettytable.PrettyTable() for i in range(3)]
    response = requests.get('https://www.rottentomatoes.com/top/')
    soup = BeautifulSoup(response.text, parser='lxml', features='lxml')

    # Headings List
    headings = soup.find_all(name='h2', class_='panel-heading')
    headings_list = [i.text for i in headings if re.search('^Best Movies of [0-9]+', i.text)]

    # Movies List
    def movie_list(index: int):
        list_movies = soup.find_all(name='table', class_='movie_list')[index].text.split('\n')
        list_movies = [i for i in list_movies if not i == '' and not re.search('^[0-9]+[%.]', i)]
        return list_movies

    # Creating the dictionary
    movie_yr = dict()
    keys = [2, 4, 6]
    movie_yr = {key: movie_list(index=val) for key, val in zip(headings_list, keys)}

    table = lambda column_num: pt[column_num].add_column(list(movie_yr.keys())[column_num],
                                                         movie_yr[list(movie_yr.keys())[column_num]])

    for i in range(3):
        table(i)
        print(pt[i])
