#!/usr/bin/python
"""Script can be used to calculate the Gini Index of a column in a CSV file.

Classes are strings."""

import fileinput
import csv
from collections import defaultdict, Counter


############### Set up variables
# Declare variables: global
candidates = [] # List of all the candidate names. Includes duplicates
zipCodes = [] # List of all the zip codes
zipCand = defaultdict(Counter) # Dictionary with zipcode as key. The values are dictionaries with candidate name as key and number of records for the candidate in that zip as value
totalRec = 0
gini = 0  # current Gini Index using candidate name as the class
split_gini = 0  # weighted average of the Gini Indexes using candidate names, split up by zip code

#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

# This method is used to compute the Gini Index using candidate name as the class
def computeGini():
    for row in csv.reader(fileinput.input()):
        if not fileinput.isfirstline():
            global totalRec, zipCodes
            totalRec += 1 # Calculate the total number of records in the dataset
            zipCodes.append(row[6]) # Make a list of all the zip codes
            candidates.append(row[2]) # Make a list of all the candidate names. Includes duplicates

            """ Create a dictionary with zipcodes as key. The values are dictionaries with
            candidate name as key and number of records for the candidate in that zip as value.
            Eg. {'94704': {'ABC': 10, 'BCD': 20}...}'"""
            zipCand[row[6]][row[2]] += 1

    zipCodes = list(set(zipCodes)) # Remove duplicate zipcodes
    fracs = []
    candidateRecs = Counter(candidates) # This counter will create a dictionary with candidate name as key and number of records for each candidate as value
    for i in candidateRecs:
        fracs.append(candidateRecs[i] / float(totalRec)) # Fraction of each candidate in the candidate class

    gini = 1 - sum(frac**2 for frac in fracs)
    return gini

# This method is used to compute the Gini Index using candidate names, split up by zip code
def computeSplitGini():
    global zipCodes, totalRec
    sginiArray = []
    for zip in zipCodes:
        ztotalRec = 0
        zfracs = []
        for cand in zipCand[zip]:
            ztotalRec += zipCand[zip][cand] # Total number of records for each zipcode

        for cand in zipCand[zip]:
            zfracs.append(zipCand[zip][cand] / float(ztotalRec)) # Fraction of each candidate in a zipcode

        tempGini = 1 - sum(frac**2 for frac in zfracs)

        sginiArray.append(tempGini * ztotalRec / float(totalRec))

    split_gini = sum(sginiArray)
    return split_gini

gini = computeGini()
split_gini = computeSplitGini()

print "Gini Index: %s" % gini
print "Gini Index after split: %s" % split_gini



