### Author: Ben Tannenwald
### Date: Oct 10, 2017
### Purpose: really simple assignment between online form # and campaign filing

import json

# 0. *** Open JSON file with URL and form information
with open('../scraping/multiForm_10-10-2017.json') as data_file:
    data = json.load(data_file)

    
# 1. *** Produce list of candidates
c_list={}
for entry in data[:]:
    if entry['candidate'] not in c_list:
        c_list[ entry['candidate'] ] = 1
    else:
        c_list[ entry['candidate'] ] = c_list[ entry['candidate'] ] + 1

# ** Print list of how many candidates and how many contributions each has
print '############################################'
print 'Processed information for', len(c_list), 'candidates'
print '############################################'
for cand in c_list:
    print cand, 'has', c_list[cand], 'contributions' 
print '############################################'


# 2. *** Create first pass at intelligent data-structure
c_list2={}
for entry in data[:]:
    # store candidate name
    cName = entry['candidate']
    entry_temp = entry
    del entry_temp['candidate']
    
    if cName not in c_list2:
        #print entry_temp
        c_list2[cName] = [entry_temp]
    else: 
        c_list2[cName].append(entry_temp)

# ** Check list of how many candidates and how many contributions each has
print '############################################'
print 'Processed information for', len(c_list2), 'candidates'
print '############################################'
for cand in c_list2:
    print cand, 'has', len(c_list2[cand]), 'contributions' 
print '############################################'


# 3. *** Split irst pass at intelligent data-structure
c_list3 = {}
for cand in c_list2.keys(): # loop over candidates
    c_list3[cand] = {} # make top-level candidate object
    for contribution in c_list2[cand]: # loop over contributions
        # store report name
        reportName = contribution['report']
        contrib_temp = contribution
        del contrib_temp['report']
    
        if reportName not in c_list3[cand]:
            c_list3[cand][reportName] = [contrib_temp] 
        else: 
            c_list3[cand][reportName].append(entry_temp)

# ** Print list of how many candidates and how many contributions each has
print '############################################'
print 'Processed information for', len(c_list3), 'candidates'
print '############################################'
for cand in c_list3:
    print cand, 'has', len(c_list3[cand]), 'reports' 
    for report in c_list3[cand]:
        print "\t", report, 'has', len(c_list3[cand][report]), 'contributions' 
print '############################################'
