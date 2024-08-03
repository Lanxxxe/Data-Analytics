import pandas as pd
import matplotlib.pyplot as plt

# March 19 2020 - Covid 19 start
def filterData(file):
    # Reads the CSV File

    file_Data = pd.read_csv(file)

    # Covert date columns to DateTime Format
    file_Data['Created Date'] = pd.to_datetime(file_Data['Created Date'])
    file_Data['Closed Date'] = pd.to_datetime(file_Data['Closed Date'])   

    file_Data.dropna(subset=['Created Date', 'Complaint Type', 'Agency'], inplace=True)

    covid19_Start = pd.to_datetime('2020-03-01') #First Case of covid 19 in New York

    before_Covid19 = file_Data[file_Data['Created Date'] <= covid19_Start]
    after_Covid19 = file_Data[file_Data['Created Date'] >= covid19_Start]

    return before_Covid19, after_Covid19

def plotRequestOvertime(before, after):
    # Compare the number of service requests before and after COVID-19
    before_counts = before['Created Date'].dt.to_period('M').value_counts().sort_index()
    after_counts = after['Created Date'].dt.to_period('M').value_counts().sort_index()
    
    # print('\nService Requests Before and After COVID-19: \n',before_counts, after_counts)
    # Plot the comparison
    plt.figure(figsize=(14, 7))
    plt.plot(before_counts.index.astype(str), before_counts.values, label='Before COVID-19')
    plt.plot(after_counts.index.astype(str), after_counts.values, label='After COVID-19')
    plt.xlabel('Date')
    plt.ylabel('Number of Requests')
    plt.title('Service Requests Before and After COVID-19')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def barComplaintsOvertime(before, after):
    # Identify common complaint types before and after COVID-19
    before_complaints = before['Complaint Type'].value_counts().head(10)
    after_complaints = after['Complaint Type'].value_counts().head(10)
    
    # print('\nTop 10 Complaint Types Before and After COVID-19: \n', before_complaints, after_complaints)
    # Create a DataFrame for plotting
    complaints_df = pd.DataFrame({
        'Before COVID-19': before_complaints,
        'After COVID-19': after_complaints
    })

    # Plot the common complaint types
    complaints_df.plot(kind='bar', figsize=(14, 7))
    plt.xlabel('Complaint Type')
    plt.ylabel('Number of Requests')
    plt.title('Top 10 Complaint Types Before and After COVID-19')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def agenciesWithHighestRequests(before, after):
    # Identify agencies with the highest number of requests before and after COVID-19
    before_agencies = before['Agency'].value_counts().head(10)
    after_agencies = after['Agency'].value_counts().head(10)

    # print('\nTop 10 Agencies Receive Request Before and After COVID-19: \n', before_agencies, after_agencies)

    # Create a DataFrame for plotting
    agencies_df = pd.DataFrame({
        'Before COVID-19': before_agencies,
        'After COVID-19': after_agencies
    })

    # Plot the top agencies
    agencies_df.plot(kind='bar', figsize=(14, 7))
    plt.xlabel('Agency')
    plt.ylabel('Number of Requests')
    plt.title('Top 10 Agencies Receive Request Before and After COVID-19')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def analyzeAreasByZip(before, after):
    # Analyze which areas (Incident Zip) were receiving the most complaints
    before_zip = before['Incident Zip'].value_counts().head(10)
    after_zip = after['Incident Zip'].value_counts().head(10)

    # print('Top 10 Zip Codes Call a Request Before and After COVID-19:\n', before_zip, after_zip)

    # Create a DataFrame for plotting
    zip_df = pd.DataFrame({
        'Before COVID-19': before_zip,
        'After COVID-19': after_zip
    })

    # Plot the top zips
    zip_df.plot(kind='bar', figsize=(14, 7))
    plt.xlabel('Incident Zip')
    plt.ylabel('Number of Requests')
    plt.title('Top 10 Zip Codes Call a Request Before and After COVID-19')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    covid19_file = './covid19-data.csv'

    before_covid, after_covid = filterData(covid19_file)
    
    # Compare service requests
    plotRequestOvertime(before_covid, after_covid)
    
    # Identify common complaints
    barComplaintsOvertime(before_covid, after_covid)
    
    # Identify top agencies
    agenciesWithHighestRequests(before_covid, after_covid)
    
    # Analyze areas by zip
    analyzeAreasByZip(before_covid, after_covid)



if __name__ == "__main__":
    main()


