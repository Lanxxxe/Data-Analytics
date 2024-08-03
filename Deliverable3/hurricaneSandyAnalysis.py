import pandas as pd
import matplotlib.pyplot as plt

# October 22 2012 - November 12 2012
def filterData(file):
    sandy_Data = pd.read_csv(file, index_col='id')

    # Covert date columns to DateTime Format
    sandy_Data['created_date'] = pd.to_datetime(sandy_Data['created_date'])

    # Remove Row that has a NA value of created_date and complaint_type
    sandy_Data.dropna(subset=['created_date', 'complaint_type'], inplace=True)

    # Date when the Hurricane Sandy hit NYC
    hurricane_Sandy_Start = pd.to_datetime('2012-10-22')

    # After Hurricane Sandy hit NYC
    hurricane_Sandy_End = pd.to_datetime('2012-11-2')

    before_Sandy = sandy_Data[(sandy_Data['created_date'] < hurricane_Sandy_Start)]
    after_Sandy = sandy_Data[(sandy_Data['created_date'] > hurricane_Sandy_End)]

    return before_Sandy, after_Sandy

def plotRequestOvertime(before, after):
    # Compare the number of service requests before and after Hurricane Sandy
    before_counts = before['created_date'].dt.to_period('M').value_counts().sort_index()
    after_counts = after['created_date'].dt.to_period('M').value_counts().sort_index()
    
    print('\nService Requests Before and After Hurricane Sandy:\n', before_counts, after_counts)

    # Plot the comparison
    # plt.figure(figsize=(14, 7))
    # plt.plot(before_counts.index.astype(str), before_counts.values, label='Before Hurricane Sandy')
    # plt.plot(after_counts.index.astype(str), after_counts.values, label='After Hurricane Sandy')
    # plt.xlabel('Date')
    # plt.ylabel('Number of Requests')
    # plt.title('Service Requests Before and After Hurricane Sandy')
    # plt.xticks(rotation=45)
    # plt.legend()
    # plt.tight_layout()
    # plt.show()

def barComplaintsOvertime(before, after):
    # Identify common complaint types before and after Hurricane Sandy
    before_complaints = before['complaint_type'].value_counts().head(10)
    after_complaints = after['complaint_type'].value_counts().head(10)
    
    print('\nTop 10 Complaint Types Before and After Hurricane Sandy\n', before_complaints, after_complaints)
    # Create a DataFrame for plotting
    # complaints_df = pd.DataFrame({
    #     'Before Hurricane Sandy': before_complaints,
    #     'After Hurricane Sandy': after_complaints
    # })

    # # Plot the common complaint types
    # complaints_df.plot(kind='bar', figsize=(14, 7))
    # plt.xlabel('Complaint Type')
    # plt.ylabel('Number of Requests')
    # plt.title('Top 10 Complaint Types Before and After Hurricane Sandy')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()


def agenciesWithHighestRequests(before, after):
    # Identify agencies with the highest number of requests before and after Hurricane Sandy
    before_agencies = before['agency'].value_counts().head(10)
    after_agencies = after['agency'].value_counts().head(10)

    print('\nTop 10 Agencies Receive a Request Before and After Hurricane Sandy\n', before_agencies, after_agencies)

    # Create a DataFrame for plotting
    # agencies_df = pd.DataFrame({
    #     'Before Hurricane Sandy': before_agencies,
    #     'After Hurricane Sandy': after_agencies
    # })

    # # Plot the top agencies
    # agencies_df.plot(kind='bar', figsize=(14, 7))
    # plt.xlabel('Agency')
    # plt.ylabel('Number of Requests')
    # plt.title('Top 10 Agencies Receive a Request Before and After Hurricane Sandy')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    plt.show()


def analyzeAreasByCity(before, after):
    # Analyze which areas (Incident Zip) were receiving the most complaints
    before_zip = before['city'].value_counts().head(10)
    after_zip = after['city'].value_counts().head(10)

    print('\nTop 10 City Request a Services Before and After Hurricane Sandy\n', before_zip, after_zip)
    # Create a DataFrame for plotting
    # zip_df = pd.DataFrame({
    #     'Before Hurricane Sandy': before_zip,
    #     'After Hurricane Sandy': after_zip
    # })

    # # Plot the top zips
    # zip_df.plot(kind='bar', figsize=(14, 7))
    # plt.xlabel('City')
    # plt.ylabel('Number of Requests')
    # plt.title('Top 10 City Request a Services Before and After Hurricane Sandy')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

def main():

    # Reads the CSV File
    file_311Data = './311Data.csv'

    before_Sandy, after_Sandy = filterData(file_311Data)
    
    # Compare service requests
    plotRequestOvertime(before_Sandy, after_Sandy)
    
    # Identify common complaints from the people
    barComplaintsOvertime(before_Sandy, after_Sandy)
    
    # Identify top agencies recieve request of service
    agenciesWithHighestRequests(before_Sandy, after_Sandy)
    
    # Analyze areas by City
    analyzeAreasByCity(before_Sandy, after_Sandy)
    


if __name__ == "__main__":
    main()


