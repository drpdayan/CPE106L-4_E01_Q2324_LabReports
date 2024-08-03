"""
File: hoopstatsapp.py

The application for analyzing basketball stats.
"""

from hoopstatsview import HoopStatsView
import pandas as pd

def main():
    """Creates the data frame and view and starts the app."""
    frame = pd.read_csv("cleanbrogdonstats.csv")
    newframe = cleanStats(frame)
    HoopStatsView(newframe)

def cleanStats(df):
    for col in ['FG', '3PT', 'FT']:
        # Split the column into two new columns
        df[col + 'M'], df[col + 'A'] = df[col].str.split('/').str
        # Remove the original column
        df = df.drop(col, axis=1)
    return df

if __name__ == "__main__":
    main()
