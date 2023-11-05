class Node:
    def __init__(self, topic_name, score=0):
        self.topic_name = topic_name
        self.score = score
        self.connected_nodes = []

class Knowledge_tree:

    def __init__(self, tree_name, topic_name):
        self.tree_name = tree_name
        self.root = Node(topic_name)

    def create_tree_from_structure(structure):
        '''
        question1 : [topic, sub_topic, sub_sub_topic ...]
        question2 : [topic, sub_topic, sub_sub_topic ...]
        question3 : [topic, sub_topic, sub_sub_topic ...]
        
        '''

    #Traverse tree to find all leaf nodes (to edit scores and other data)
    def traverse_tree(self, node, leaf_nodes):
        '''
        Traverses the tree starting at the leaf node and edits the list to add all of the leaf nodes

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
        Traverses the tree starting at the leaf node, and updates all of the higher level catagory (higher nodes) scores

        Input:
            node: the start node of the search (ussually the root node)

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
    example_tree= Knowledge_tree("Example Tree", "Machine Learning")

    #create first level groups
    new_node = Node("Linear Regresssion")
    example_tree.root.connected_nodes.append(new_node)

    new_node = Node("Neural Networks")
    example_tree.root.connected_nodes.append(new_node)
    
    #create base level node
    leaf_node = Node("Linear algebra", 0.3)
    example_tree.root.connected_nodes[0].connected_nodes.append(leaf_node)

    leaf_node = Node("Forward Propragation", 0.7)
    example_tree.root.connected_nodes[1].connected_nodes.append(leaf_node)

    leaf_node = Node("Backward Propragation", 0.6)
    example_tree.root.connected_nodes[1].connected_nodes.append(leaf_node)

    print("\n----- Print Tree -----")
    example_tree.print_tree(example_tree.root, 0)
    #update Scores 

    print("\n----- Print Updated Tree -----")
    example_tree.update_scores(example_tree.root)
    example_tree.print_tree(example_tree.root, 0)

    all_leaf_nodes = []
    example_tree.traverse_tree(example_tree.root, all_leaf_nodes)

    print("\n----- Print Leaf Nodes -----")
    for i in all_leaf_nodes:
        print(i.topic_name)

