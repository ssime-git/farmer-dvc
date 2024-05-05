import pandas as pd

def load_data(filepath):
    """Load the dataset into a pandas DataFrame."""
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"The file {filepath} was not found.")
        return None

def drop_features(df, drop_list):
    """Drop specified features from the DataFrame."""
    return df.drop(columns=drop_list)

def convert_to_numeric(df, non_numeric_cols):
    """Convert non-numeric columns to numeric using factorization."""
    for col in non_numeric_cols:
        df[col], _ = pd.factorize(df[col])
    return df

def main():
    data_raw_filepath = "data/data_raw.csv"
    data_processed_filepath = "data/data_processed.csv"

    # Load the data
    df = load_data(data_raw_filepath)
    if df is None:
        return

    all_features = df.columns

    # Specify features to drop
    names = [feat for feat in all_features if "net_name" in feat]
    useless = ["info_gew", "info_resul", "interviewtime", "id", "date"]
    practice_list = ["legum", "conc", "add", "lact", "breed", "covman", "comp", "drag", "cov", "plow", "solar", "biog", "ecodr"]
    
    drop_list = names + useless + [feat for feat in all_features if any(x in feat for x in practice_list)]

    # Drop the specified features
    df = drop_features(df, drop_list)

    # Convert non-numeric features to numeric
    non_numeric_cols = list(df.select_dtypes(include=['O']).columns)
    df = convert_to_numeric(df, non_numeric_cols)

    # Save the processed data
    df.to_csv(data_processed_filepath)

if __name__ == '__main__':
    main()
