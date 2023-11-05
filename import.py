def tsv_to_dict(file_path):
    result_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into columns using tab as the separator
            columns = line.strip().split('\t')
            
            if len(columns) == 2:
                key, value = columns[1], columns[0]
                result_dict[key] = value
    
    return result_dict