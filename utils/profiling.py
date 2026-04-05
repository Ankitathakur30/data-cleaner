import pandas as pd
def profile_data(df):
    profile={}
    profile["shape"]=df.shape
    profile["missing"]=(df.isnull().sum()).to_dict()
    profile["dtypes"]=(df.dtypes.astype(str).to_dict())
    if len(df.select_dtypes(include="number").columns) > 0:
        profile["numeric_summary"] = df.describe().to_dict()
    else:
        profile["numeric_summary"] = {}
    profile["categorical_summary"]={
        col:
        df[col].value_counts().head(5).to_dict()
        for col in df.select_dtypes(include="object").columns
    }
    return profile