import pandas as pd

#Column mappings for data normalization
BANK_COLUMN_MAPPINGS = {
    'Chase': {
        'Date': 'Transaction Date',
        'Description': 'Description',
        'Amount': 'Amount',
        'Category': 'Category'
    }

}

# Function to parse CSV files based on bank-specific column mappings
# Ingests a CSV file, applies the appropriate column mappings, and returns a standardized DataFrame
def parse_csv(file_path, bank_name):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error parsing CSV file: {e}")
        return None


