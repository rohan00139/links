from bs4 import BeautifulSoup
import requests
import csv

def get_links(str):
    r=requests.get("%s"%str)
    data=r.text
    soup=BeautifulSoup(data,'lxml')
    li = []

    for link in soup.find_all('a'):
        le=link.get('href')
        if le[0]=='h':
           li.append(le)
        else:
            continue
    print(len(li))

    csv=open("links.csv","w")
    for col in li:
        csv.write(col+",")

r=requests.get("https://medium.com")
data=r.text
soup=BeautifulSoup(data,'lxml')
list1 = []
for link in soup.find_all('a'):
    le=str(link.get('href'))
    if le[0]=='h':
      list1.append(le)
# write 1st set of links from medium.com to csv file
csv=open("links.csv","w")
for col in list1:
    csv.write(col+", ")

#use 1st set to get rest of the links
for i in range(0,5):
     get_links(list1[i])

csv=open("links.csv","r")
for row in csv:
    print(row+",")
print(len(row))
