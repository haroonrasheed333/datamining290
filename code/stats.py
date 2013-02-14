#!/usr/bin/python
"""This script can be used to analyze data in the 2012 Presidential Campaign,
available from http://www.fec.gov/disclosurep/PDownload.do"""

import fileinput
import csv

candidates = []
donationStats = dict()
def stats(candidate=''):
    total = 0
    amtArray = []
    minimum = 0
    maximum = 0
    mean = 0
    median = 0
    sd = 0
    numRecords = 0
    var = 0
    for row in csv.reader(fileinput.input()):
        if not fileinput.isfirstline() and (candidate == '' or candidate == row[2]):
            total += float(row[9])
            amtArray.append(float(row[9]))
            numRecords += 1

            if numRecords == 1 or float(row[9]) < minimum:
                minimum = float(row[9])

            if float(row[9]) > maximum:
                maximum = float(row[9])

            if candidate == '':
                cand = row[2]
                if not cand in candidates:
                    candidates.append(cand)

    mean = total / numRecords

    amtArray.sort()

    if numRecords % 2 == 0:
        median = amtArray[(numRecords+1)/2]
    else:
        median = (amtArray[numRecords/2] + amtArray[(numRecords/2)+1]) / 2

    for x in amtArray:
        var += ((x-mean)*(x-mean))

    var = var / numRecords

    sd = var**0.5

    donationStats[candidate] = {}
    donationStats[candidate]['total'] = total
    donationStats[candidate]['minimum'] = minimum
    donationStats[candidate]['maximum'] = maximum
    donationStats[candidate]['mean'] = mean
    donationStats[candidate]['median'] = median
    donationStats[candidate]['sd'] = sd

    return donationStats

totalDonationStats = stats()
##### Print out the stats
print "Stats for the whole data"
print "Total: %s" % totalDonationStats['']['total']
print "Minimum: %s" % totalDonationStats['']['minimum']
print "Maximum: %s" % totalDonationStats['']['maximum']
print "Mean: %s" % totalDonationStats['']['mean']
print "Median: %s" % totalDonationStats['']['median']
print "Standard Deviation: %s" % totalDonationStats['']['sd']
##### Comma separated list of unique candidate names
print "Candidates: %r" % candidates

minimum = totalDonationStats['']['minimum']
maximum = totalDonationStats['']['maximum']
mean = totalDonationStats['']['mean']
sd = totalDonationStats['']['sd']

def minmax_normalize(value):
    """Takes a donation amount and returns a normalized value between 0-1. The
    normilzation should use the min and max amounts from the full dataset"""
    ###
    # TODO: replace line below with the actual calculations
    norm = ((value - minimum) / (maximum - minimum))
    ###/

    return norm

def zscore_normalize(value):
    norm = (value - mean) / sd
    return norm

##### Normalize some sample values
print "Min-max normalized values: %r" % map(minmax_normalize, [2500, 50, 250, 35, 8, 100, 19])

#*************************** Extra Credit z-score *****************************#
print "z-score normalized values: %r" % map(zscore_normalize, [2500, 50, 250, 35, 8, 100, 19])

#*************************** Extra Credit stats for each candidates *****************************#
candidateDonationStats = dict()
print "Computing stats for each candidate. Please wait"
for candidate in candidates:
    candidateDonationStats = stats(candidate)

for candidate in candidates:
    print "Details for candidate: %s" % candidate
    print "Total: %s" % candidateDonationStats[candidate]['total']
    print "Minimum: %s" % candidateDonationStats[candidate]['minimum']
    print "Maximum: %s" % candidateDonationStats[candidate]['maximum']
    print "Mean: %s" % candidateDonationStats[candidate]['mean']
    print "Median: %s" % candidateDonationStats[candidate]['median']
    print "Standard Deviation: %s" % candidateDonationStats[candidate]['sd']

