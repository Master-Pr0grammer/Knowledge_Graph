import ntpath

def tsv_to_dict(file_path):
    result_dict = {}
    file_name = ntpath.basename(file_path)

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into columns using tab as the separator
            columns = line.strip().split('\t')
            
            if len(columns) == 2:
                question, answer = columns[0], columns[1]
                result_dict[question + " - " + answer] = [file_name]
    
    return result_dict