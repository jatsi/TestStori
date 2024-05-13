import pandas as pd
from datetime import datetime

def process_transactions(path: str) -> dict:
    """
    Process transaction data from a CSV file.
    
    Args:
        path (str): The path to the CSV file containing transaction data.
    
    Returns:
        dict: A dictionary containing summary information about the transactions.
    """
    # Read CSV file into a DataFrame
    df = pd.read_csv(path)
    
    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format="%m/%d")
    
    # Extract month from 'Date' column
    df['Month'] = df['Date'].dt.strftime('%B')

    # Separate credit and debit transactions
    credits = df[df["Transaction"] > 0]
    debits = df[df["Transaction"] < 0]

    # Calculate total balance, transactions by month, and average credit and debit amounts
    results = {
        "total_balance": df["Transaction"].sum(),
        "transactions_by_month": df.groupby("Month").size().to_dict(),
        "average_credit": credits["Transaction"].mean(),
        "average_debit": debits["Transaction"].mean()
    }
    
    return results
