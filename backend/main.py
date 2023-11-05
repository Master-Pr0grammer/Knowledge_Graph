import categorization as cat
import tree as tree
import anki_tools
import ntpath

topic_structure = {}
tree_data = tree.Knowledge_tree()

def tsv_to_dict(file_path):
    result_dict = {}
    file_name = ntpath.basename(file_path)
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into columns using tab as the separator
            columns = line.strip().split('\t')
            
            if len(columns) == 2:
                key, value = columns[0], columns[1]
                result_dict[key + " - " + value] = [file_name]
    
    return result_dict

# Asks generator to create a new layer of topics
def make_tree_more_specific(json_filename):
    topic_structure = cat.generate_category(topic_structure)
    
    tree_data.create_tree_from_structure(topic_structure)
    tree_data.save_json(json_filename)

# Create an initial tree of categories from an input file
def upload(file_path, json_filename):
    question_dict = tsv_to_dict(file_path)
    topic_structure = cat.generate_category(question_dict)
    
    tree_data = tree.Knowledge_tree()
    tree_data.create_tree_from_structure(topic_structure)
    tree_data.save_json(json_filename)

# ----------\/ using AKNI tools \/----------
def update_scores():
    score_data = anki_tools.get_cards_review_details("DECK NAME HERE")

    #set leaf node scores in tree
    leaf_nodes = []
    tree_data.traverse_tree(tree_data.root, leaf_nodes)
    for leaf in leaf_nodes:
        leaf.score = score_data[leaf.topic_name]['score']
    tree_data.update_scores(tree_data.root)

def build_tree_from_anki():
    #send data to henry's code
    #send henry's code output to Ethan's code
    #done
    pass