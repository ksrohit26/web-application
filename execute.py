import json
import pandas as pd

def main():
    # Read data.xlsx and convert to CSV
    df = pd.read_excel('data.xlsx')
    df.to_csv('data.csv', index=False)

    # Example processing logic (fix any errors in the original script)
    # ... (additional fixed code if needed)

if __name__ == '__main__':
    main()