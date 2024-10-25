def evaluate_operand(operand, data):
    # This function parses and evaluates the operand
    attribute, operator, value = operand.split()  # e.g., "age > 30"
    attribute_value = data.get(attribute)

    if operator == ">":
        return attribute_value > int(value)
    elif operator == "<":
        return attribute_value < int(value)
    elif operator == "=":
        return attribute_value == value.strip("'")
    return False

def evaluate_rule(node, data):
    # Recursive function to evaluate the rule against data
    if node.node_type == 'operand':
        return evaluate_operand(node.value, data)
    elif node.node_type == 'operator':
        left_result = evaluate_rule(node.left, data)
        right_result = evaluate_rule(node.right, data)
        if node.value == 'AND':
            return left_result and right_result
        elif node.value == 'OR':
            return left_result or right_result
    return False
