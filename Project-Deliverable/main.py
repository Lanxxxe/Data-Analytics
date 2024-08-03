import pandas as pd
import matplotlib.pyplot as plt
'''
!!! NOTE: This is just a sample analysis code !!!
'''

class Read311Data:
    def __init__(self, path):
        self.path = path

    def loadFile(self):
        file = pd.read_csv(self.path)
        return file

def main():
    # Reads the CSV File
    file = Read311Data('./311data.csv')
    data = file.loadFile()
    # Convert date columns to datetime
    data['created_date'] = pd.to_datetime(data['created_date'])
    data['closed_date'] = pd.to_datetime(data['closed_date'], errors='coerce')
    data['resolution_date'] = pd.to_datetime(data['resolution_date'], errors='coerce')

    # Filter data for Hurricane Sandy period
    preHurricaneData = data[(data['created_date'] >= '2012-09-28') & (data['created_date'] < '2012-10-29')]
    postHurricaneData = data[(data['created_date'] >= '2012-10-29') & (data['created_date'] <= '2012-11-29')]

    # Filter data for COVID-19 period
    preCovidData = data[(data['created_date'] >= '2020-02-01') & (data['created_date'] < '2020-03-22')]
    postCovidData = data[(data['created_date'] >= '2020-03-22') & (data['created_date'] <= '2020-06-01')]

    # Summarize and visualize data
    def summarize_data(df, period):
        if df.empty:
            print(f"No data available for {period}.")
            return

        print(f"Summary for {period}:")
        print(df['complaint_type'].value_counts().head(10))
        df['complaint_type'].value_counts().head(10).plot(kind='bar')
        plt.title(f"Top 10 Complaint Types - {period}")
        plt.show()

    # Summarize and visualize Hurricane Sandy data
    summarize_data(preHurricaneData, 'Before Hurricane Sandy')
    summarize_data(postHurricaneData, 'After Hurricane Sandy')

    # Summarize and visualize COVID-19 data
    summarize_data(preCovidData, 'Before COVID-19 Lockdown')
    summarize_data(postCovidData, 'After COVID-19 Lockdown')


if __name__ == "__main__":
    main()