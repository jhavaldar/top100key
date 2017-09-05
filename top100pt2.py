import csv

data=[]
with open('csvfile.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  for row in reader:
    data.append({'key': row[0], 'bpm': row[1]})

#print data

enharm = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
def num_tone(tone):
  return enharm.index(tone)

def rel_maj(tone):
  index = (num_tone(tone) + 3) % 12
  return enharm[index]


buckets = {}
for tone in enharm:
  buckets[tone] = 0

for song in data:
  key = song['key']
  tone,scale = key.split(" ")
  if scale=='Minor':
    tone = rel_maj(tone)
    song['key'] = tone + " Major"
  buckets[tone]+=1

## Send the data into buckets
#for song in data:

circle = ['C','G','D','A','E', 'B', 'F#', 'Db','Ab', 'Eb', 'Bb', 'F']

final_data = []
for tone in circle:
  key = {}
  key['axis'] = tone
  key['value'] = buckets[tone]
  final_data.append(key)

##text=List of strings to be written to file
with open('circle.csv','wb') as file:
  for elt in final_data:
    file.write(elt['axis']+" Major"+","+str(elt['value']))
    file.write('\n')
