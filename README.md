# Trader-Performance-vs-Market-Sentiment-Analysis
📘 Trader Performance vs Market Sentiment Analysis

🔍 Project Overview

This project explores the relationship between Bitcoin market sentiment (Fear & Greed Index) and individual trader performance using real historical trading data. The goal is to analyze how sentiment impacts closed PnL, trading volume, and execution behavior.

🧾 Datasets Used

1. Bitcoin Market Sentiment Dataset (fear_greed_index.csv)

Columns: timestamp, value, classification, date

Classification examples: Fear, Greed, Extreme Fear, Extreme Greed, Neutral



2. Historical Trader Data (historical_data.csv)

Columns include: Account, Execution Price, Size Tokens, Size USD, Side, Timestamp IST, Closed PnL, etc.




🧪 Objectives

Merge trader performance with market sentiment by date

Identify which sentiment leads to better trading outcomes

Calculate metrics like average profit, average execution price, and trade size under each sentiment


🛠 Technologies & Libraries

Python 3.8+

Pandas – for data manipulation

NumPy – for numerical operations

Matplotlib – for future visualizations

Seaborn – for stylized charts


📈 Steps Performed

1. Loaded and cleaned the data


2. Converted date/time formats for proper merging


3. Merged sentiment and trading data on date


4. Dropped rows with missing sentiment classification


5. Grouped trades by sentiment and calculated performance metrics


6. Exported summarized insights to a CSV file



📊 Results Sample

| Sentiment       | Avg Closed PnL | Total Closed PnL | Avg Execution Price | Avg Trade Size USD | Number of Trades |
|----------------|----------------|------------------|---------------------|--------------------|
