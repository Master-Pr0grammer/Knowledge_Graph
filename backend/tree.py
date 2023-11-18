import json

class Node:
    '''
    Node class Used for building the tree

    Constructor input:
        topic_name: name of of the topic for the node
        score: knowledge score for the topic
    '''

    def __init__(self, topic_name, score=0):
        self.topic_name = topic_name
        self.score = score
        self.connected_nodes = []

    # is equal operator ('==')
    def __eq__(self, object):
        return self.topic_name == object.topic_name and self.score == object.score
    
    # Returns dictionary conataining all node data
    def get_dict(self):
        node_dict = {
            'name': self.topic_name,
            'score': self.score,
            'nodes': []
        }
        return node_dict

class Knowledge_tree:

    def __init__(self):
        self.root = Node('temp root')

    #build tree from topics
    def create_tree_from_structure(self,structure):
        '''
        Takes in a dictionary output (from AI) and generates a tree structure

        Dictionary format Example:
            question1 : [topic, sub_topic, sub_sub_topic ...]
            question2 : [topic, sub_topic, sub_sub_topic ...]
            question3 : [topic, sub_topic, sub_sub_topic ...]
        '''

        keys = list(structure.keys())
        self.root = Node(structure[keys[0]][0])

        # Itterate over all base level topics/questions
        for i in range(len(keys)):
            branch = self.root

            #for every base level topic, itterate over every sub_topic, and add brach to root (ignoring first, root, element in list)
            for j in range(1,len(structure[keys[i]])):
                current_node = Node(structure[keys[i]][j])

                # add sub topic to current branch if its not already there
                if current_node in branch.connected_nodes:
                    branch = branch.connected_nodes[branch.connected_nodes.index(current_node)] #set branch pointer to pre-existing branch with same name
                else:
                    branch.connected_nodes.append(current_node)
                    branch = branch.connected_nodes[-1]
                    
            current_node = Node(keys[i])
            branch.connected_nodes.append(current_node)

    #recursive function to build a dictionary object representation of the tree
    def export_structure(self, node):
        '''
        Generates a dictionary that recursivly represents the structure of the tree

        Input:
            Starting node for the export (ussually the root node)

        Output:
            Dictionary tree representation
        '''

        if len(node.connected_nodes) == 0:
            return node.get_dict()
        else:
            temp_dict = node.get_dict()
            for i in range(len(node.connected_nodes)):
                var = self.export_structure(node.connected_nodes[i])
                temp_dict['nodes'].append(var)

            dictionary = temp_dict

        return dictionary
    
    #saves dictionary structure to json file
    def save_json(self, filename):
        '''
        Creates a tree structure JSON file in the format defined by the "export_structure" function

        Input:
            filename: filename of the JSON file

        Output:
            JSON file written to current working directory named "filename"
        '''
        dictionary = self.export_structure(self.root)
        file = open(filename, 'w')
        json.dump(dictionary, file)
        file.close()



    #Traverse tree to find all leaf nodes (to edit scores and other data)
    def traverse_tree(self, node, leaf_nodes):
        '''
        Traverses the tree starting at the specified node, and edits the leaf node list to add all of the leaf nodes.
        
        Useful for setting the scores for all of the base topics that are in the base, or leaf nodes, of the tree, then calling "update_scores" 
        function to update all of the higher level node scores.

        Input:
            node: the start node of the search (ussually the root node)
            leaf_nodes: empty list ([])

        Output:
            None: edits leaf_nodes list, and adds all leaf nodes found
        '''

        #Base case if leaf node
        if len(node.connected_nodes) == 0:
            leaf_nodes.append(node)
            return node
        
        else:
            for i in range(len(node.connected_nodes)):
                self.traverse_tree(node.connected_nodes[i], leaf_nodes)
        

    def update_scores(self, node):
        '''
        Traverses the tree starting at the specified node, and updates all of the higher level catagory (higher nodes) scores

        Input:
            node: the start node of the update scores function (ussually the root node)

        Output:
            None: updates all node scores
        '''

        #Base case if leaf node
        if len(node.connected_nodes) == 0:
            return node.score
        
        else:
            score_sum = 0
            for i in range(len(node.connected_nodes)):
                score_sum += self.update_scores(node.connected_nodes[i])
            average_score = score_sum / len(node.connected_nodes)

            #update current node score
            node.score = average_score
            return average_score
        
    #print tree for debugging
    def print_tree(self, node, layer):
        print('\t'*layer,f'{node.topic_name}, Score: {round(node.score, 2)}')

        #Base case if leaf node
        if len(node.connected_nodes) == 0:
            return
        
        else:
            for i in range(len(node.connected_nodes)):
                self.print_tree(node.connected_nodes[i], layer+1)
        


#test code
if __name__ == '__main__':
    example_tree= Knowledge_tree()

    # ----- Example structure for creating tree -----
    structure = {
        'question1':['Machine Learning', 'Linear Regression'],
        'question2':['Machine Learning', 'Neural Networks'],
        'question3':['Machine Learning', 'Neural Networks'],
    }
    example_tree.create_tree_from_structure(structure)

    # ----- Print Tree -----
    print("\n----- Print Tree -----")
    example_tree.print_tree(example_tree.root, 0)

    # ----- Get leaf Nodes -----
    print("\n----- Print Leaf Nodes -----")
    all_leaf_nodes = []
    example_tree.traverse_tree(example_tree.root, all_leaf_nodes)
    for i in all_leaf_nodes:
        print(i.topic_name)

    #----- Update leaf nodes with scores -----
    for node in all_leaf_nodes:
        node.score = 0.3
    
    #----- Update Tree Scores -----
    print("\n----- Print Updated Tree -----")
    example_tree.update_scores(example_tree.root)
    example_tree.print_tree(example_tree.root, 0)

    #----- Export Structure as dictionary -----
    print("\n----- Print Export Structure -----")
    structure = example_tree.export_structure(example_tree.root)
    print(structure)
    #example_tree.save_structure('test.json')