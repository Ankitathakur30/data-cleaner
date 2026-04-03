import pandas as pd
def clean_data(df):
    report={}
    before=len(df)
    df=df.drop_duplicates()
    report["duplicates_removed"]=before-len(df)
    for col in df.select_dtypes(include="number").columns:
        missing_count=df[col].isnull().sum()
        if missing_count>0:
            median_val=df[col].median()
            df[col]=df[col].fillna(median_val)
            report[f"{col}_filled_with_median"]=int(missing_count)

    for col in df.select_dtypes(include="object").columns:
        missing_count=df[col].isnull().sum()
        if missing_count>0:
            mode_val=df[col].mode()[0]
            df[col]=df[col].fillna(mode_val)
            report[f"{col}_filled_with_mode"]=int(missing_count)

    for col in df.select_dtypes(include="object").columns:
        df[col]=df[col].str.strip().str.lower()
        report[f"{col}_standardized"]=True
    constant_cols=[col for col in df.columns if df[col].nunique()==1]
    df=df.drop(columns=constant_cols)
    report["constant_columns_removed"]=constant_cols
    return df,report