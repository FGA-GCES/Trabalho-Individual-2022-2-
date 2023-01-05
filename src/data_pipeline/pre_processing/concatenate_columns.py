from pandas import DataFrame

def get_concatenated_column(csv, columns, column_name):
    if(type(columns) == str):
        csv[column_name] = csv[columns]
        return DataFrame(csv[column_name])
    
    for value in columns:
        if(not(column_name in csv)):
            csv[column_name] = csv[value].astype(str)
            continue
        
        csv[column_name] = csv[column_name] + ' ' + csv[value].astype(str)
        
    return DataFrame(csv[column_name])
