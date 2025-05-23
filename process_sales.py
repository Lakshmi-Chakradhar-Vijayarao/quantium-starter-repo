import pandas as pd
import glob
import os

# Path to data folder containing your raw CSV files
data_path = './data'

# Get list of CSV files in the data folder
csv_files = glob.glob(os.path.join(data_path, '*.csv'))

# List to hold processed dataframes
dfs = []

for file in csv_files:
    df = pd.read_csv(file)
    
    # Filter for pink morsel only (case insensitive)
    df = df[df['product'].str.lower() == 'pink morsel']
    
    # Remove $ from price and convert to float
    df['price'] = df['price'].str.replace('$', '').astype(float)
    
    # Calculate Sales = quantity * price
    df['Sales'] = df['quantity'] * df['price']
    
    # Select only Sales, date, region columns
    df_processed = df[['Sales', 'date', 'region']]
    
    dfs.append(df_processed)

# Concatenate all dataframes
combined_df = pd.concat(dfs, ignore_index=True)

# Ensure output folder exists and save processed CSV
os.makedirs('processed', exist_ok=True)
combined_df.to_csv('processed/pink_morsel_sales.csv', index=False)
