import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

'''
Country:
    Singapore
    Iceland
    Germany
'''

# Do not change anything from here
class Gapminder:
    def __init__(self, filePath):
        self.filePath = filePath
    
    def readFile(self):
        gapminderContent = pd.read_csv(self.filePath)
        
        return gapminderContent
    
    def getSingaporeLifeExpectancy(self):
        gapminderData = self.readFile()
        singaporeFilteredData = gapminderData[gapminderData["country"] == "Singapore"]

        return singaporeFilteredData


    def getIcelandLifeExpectancy(self):
        gapminderData = self.readFile()
        icelandFilteredData = gapminderData[gapminderData["country"] == "Iceland"]

        return icelandFilteredData

    def getGermanyLifeExpectancy(self):
        gapminderData = self.readFile()
        germanyFilteredData = gapminderData[gapminderData["country"] == "Germany"]

        return germanyFilteredData
    
    
def main():
    file = Gapminder('./gapminder_dataset.csv') #Replace this with the correct file name and file path of the csv file

    #Get Data from 3 different countries
    singaporeLifeExpectancy = file.getSingaporeLifeExpectancy()
    icelandLifeExpectancy = file.getIcelandLifeExpectancy()
    germanyLifeExpectancy = file.getGermanyLifeExpectancy()

    # Plotting the data
    plt.figure(figsize=(11, 7))

    # Create a line plot for Singapore
    plt.plot(singaporeLifeExpectancy["year"], singaporeLifeExpectancy["life_expectancy"], label='South Korea', marker='8', linestyle='-', color='limegreen')

    # Create a line plot for Iceland
    plt.plot(icelandLifeExpectancy["year"], icelandLifeExpectancy["life_expectancy"], label='Iceland', marker='s', linestyle='--', color='gold')

    # Create a line plot for Germany
    plt.plot(germanyLifeExpectancy["year"], germanyLifeExpectancy["life_expectancy"], label='Germany', marker='*', linestyle='dotted', color='magenta')

    # Add titles and labels
    plt.title('Life Expectancy Over Time')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')

    # Add a legend
    plt.legend(loc='upper left')

    # Add grid lines
    plt.grid(True)

    # Display the plot
    plt.show()

if __name__ == "__main__":
    main()