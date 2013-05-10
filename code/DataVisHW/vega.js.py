import codecs
import json
import csv

fb = codecs.open('data/yelp_academic_dataset_business.json', encoding='iso-8859-1')
categories = {}
for line in fb:
    jsonc = json.loads(line)
    business_id = jsonc['business_id']
    cats = jsonc['categories']
    categories[business_id] = cats


f1 = codecs.open('data/training1_1000.json', encoding='iso-8859-1')
data = []
n = 0

sel_cats = ['Chinese', 'Italian', 'Mexican', 'Mediterranean', 'American (Traditional)', 'American (New)']

for line in f1:
    if n < 500:
        jsonc = json.loads(line)
        catsTemp = categories[jsonc['business_id']]

        for c in catsTemp:
            if c == 'Italian':
                rev_dict = dict()
                rev_dict['date'] = jsonc['date']
                rev_dict['stars'] = jsonc['stars']
                rev_dict['category'] = c
                data.append(rev_dict)
        n += 1

data1 = sorted(data, key=lambda k: k['date'])

dump = json.dumps(data1)

f = open("data/log.txt", 'w')
f.write(dump)
f.close()

with open('data/data.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['category', 'date', 'stars'])
    for d in data1:
        csvwriter.writerow([d['category'], d['date'], d['stars']])

