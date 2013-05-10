import codecs
import json
import csv
import calendar

fb = codecs.open('yelp_academic_dataset_business.json', encoding='iso-8859-1')
categories = {}
for line in fb:
    jsonc = json.loads(line)
    business_id = jsonc['business_id']
    cats = jsonc['categories']
    categories[business_id] = cats

sel_cats = ['French', 'Chinese', 'Italian', 'Mexican', 'Mediterranean', 'American (New)', 'Indian', 'Thai', 'Japanese']

with open('data.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['category', 'month', 'avgStars'])

ratings = dict()
mons = dict((k, v) for k,v in enumerate(calendar.month_abbr))

for cc in sel_cats:
    ratings[cc] = {}
    for mon in mons:
        ratings[cc][mon] = []

f1 = codecs.open('yelp_academic_dataset_review.json', encoding='iso-8859-1')
for line in f1:
    jsonc = json.loads(line)
    catsTemp = categories[jsonc['business_id']]

    for c in catsTemp:
        if not c in sel_cats:
            continue
        if int(jsonc['date'][0:4]) == 2012:
            ratings[c][int(jsonc['date'][5:7])].append(jsonc['stars'])

avg_ratings = dict()

for r in ratings:
    avg_ratings[r] = {}
    for m in ratings[r]:
        if m == 0:
            continue
        avg_ratings[r][m] = sum(ratings[r][m]) / float(len(ratings[r][m]))

with open('data.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    for cat in avg_ratings:
        for m in avg_ratings[cat]:
            csvwriter.writerow([cat, mons[m], avg_ratings[cat][m]])



