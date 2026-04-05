import pandas as pd
def detect_issues(df):
    issues={}
    issues["missing_percent"]=(
        df.isnull().sum()/len(df)*100
    ).to_dict()
    issues["duplicates"]=int(df.duplicated().sum())
    issues["constant_columns"]=[
        col for col in df.columns if df[col].nunique()==1
    ]
    outliers={}
    for col in df.select_dtypes(include="number").columns:
        Q1=df[col].quantile(0.25)
        Q3=df[col].quantile(0.75)
        IQR=Q3-Q1
        outliers[col]=int(((df[col]<Q1-1.5*IQR) | (df[col]>Q3+1.5*IQR)).sum())
    issues["outliers"]=outliers
    return issues