import pandas as pd 


if __name__ == "__main__":
    df = pd.read_excel("./src/output_scale[1-10].xlsx")
    print("number of rows: ", len(df))

    # drop rows with NaN values
    df = df.dropna()
    print("number of rows after dropna: ", len(df))

    # get columns names 
    columns = df.columns
    print("columns: ", columns)