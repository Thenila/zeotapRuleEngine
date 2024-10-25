import requests

BASE_URL = "http://127.0.0.1:8000"

def create_rule(rule_string):
    response = requests.post(f"{BASE_URL}/create_rule/", json={"rule_string": rule_string})
    print(f"create_rule('{rule_string}') response:", response.json())
    return response.json()

def combine_rules(rules):
    response = requests.post(f"{BASE_URL}/combine_rules/", json={"rules": rules})
    print(f"combine_rules({rules}) response:", response.json())
    return response.json()

def evaluate_rule(rule_ast, data):
    response = requests.post(f"{BASE_URL}/evaluate_rule/", json={"rule_ast": rule_ast, "data": data})
    print(f"evaluate_rule({rule_ast}, {data}) response:", response.json())
    return response.json()

# Test Case 1: Create individual rules
rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
rule2 = "((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"

ast_rule1 = create_rule(rule1)
ast_rule2 = create_rule(rule2)

# Test Case 2: Combine the example rules
combined_ast = combine_rules([rule1, rule2])

# Test Case 3: Evaluate rules with sample JSON data
sample_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 4}
evaluate_rule(ast_rule1, sample_data)
evaluate_rule(ast_rule2, sample_data)

# Explore combining additional rules
additional_rule = "((age < 30 AND department = 'HR')) AND (salary > 30000 OR experience > 2)"
ast_additional_rule = create_rule(additional_rule)
combined_ast = combine_rules([rule1, rule2, additional_rule])
print("Combined AST with additional rule:", combined_ast)

# Evaluate combined rules
evaluate_rule(combined_ast, sample_data)
