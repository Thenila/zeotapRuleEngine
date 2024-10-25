class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # 'operator' or 'operand'
        self.left = left
        self.right = right
        self.value = value

    def __repr__(self):
        return f"Node(type={self.node_type}, value={self.value})"

# Function to create an AST from a rule string (this can be extended with a parser)
def create_rule(rule_string):
    # A simplified version that returns a dummy AST for now
    # You would expand this by parsing the rule string into tokens and constructing the AST
    root = Node("operator", value="AND")
    root.left = Node("operand", value="age > 30")
    root.right = Node("operand", value="salary > 50000")
    return root
