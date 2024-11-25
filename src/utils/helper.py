import pandas as pd


def insert_column_variable(column_name, csv="data/master.csv"):
    try:
        df = pd.read_csv(csv)
        df[column_name] = None
        df.to_csv(csv, index=False)
    except Exception as e:
        print(f"Exception occured: {str(e)}")

if __name__ == "__main__":
    insert_column_variable("full_name")