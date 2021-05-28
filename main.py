from bs4 import BeautifulSoup

with open('Gold Price Today _ Live Updates _ APMEX.html','r') as html_file:
  content = html_file.read()
  print(content)