import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def makeTotalPrePrimaryPostPrimaryPlot(candidateFile):
    """function for producing complicated pie chart"""
    location_all = candidateFile.returnContributionLocations()
    location_pre = candidateFile.returnContributionLocations('Pre Primary')
    location_post = candidateFile.returnContributionLocations('Post Primary')


    fig = plt.figure(figsize=(14,16))
    #fig = plt.figure()
    fig.suptitle(candidateFile.candidate, fontsize=20, fontweight='bold')
    the_grid = GridSpec(3, 3)
    #the_grid.update(left=0.05, right=1.2, wspace=0.1)
    labels = ['Columbus, OH', 'Greater Ohio', 'Outside OH']
    
    # *** A. First row
    # ** I. First row, first column
    ax1 = plt.subplot(the_grid[0, 0], aspect=1)
    #ax1.set_title('JasmineAyres')
    #plt.subplot.title('Jasmine Ayres', fontsize=16, fontweight='bold')
    size_contrib = location_all['nContributions']
    total_contrib = sum(size_contrib)
    plt.pie(size_contrib, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90) # shows relative values
    plt.text(-0.65, 1.2, '# Of Contributions', fontsize=14)
    
    # ** II. First row, second column
    plt.subplot(the_grid[0, 1], aspect=1)
    size_cash = location_all['nRaised']
    total_cash = sum(size_cash)
    plt.pie(size_cash, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90) # shows relative values
    plt.text(-0.28, 1.2, '$ Raised', fontsize=14)
    
    # ** III. First row, third column
    plt.subplot(the_grid[0, 2], aspect=0.7)
    plt.axis('off')
    plt.text(0.3, 0.9, 'All Contributions', fontsize=14, fontweight = 'bold')
    plt.text(0.3, 0.7, '# of Contributions: ' + str(sum(size_contrib)), fontsize=14)
    plt.text(0.3, 0.5, 'Total Raised: $'+ str(sum(size_cash)), fontsize=14)
    plt.text(0.3, 0.3, 'Filing Date:    N/A', fontsize=14)
    
    # *** B. Second row
    # ** I. Second row, first column
    plt.subplot(the_grid[1, 0], aspect=1)
    size_contrib = location_pre['nContributions']
    total_contrib = sum(size_contrib)
    plt.pie(size_contrib, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90) # shows relative values
    plt.text(-0.65, 1.2, '# Of Contributions', fontsize=14)
    
    # ** II. Second row, second column
    plt.subplot(the_grid[1, 1], aspect=1)
    size_cash = location_pre['nRaised']
    total_cash = sum(size_cash)
    plt.pie(size_cash, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90) # shows relative values
    plt.text(-0.28, 1.2, '$ Raised', fontsize=14)
    
    # ** III. Second row, third column
    plt.subplot(the_grid[1, 2], aspect=0.7)
    plt.axis('off')
    plt.text(0.3, 0.9, 'Pre Primary', fontsize=14, fontweight = 'bold')
    plt.text(0.3, 0.7, '# of Contributions: ' + str(sum(size_contrib)), fontsize=14)
    plt.text(0.3, 0.5, 'Total Raised: $'+ str(sum(size_cash)), fontsize=14)
    plt.text(0.3, 0.3, 'Filing Date: ' + candidateFile.filings['Pre Primary']['filingDate'], fontsize=14)
    
    
    # *** B. Third row
    # ** I. Third row, first column
    plt.subplot(the_grid[2, 0], aspect=1)
    size_contrib = location_post['nContributions']
    total_contrib = sum(size_contrib)
    plt.pie(size_contrib, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90) # shows relative values
    plt.text(-0.65, 1.2, '# Of Contributions', fontsize=14)
    
    # ** II. Third row, second column
    plt.subplot(the_grid[2, 1], aspect=1)
    size_cash = location_post['nRaised']
    total_cash = sum(size_cash)
    plt.pie(size_cash, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90) # shows relative values
    plt.text(-0.28, 1.2, '$ Raised', fontsize=14)
    
    # ** III. Second row, third column
    plt.subplot(the_grid[2, 2], aspect=0.7)
    plt.axis('off')
    plt.text(0.3, 0.9, 'Post Primary', fontsize=14, fontweight = 'bold')
    plt.text(0.3, 0.7, '# of Contributions: ' + str(sum(size_contrib)), fontsize=14)
    plt.text(0.3, 0.5, 'Total Raised: $'+ str(sum(size_cash)), fontsize=14)
    plt.text(0.3, 0.3, 'Filing Date: ' + candidateFile.filings['Post Primary']['filingDate'], fontsize=14)

    fig.savefig( candidateFile.candidate.replace(' ','')+'_Total-PrePrimary-PostPrimary_byLocation.png')
    fig.savefig( candidateFile.candidate.replace(' ','')+'_Total-PrePrimary-PostPrimary_byLocation.pdf')
    
    
def makeLocationPieChart(info, category, text):
    """function for producing pie chart"""
        
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = ['Columbus, OH', 'Greater Ohio', 'Outside OH']
    sizes = info[category]
    total = sum(sizes)
    #explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice 

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90) # shows relative values
    #ax1.pie(sizes, labels=labels, autopct=lambda p: '{:.0f}'.format(p * total / 100), shadow=False, startangle=90) # shows absolute values
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.text(-1.6, 1.1, text, fontsize=16)
    
    #plt.show()
    return ax1
   
