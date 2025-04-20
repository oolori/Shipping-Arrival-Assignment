# Inspect columns to see number of rows and check if there any row with missing data
def check_missing_data(data):
    print(data.info())

# This function is to help fill mising cells with median of the columns 
def clean_data(data):
    numeric_columns = data.select_dtypes(include=['number']).columns
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())
    return data