### Author: Ben Tannenwald
### Date: Oct 12, 2017
### Purpose: file to store useful functions for plotting contribution information

import operator, numpy as np, datetime as dt
import matplotlib.pyplot as plt, matplotlib.dates as date2num, matplotlib.ticker as tkr
from matplotlib.gridspec import GridSpec


def makeMultiCandidateUniqueDonorList(candidateFiles, title):
    """function for making .txt files summarizing all unique donors, ranking by amount donated, and noting how many donations"""

    uniqueList_total = {}
    for file in candidateFiles:
        uniqueList_temp = file.returnUniqueDonorList()
        for donor in uniqueList_temp:
            if donor not in uniqueList_total:
                uniqueList_total[donor] = uniqueList_temp[donor]
            else:
                uniqueList_total[donor][0] = uniqueList_total[donor][0] + uniqueList_temp[donor][0]
                uniqueList_total[donor][1] = uniqueList_total[donor][1] + uniqueList_temp[donor][1]
        
    uniqueList_total_ordered = sorted(uniqueList_total.items(), key=operator.itemgetter(1), reverse=True)
    nTotal, totalAmount = 0, 0
    
    #outfile = open('../tables/'+candidateFile.candidate.replace(' ','')+'_uniqueDonorList.txt', 'w')
    outfile = open('../tables/'+title+'_uniqueDonorList.txt', 'w')
    outfile.write('{0: <48} \t\t ${1: <20} \t\t {2: <10} \n'.format('Donor', 'Money Donated', '# Donations') )
    outfile.write('==============================================================================================================\n')
    
    #for donor in uniqueList_all.keys():
    for entry in uniqueList_total_ordered:
        donor = entry[0]
        outfile.write('{0: <48} \t\t ${1: <20} \t\t {2: <10} \n'.format(donor,uniqueList_total[donor][1],str(uniqueList_total[donor][0])) )
        nTotal = nTotal + uniqueList_total[donor][0]
        totalAmount = totalAmount + uniqueList_total[donor][1]

    outfile.write('==============================================================================================================\n')
    outfile.write('{0: <48} \t\t ${1: <20} \t\t {2: <10} \n'.format('Totals', totalAmount, nTotal) )        
    outfile.close()
    return


def makeUniqueDonorList(candidateFile):
    """function for making .txt files summarizing all unique donors, ranking by amount donated, and noting how many donations"""

    uniqueList_all = candidateFile.returnUniqueDonorList()
    uniqueList_all_ordered = sorted(uniqueList_all.items(), key=operator.itemgetter(1), reverse=True)
    nTotal, totalAmount = 0, 0
    
    outfile = open('../tables/'+candidateFile.candidate.replace(' ','')+'_uniqueDonorList.txt', 'w')
    outfile.write('{0: <48} \t\t ${1: <20} \t\t {2: <10} \n'.format('Donor', 'Money Donated', '# Donations') )
    outfile.write('==============================================================================================================\n')
    
    #for donor in uniqueList_all.keys():
    for entry in uniqueList_all_ordered:
        donor = entry[0]
        outfile.write('{0: <48} \t\t ${1: <20} \t\t {2: <10} \n'.format(donor,uniqueList_all[donor][1],str(uniqueList_all[donor][0])) )
        nTotal = nTotal + uniqueList_all[donor][0]
        totalAmount = totalAmount + uniqueList_all[donor][1]

    outfile.write('==============================================================================================================\n')
    outfile.write('{0: <48} \t\t ${1: <20} \t\t {2: <10} \n'.format('Totals', totalAmount, nTotal) )        
    outfile.close()

    return uniqueList_all

def makeTotalAndAllReportByTime(candidateFile):
    """function for making plot showing total contributions as function of time"""

    amountsByTime_all, datesByTime_all = candidateFile.returnAmountValuesWithTime()
    #amountsByTime_pre, datesByTime_pre = candidateFile.returnAmountValuesWithTime('Pre Primary')


    x = [dt.datetime.strptime(d,'%Y/%m/%d').date() for d in datesByTime_all] 
    y = [value for value in amountsByTime_all] # individual contributions
    y2, sum = [y[0]], y[0]
    for contrib in y[1:]: # cumulative contributions
        sum = sum + contrib
        y2.append( sum ) 
        
    fig = plt.figure( candidateFile.candidate.replace(' ','')+'_byTime')
    plt.title(candidateFile.candidate+': '+'All Contributions', fontsize=18, fontweight='bold')
    plt.ylabel("Amount Raised [$]", fontsize=18)
    plt.xlabel("Date", fontsize=15)
    
    graph = fig.add_subplot(111)
    indiv, = graph.plot(x,y,'r-o', label='Individual')
    cumul, = graph.plot(x,y2,'b-o', label='Cumulative')
    graph.set_xticklabels( [ date.strftime("%m/%d/%Y") for date in x] )
    fig.autofmt_xdate()

    plt.gca().xaxis.set_major_formatter(tkr.FuncFormatter(xfmt))
    daygap = abs((x[0] - x[len(x)-1]).days)
    plt.gca().xaxis.set_major_locator(date2num.DayLocator(interval=int(daygap/10)))
    plt.gca().xaxis.set_minor_locator(date2num.DayLocator())

    plt.legend([cumul, indiv], ['Cumulative', 'Individual'],loc=2)

    plt.savefig( '../figures/byTime/'+candidateFile.candidate.replace(' ','')+'_Total_byTime.png')
    plt.savefig( '../figures/byTime/'+candidateFile.candidate.replace(' ','')+'_Total_byTime.pdf')

