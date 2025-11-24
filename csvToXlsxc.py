import pandas as pd 

def replaceChartAndModificateData(drive:pd.DataFrame , nameColum:str , charofreplace:str , charReplace:str):
    """
    Replaces characters in the specified DataFrame column and converts it to a date (dayfirst=True).
    If inplace=True, modifies the original DataFrame; if False, returns a modified copy.
    """
    drive[f'{nameColum}'] = drive[f'{nameColum}'].astype(str).str.replace(charofreplace,charReplace)
    drive[f'{nameColum}'] = pd.to_datetime(drive[f'{nameColum}'] , dayfirst=True ).dt.date

df = pd.read_csv('ecommerce_dataset_10000.csv')

replaceChartAndModificateData(df , 'order_date', '-', '/')

replaceChartAndModificateData(df , 'signup_date', '-' , '/')

df.to_excel('ecommerce_dataset_10000.xlsx' , index=False)