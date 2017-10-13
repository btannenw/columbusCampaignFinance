### Author: Ben Tannenwald
### Date: Oct 11, 2017
### Purpose: class to take restructured JSON format and create members/functions to centralize and streamline data queries

import operator

class donorFile(object):
    """A class for candidate donor contribution information.

    Attributes:
        candidate:           the candidate's name
        filings:             the dictionary of all contribution filings
        nReports:            the number of contribution reports filed by a candidate (or their campaign)
        reports:             a list of the names of the filed contribution reports
        totalRaised:         total amount of $ raised by candidate
        totalContributions:  total number of contributions raised by candidate
        orderedReports:      list of time-ordered reports

        printSimpleSummary:          print summary of overview information
        filingDate:                  return the filing date of a specified report
        nContributions:              return the number of contributions in a specified report
        nRaised:                     return the amount of $ raised by a given report
        orderReportsByFiling:        create and store list of reports ordered by filing date
        returnTotalRaised:           return the total amount of $ raised by candidate
        returnTotalContributions:    returns total number of contributions raised by candidate
        returnAmountValues:          return list of value of all campaign contributions
        returnAmountValuesWithTime:  return list of value of all campaign contributions with time stamp
    """

    # Members
    
    # Functions
    def __init__(self, name, record):
        self.candidate = name
        self.filings = record
        self.nReports = len(self.filings)
        self.reports = self.filings.keys()
        self.totalRaised = self.returnTotalRaised()
        self.orderedReports = self.orderReportsByFiling()
        self.totalContributions = self.returnTotalContributions()
        
    def printSimpleSummary(self):
        """function for printing simple summary to screen"""
        print self.candidate, "filed", self.nReports, 'reports for a total of', self.totalRaised
        for r in self.reports:
            print '\t', r, '(filed', self.filingDate(r), ') has', self.nContributions(r), 'contributions for a total of $', self.nRaised(r)
        
    def filingDate(self, reportName):
        """function for returning filing date of <reportName>"""
        return self.filings[reportName]['filingDate']

    def nContributions(self, reportName):
        """function for returning number of contributions in <reportName>"""
        return len(self.filings[reportName]['contributions'])

    def nRaised(self, reportName):
        """function for returning amount raised in <reportName>"""
        total = 0
 
        for contribution in self.filings[reportName]['contributions']:
            #print contribution['donor'], 'gave', contribution['amount']
            total = total + float(contribution['amount'].strip('$').replace(',',''))
            
        return total

    def returnTotalRaised(self):
        """function for returning amount total amount raised by candidate"""
        total = 0

        for r in self.reports:
            total = total + self.nRaised(r)

        return total

    def returnTotalContributions(self):
        """function for returning amount total number of contributions raised by candidate"""
        total = 0

        for r in self.reports:
            total = total + self.nContributions(r)

        return total


    def returnContributionLocations(self, reportName=''):
        """function for returning list of contribution locations and either total $ or total # contributions. Can be for summary for candidate or single report. Three categories for the moment: 0) Columbus, 1) Elsewhere in Ohio, 2) Non-Ohio"""
        
        # make lists,  0) Columbus, 1) Elsewhere in Ohio, 2) Non-Ohio
        countContributions = [0,0,0]
        countDonations = [0,0,0]

        # first do case when report specified
        if reportName != '':
            for contribution in self.filings[reportName]['contributions']:
                donation = float(contribution['amount'].strip('$').replace(',',''))
                inOhio = ', oh' in contribution['town'].lower()
                inColumbus = 'columbus' in contribution['town'].lower() or 'cols,' in contribution['town'].lower()

                # fill lists by criteria
                if inOhio and inColumbus:
                    countContributions[0] = countContributions[0] + 1
                    countDonations[0] = countDonations[0] + donation
                elif inOhio and not inColumbus:
                    countContributions[1] = countContributions[1] + 1
                    countDonations[1] = countDonations[1] + donation
                else:
                    countContributions[2] = countContributions[2] + 1
                    countDonations[2] = countDonations[2] + donation

        # second do case when report un-specified, i.e. candidate total
        else:
            for r in self.reports:
                for contribution in self.filings[r]['contributions']:
                    donation = float(contribution['amount'].strip('$').replace(',',''))
                    inOhio = ', oh' in contribution['town'].lower()
                    inColumbus = 'columbus' in contribution['town'].lower()  or 'cols,' in contribution['town'].lower()
                    
                    # fill lists by criteria
                    if inOhio and inColumbus:
                        countContributions[0] = countContributions[0] + 1
                        countDonations[0] = countDonations[0] + donation
                    elif inOhio and not inColumbus:
                        countContributions[1] = countContributions[1] + 1
                        countDonations[1] = countDonations[1] + donation
                    else:
                        countContributions[2] = countContributions[2] + 1
                        countDonations[2] = countDonations[2] + donation

        # dictionary to return
        locationDict = {'nContributions': countContributions, 'nRaised': countDonations}
        return locationDict

    
    def returnAmountValues(self, reportName=''):
        """function for returning list of the value of all contributions. Can be for candidate summary or single report."""
        amount_values = []

        # report specified
        if reportName != '':
            for contribution in self.filings[reportName]['contributions']:
                amount_values.append( float(contribution['amount'].strip('$').replace(',','')) )
        # run over all reports
        else: 
            for r in self.reports:
                for contribution in self.filings[r]['contributions']:
                    amount_values.append( float(contribution['amount'].strip('$').replace(',','')) )

        return amount_values


    def returnAmountValuesWithTime(self, reportName=''):
        """function for returning list of the value of all contributions. Can be for candidate summary or single report."""
        amount_values = {}

        # report specified
        if reportName != '':
            for contribution in self.filings[reportName]['contributions']:
                date = contribution['date'].split('/')[2] + '/' + contribution['date'].split('/')[0] + '/' + contribution['date'].split('/')[1]
                if date not in amount_values.keys():
                    amount_values[date] = float(contribution['amount'].strip('$').replace(',',''))
                else:
                    amount_values[date] = amount_values[date] + float(contribution['amount'].strip('$').replace(',',''))
        # run over all reports
        else: 
            for r in self.reports:
                for contribution in self.filings[r]['contributions']:
                    date = contribution['date'].split('/')[2] + '/' + contribution['date'].split('/')[0] + '/' + contribution['date'].split('/')[1]
                    if date not in amount_values.keys():
                        amount_values[date] = float(contribution['amount'].strip('$').replace(',',''))
                    else:
                        amount_values[date] = amount_values[date] + float(contribution['amount'].strip('$').replace(',',''))

        # time order reports
        amount_values = self.orderReportsByFiling(amount_values) # only returns dates. Need to add values !!!!! HEY
        
        return amount_values

                                         
    def orderReportsByFiling(self, inDict={}):
        """function to create and store list of reports ordered by filing date"""
        # *** B. Blunt force approach to ordering reports by date
        date_list = {}
        # **  loop over reports  ** 
        if not bool(inDict):
            for report in self.reports:
                date_raw = self.filings[report]['filingDate']
                date_list[report] = date_raw.split('/')[2] + '/' + date_raw.split('/')[0] + '/' + date_raw.split('/')[1]
        else:
            date_list=inDict
            
        # **  order reports  ** 
        sorted_dates = sorted(date_list.items(), key=operator.itemgetter(1))
        # **  make proper list ** 
        ordered_dates = []
        for tup in sorted_dates:
            ordered_dates.append(tup[0])

        return ordered_dates