def xfmt(x,pos=None):
    ''' custom date formatting '''
    x = date2num.num2date(x)
    label = x.strftime('%m/%d/%Y')
    label = label.lstrip('0')
    return label
    
def makeTotalAndAllReportHistograms(candidateFile):
    """function for producing histograms showing donation amount"""

    #fig, axes = plt.hist()
    #fig, axes = plt.subplots(rows, 3, figsize=(14,1+3.5*rows))
    #fig.suptitle(candidateFile.candidate, fontsize=20, fontweight='bold')
    #fig.subplots_adjust(wspace = 0.5, hspace = 0.3 )
    
    plt.figure( candidateFile.candidate.replace(' ','')+'_byDonation')
    donation_data = candidateFile.returnAmountValues()
    #print donation_data
    n, bins, patches = plt.hist(donation_data, bins=25, range=(0,500))
    index, value = max(enumerate(n), key=operator.itemgetter(1))
    plt.title(candidateFile.candidate+': '+'All Contributions', fontsize=18, fontweight='bold')
    plt.ylabel("Number of Contributions", fontsize=18)
    plt.xlabel("Contribution Value [$]", fontsize=15)
    
    #print n, bins, value, index
    #print np.median(donation_data), np.mean(donation_data)
    plt.text( int(0.3*max(bins)), value*.9, 'Total Raised: $%.2f'%candidateFile.totalRaised, fontsize=14)
    plt.text( int(0.3*max(bins)), value*.84, 'Mean Contribution: $%.2f'%(candidateFile.totalRaised/candidateFile.totalContributions), fontsize=14)
    plt.text( int(0.3*max(bins)), value*.78, 'Percent Raised from ', fontsize=14)
    plt.text( int(0.34*max(bins)), value*.73, "Contributions > \$1000: %.1f %%"% (100*sum([i for i in donation_data if i > 1000])/candidateFile.totalRaised), fontsize=14)
    plt.text( int(0.34*max(bins)), value*.67, "Contributions < \$500: %.1f %%"% (100*sum([i for i in donation_data if i <= 500])/candidateFile.totalRaised), fontsize=14)

    plt.savefig( '../figures/byAmount/'+candidateFile.candidate.replace(' ','')+'_Total_byAmount.png')
    plt.savefig( '../figures/byAmount/'+candidateFile.candidate.replace(' ','')+'_Total_byAmount.pdf')
 

def makeTotalAndAllReportPlotsByLocation(candidateFile):
    """function for producing pie charts splitting donations by location"""

    rows = candidateFile.nReports + 1 # plus one for summary
    fig, axes = plt.subplots(rows, 3, figsize=(14,1+3.5*rows))
    fig.suptitle(candidateFile.candidate, fontsize=20, fontweight='bold')
    fig.subplots_adjust(wspace = 0.5, hspace = 0.3 )
    
    # *** A. First row shows over summary
    location_data = candidateFile.returnContributionLocations()
    makeLocationPieChart(axes[0][0], location_data, 'nContributions')  # ** first column
    makeLocationPieChart(axes[0][1], location_data, 'nRaised')         # ** second column
    makeLocationTextSummary(axes[0][2], location_data)                 # ** third column
    
    # *** B. Loop over time-ordered reports
    row = 1
    for report in candidateFile.orderedReports:
        location_data = candidateFile.returnContributionLocations(report)
        makeLocationPieChart(axes[row][0], location_data, 'nContributions')  # ** first column
        makeLocationPieChart(axes[row][1], location_data, 'nRaised')         # ** second column
        makeLocationTextSummary(axes[row][2], location_data, report, date=candidateFile.filings[report]['filingDate'] )                 # ** third column
            
        # move to next row
        row = row + 1

    fig.savefig( '../figures/byLocation/'+candidateFile.candidate.replace(' ','')+'_TotalAndReports_byLocation.png')
    fig.savefig( '../figures/byLocation/'+candidateFile.candidate.replace(' ','')+'_TotalAndReports_byLocation.pdf')

    
def makeLocationPieChart(ax, data, plotType):
    """ function to condense plot drawing"""
    labels = ['Columbus, OH', 'Greater Ohio', 'Outside OH']
    colors = ['blue', 'green', 'red']
    
    size = data[ plotType ]
    #remove categories with 0
    for item in size:
        if item == 0:
            del labels[size.index(item)]
            del colors[size.index(item)]
            del size[size.index(item)]

    # keep on rolling
    total = sum(size)
    ax.pie(size, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, colors=colors) # shows relative values
    if plotType == 'nContributions':
        ax.text(-0.65, 1.4, '# Of Contributions', fontsize=14)
    elif plotType == 'nRaised':
        ax.text(-0.28, 1.4, '$ Raised', fontsize=14)


def makeLocationTextSummary(ax, data, report='', date=''):
    """ function to condense report summary"""
    ax.axis('off')
    if report =='':
        ax.text(0.3, 0.9, 'All Contributions', fontsize=14, fontweight = 'bold')
    else:
        ax.text(0.3, 0.9, report, fontsize=14, fontweight = 'bold')
    ax.text(0.3, 0.7, '# of Contributions: ' + str(sum(data['nContributions'])), fontsize=14)
    ax.text(0.3, 0.5, 'Total Raised: $'+ str(sum(data['nRaised'])), fontsize=14)
    if date =='':
        ax.text(0.3, 0.3, 'Filing Date:    N/A', fontsize=14)
    else:
        ax.text(0.3, 0.3, 'Filing Date: ' + date, fontsize=14)
