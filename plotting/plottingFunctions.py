### Author: Ben Tannenwald
### Date: Oct 12, 2017
### Purpose: file to store useful functions for plotting contribution information

import operator, numpy as np, datetime as dt
import matplotlib.pyplot as plt, matplotlib.dates as date2num
from matplotlib.gridspec import GridSpec


def makeTotalAndAllReportByTime(candidateFile):
    """function for making plot showing total contributions as function of time"""

    amountsByTime_all, datesByTime_all = candidateFile.returnAmountValuesWithTime()
    amountsByTime_pre, datesByTime_pre = candidateFile.returnAmountValuesWithTime('Pre Primary')

    x = [dt.datetime.strptime(d,'%Y/%m/%d').date() for d in datesByTime_all]
    y = [value for value in amountsByTime_all]
    fig = plt.figure( candidateFile.candidate.replace(' ','')+'_byTime')
    plt.title(candidateFile.candidate+': '+'All Contributions', fontsize=18, fontweight='bold')
    plt.ylabel("Amount Raised [$]", fontsize=18)
    plt.xlabel("Date", fontsize=15)
    
    graph = fig.add_subplot(111)
    graph.plot(x,y,'r-o')
    graph.set_xticklabels( [ date.strftime("%m/%d/%Y") for date in x] )
    fig.autofmt_xdate()
    plt.show()
    

    
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
