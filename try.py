from selenium import webdriver
import requests, bs4
res = requests.get('http://karresults.nic.in/indexPUC_2019.asp')
res.raise_for_status();
soup = bs4.BeautifulSoup(res.text,features='lxml')
print type(soup)
elems = soup.select('#reg')
print type(elems)
print "========"
print elems
