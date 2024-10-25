from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Union, Optional

# Create the FastAPI app
app = FastAPI()

# Add a root route to avoid the 404 error on the root URL
@app.get("/")
def read_root():
    return {"message": "Welcome to the Rule Engine API!"}

# Define a Node structure for the AST
class Node(BaseModel):
    type: str  # "operator" for AND/OR, "operand" for condition
    left: Optional['Node'] = None
    right: Optional['Node'] = None
    value: Optional[Union[str, int, float]] = None

# Define the request model for creating rules
class RuleRequest(BaseModel):
    rule_string: str

# Define the request model for combining rules
class CombineRulesRequest(BaseModel):
    rules: List[str]

# Define the request model for evaluating a rule against data
class EvaluateRequest(BaseModel):
    rule_ast: Node
    data: Dict[str, Union[str, int, float]]

# Helper function to convert rule strings to AST (basic parsing, replace this with proper parsing logic)
def create_ast_from_rule(rule_string: str) -> Node:
    if "AND" in rule_string:
        parts = rule_string.split("AND")
        return Node(type="operator", left=Node(type="operand", value=parts[0].strip()), right=Node(type="operand", value=parts[1].strip()), value="AND")
    elif "OR" in rule_string:
        parts = rule_string.split("OR")
        return Node(type="operator", left=Node(type="operand", value=parts[0].strip()), right=Node(type="operand", value=parts[1].strip()), value="OR")
    else:
        return Node(type="operand", value=rule_string.strip())

# Helper function to evaluate AST against data
def evaluate_ast(node: Node, data: Dict[str, Union[str, int, float]]) -> bool:
    if node.type == "operand":
        if ">" in node.value:
            key, threshold = node.value.split(">")
            return data.get(key.strip()) > int(threshold.strip())
        elif "<" in node.value:
            key, threshold = node.value.split("<")
            return data.get(key.strip()) < int(threshold.strip())
        elif "=" in node.value:
            key, value = node.value.split("=")
            return data.get(key.strip()) == value.strip().strip("'")
        else:
            raise ValueError("Invalid operand")
    elif node.type == "operator":
        if node.value == "AND":
            return evaluate_ast(node.left, data) and evaluate_ast(node.right, data)
        elif node.value == "OR":
            return evaluate_ast(node.left, data) or evaluate_ast(node.right, data)
        else:
            raise ValueError("Invalid operator")
    else:
        raise ValueError("Invalid node type")

# API to create a rule (AST)
@app.post("/create_rule/")
def create_rule(rule: RuleRequest):
    try:
        ast = create_ast_from_rule(rule.rule_string)
        return {"ast": ast}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating rule: {str(e)}")

# API to combine multiple rules into a single AST
@app.post("/combine_rules/")
def combine_rules(request: CombineRulesRequest):
    try:
        combined_ast = None
        for rule_string in request.rules:
            ast = create_ast_from_rule(rule_string)
            if combined_ast is None:
                combined_ast = ast
            else:
                combined_ast = Node(type="operator", left=combined_ast, right=ast, value="AND")
        return {"combined_ast": combined_ast}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error combining rules: {str(e)}")

# API to evaluate a rule (AST) against input data
@app.post("/evaluate_rule/")
def evaluate_rule(request: EvaluateRequest):
    try:
        result = evaluate_ast(request.rule_ast, request.data)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error evaluating rule: {str(e)}")
