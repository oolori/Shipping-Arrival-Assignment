def describe_data(data):
    return data.describe()

# Dynamic aggregation function
def aggregate_data(data, column_1, column_2):
    return data.groupby(column_1)[column_2].mean()