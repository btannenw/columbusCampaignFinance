### Author: Ben Tannenwald
### Date: Oct 11, 2017
### Purpose: class to take restructured JSON format and create members/functions to centralize and streamline data queries

class donorFile(object):
    """A class for candidate donor contribution information.

    Attributes:
        candidate:    the candidate's name
        filings:      the dictionary of all contribution filings
        nReports:     the number of contribution reports filed by a candidate (or their campaign)
        reports:      a list of the names of the filed contribution reports
        totalRaised:  total amount of $ raised by candidate

        printSimpleSummary:  print summary of overview information
        filingDate:          return the filing date of a specified report
        nContributions:      return the number of contributions in a specified report
        nRaised:             return the amount of $ raised by a given report
        returnTotalRaised:   return the total amount of $ raised by candidate
    """

    # members
    
    # Functions
    def __init__(self, name, record):
        """Return a Customer object whose name is *name*.""" 
        self.candidate = name
        self.filings = record
        self.nReports = len(self.filings)
        self.reports = self.filings.keys()
        self.totalRaised = self.returnTotalRaised()
        
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

