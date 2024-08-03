import pandas as pd
import statsmodels.api as stsm


class Book:
    def __init__(self, csvPath):
        self.path = csvPath

    def readCSV(self):
        bookInformation = pd.read_csv(self.path)
        return bookInformation

def main():
    
    file = Book('./books.csv')
    
    # Datafame
    books = pd.DataFrame(file.readCSV())

    #Set 'bookID' as the index
    books.set_index('bookID', inplace=True)
 
    #Display 5 Rows of the DataFrame
    print("\n\n=============================================\n")
    print("First 5 rows of the DataFrame")
    print("\n=============================================\n")
    print(books.head())

    #Display the number of Rows and Columns in the Dataframe
    print("\n\n=============================================\n")
    print("Number of rows and columns in the Dataframe")
    print("\n=============================================\n")
    print(books.shape)

    #Display the Summarized Data
    print("\n\n=============================================\n")
    print("Summarize Data")
    print("\n=============================================\n")
    print(books.describe())

    #Display the Unique Authors and Most Frequent Author
    print("\n\n=============================================\n")
    print("Number of Unique Authors in the dataset and most Frequent Author")
    print("\n=============================================\n")
    print(books['authors'].describe())

    #Dependent Variable
    dependentVariable = books['average_rating']

    # Combine the independent variables into a single DataFrame
    independentVariables = books[['num_pages', 'ratings_count', 'text_reviews_count']]
    
    # Add a constant to the model (intercept)
    independentVariables = stsm.add_constant(independentVariables)

    # Fit the OLS model
    olsModel = stsm.OLS(dependentVariable, independentVariables).fit()

    # Display the Summry of OLS Regression
    print("\n\n=================================================================\n\n")
    print(olsModel.summary())
    
if __name__ == "__main__" :
    main()