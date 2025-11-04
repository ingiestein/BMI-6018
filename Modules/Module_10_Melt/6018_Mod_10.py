import numpy as np
import pandas as pd

def load_db():
    # Loads the database for usage from the csv file.
    data = pd.read_csv("./diabetes+130-us+hospitals+for+years+1999-2008/diabetic_data.csv")
    return data

def db_melt(df:pd.DataFrame):
    """
    :param df: Dataframe object
    :return:
    takes a dataframe from our specific data set, melts
    """

    # melt ID column is patient_nbr, rename variable to Attribute, and value to Valu
    df_melted = df.melt(id_vars=["patient_nbr"], var_name="Attribute", value_name="Value")
    # Print melted dataframe
    print(df_melted)

def db_pivot(df:pd.DataFrame):
    #  pivot with encounter_id as axis, columns race, and gender as the value.
    df_pivoted = df.pivot(index='encounter_id', columns='race', values="gender")
    print("Pivoted DF")
    #  fill all NaN with 0
    print(df_pivoted.fillna(0))

def db_aggregation(df:pd.DataFrame):
    # Create a mask of only the numeric columns
    numeric_cols = df.select_dtypes(include=np.number).columns
    # Make it so we can see all the columns
    pd.set_option('display.max_columns', None)

    # print the DF with the mask, aggregating all the numbers by mean, std, min, max
    print(df[numeric_cols].agg(['mean', 'std', 'min', 'max']))

def db_itter(df:pd.DataFrame):
    # Iterate through all the time in hospital rows, add if stay is long. it's slow with itteration
    numeric_cols = df.select_dtypes(np.number).columns
    long_stays = 0
    #iterate each row, manually summing.
    for id, row in df[numeric_cols].iterrows():
        if row["time_in_hospital"]>10:
            long_stays += 1
    print("\nLong Stays: ", long_stays)

    # Faster sum
    long = (df["time_in_hospital"] > 10).sum()
    print("\nFast Sum: ", long)

def db_groupby(df:pd.DataFrame):
    #group the DF by gender, then select just the first entry of each to display/print
    print(df.groupby("gender").first())


if __name__ == "__main__":
    data = load_db()

    # print raw DF for comparison
    print("Unchanged DataFrame")
    print(data)

    #reduce the number of columns we're looking at.
    #run melt
    sliced = data[["patient_nbr","race","gender","admission_type_id"]]
    db_melt(sliced)

    # run the pivot function
    db_pivot(data)

    # run agg function
    db_aggregation(data)

    # run iterrows
    db_itter(data)

    # run groupby
    db_groupby(data)



