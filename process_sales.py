import pandas as pd
import glob
import os

# Path to data folder
data_path = './data'

# Get list of CSV files in the data folder
csv_files = glob.glob(os.path.join(data_path, '*.csv'))

# List to hold dataframes
dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    
    # Filter for Pink Morsel only
    df = df[df['product'] == 'Pink Morsel']
    
    # Calculate Sales = quantity * price
    df['Sales'] = df['quantity'] * df['price']
    
    # Select only Sales, date, region columns
    df_processed = df[['Sales', 'date', 'region']]
    
    dfs.append(df_processed)

# Concatenate all dataframes
combined_df = pd.concat(dfs, ignore_index=True)

# Save to CSV
combined_df.to_csv('processed_sales.csv', index=False)
