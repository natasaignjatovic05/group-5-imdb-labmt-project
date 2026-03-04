import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(
        path,
        sep="\t",
        skiprows=2,
        engine="python"
    )

    # Replace "--" with missing values
    df = df.replace("--", pd.NA)

    # Convert numeric columns
    numeric_cols = df.columns[1:]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    return df


if __name__ == "__main__":
    df = load_and_clean("data/raw/Data_Set_S1.txt")

    print("Shape:", df.shape)
    print("\nData types:")
    print(df.dtypes)
    print("\nMissing values:")
    print(df.isna().sum())

    # Save clean dataset
    df.to_csv("data/clean/labMT_clean.csv", index=False)