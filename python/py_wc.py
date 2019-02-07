from bs4 import BeautifulSoup
from pprint import pprint
from urllib.request import urlopen
import sys

try:
  url = sys.argv[1]
except:
  url = 'https://github.com/LuckyPigeon/LuckyPigeon/blob/master/CONTRIBUTING.md'

html = urlopen(url)
bsObj = BeautifulSoup(html.read(), 'html.parser')
title = bsObj.find('title').text.split()[0]
textArray = bsObj.find('div', {'class': 'file-info'}).text.split('\n')
textArray = [line.strip() for line in textArray]
textArray = list(filter(lambda x: x != '', textArray))

numArray = []

tmpString = ','.join(textArray)
tmpNum = ''

for index in range(len(tmpString)):
  if tmpString[index].isnumeric():
    tmpNum += tmpString[index]
  elif tmpString[index - 1].isnumeric() and not tmpString[index].isnumeric():
    numArray.append(tmpNum)
    tmpNum = ''

print('Filename: ' + title)
print('Lines: ' + numArray[0])
print('Source Line of Code: ' + numArray[1])
print('Words(bytes): ' + numArray[2])
