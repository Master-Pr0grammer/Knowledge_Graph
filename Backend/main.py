import categorization as cat
import tree

topic_structure = {}

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

# Asks generator to create a new layer of topics
def make_tree_more_specific(json_filename):
    topic_structure = cat.generate_category(topic_structure)
    
    tree_data = tree.Knowledge_tree()
    tree_data.create_tree_from_structure(topic_structure)
    tree_data.save_json(json_filename)

# Create an initial tree of categories from an input file
def upload(file_path, json_filename):
    question_dict = tsv_to_dict(file_path)
    topic_structure = cat.generate_category(question_dict)
    
    tree_data = tree.Knowledge_tree()
    tree_data.create_tree_from_structure(topic_structure)
    tree_data.save_json(json_filename)
    
if __name__ == "__main__":
    upload("text.txt", "json.json")