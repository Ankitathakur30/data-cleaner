import pandas as pd
def profile_data(df):
    profile={}
    profile["shape"]=df.shape
    profile["missing"]=(df.isnull().sum()).to_dict()
    profile["dtypes"]=(df.dtypes.astype(str).to_dict())
    profile["numeric_summary"]=df.describe().to_dict()
    profile["categorical_summary"]={
        col:
        df[col].value_count().head(5).to_head()
        for col in df.select_dtypes(include="object").columns
    }