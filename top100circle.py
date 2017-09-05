from bs4 import BeautifulSoup
import csv
import requests

r  = requests.get("http://songkeybpm.com/")

data = r.text

soup = BeautifulSoup(data, "lxml")

mydivs = soup.findAll("div", { "class" : "attribute-container text-center col-lg-2 col-xs-6 col-sm-4" })

keys = []
bpms=[]
#Key, Camelot, Duration, BPM
for div in mydivs:
  labels = div.find_all('p', {'class': 'attribute-label'})
  data = {'key': '', 'bpm': ''}
  for label in labels:
    if label.text=='Key':
      keys.append(label.parent.find_all('p', {'class': 'attribute'})[0].text.encode('utf-8'))
    if label.text=='BPM':
      bpms.append(label.parent.find_all('p', {'class': 'attribute'})[0].text.encode('utf-8'))

print len(bpms)

total_data = zip(keys, bpms)
print total_data
#print total_data[2][0].replace('\xe2\x99\xad', 'b')



##text=List of strings to be written to file
with open('csvfile.csv','wb') as file:
  for elt in total_data:
    key = elt[0].replace('\xe2\x99\xad', 'b')
    bpm = elt[1]
    file.write(key+","+bpm)
    file.write('\n')
