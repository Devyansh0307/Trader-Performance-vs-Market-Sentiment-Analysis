# 📊 Trader Performance vs Market Sentiment Analysis in Python

# ✅ Step 1: Import required libraries

import pandas as pd 

import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

# ✅ Step 2: Load the datasets

fear_greed_df = pd.read_csv("fear_greed_index.csv")
historical_data_df = pd.read_csv("historical_data.csv")

# ✅ Step 3: Convert timestamp/date columns to datetime

historical_data_df['Timestamp IST'] = pd.to_datetime(historical_data_df['Timestamp IST'], format="%d-%m-%Y %H:%M") 
fear_greed_df['date'] = pd.to_datetime(fear_greed_df['date'])

# ✅ Step 4: Extract date (without time) to align both datasets

historical_data_df['date'] = historical_data_df['Timestamp IST'].dt.date 
fear_greed_df['date'] = fear_greed_df['date'].dt.date

# ✅ Step 5: Merge trader data with sentiment classification

merged_df = pd.merge(historical_data_df, fear_greed_df[['date', 'classification']], on='date', how='left')

# ✅ Step 6: Drop rows with missing sentiment classification

cleaned_df = merged_df.dropna(subset=['classification'])

# ✅ Step 7: Analyze performance grouped by sentiment

performance_by_sentiment = cleaned_df.groupby('classification').agg({ 'Closed PnL': ['mean', 'sum'], 'Execution Price': 'mean', 'Size USD': 'mean', 'Account': 'count'  # number of trades
                                                                      })

# ✅ Step 8: Rename columns for clarity

performance_by_sentiment.columns = [ 'Avg Closed PnL', 'Total Closed PnL', 'Avg Execution Price', 'Avg Trade Size USD', 'Number of Trades' ]

# ✅ Step 9: Sort sentiment types alphabetically

performance_by_sentiment = performance_by_sentiment.sort_index()

# ✅ Step 10: Display results

print("\n=== Trader Performance by Market Sentiment ===\n") 
print(performance_by_sentiment)

# ✅ Optional: Save result to CSV (for reporting or dashboard use)

performance_by_sentiment.to_csv("sentiment_vs_performance_summary.csv")