// Base URL for the backend API
const BASE_URL = "http://127.0.0.1:8000";

// DOM Elements
const createRuleBtn = document.getElementById('createRuleBtn');
const combineRulesBtn = document.getElementById('combineRulesBtn');
const evaluateRuleBtn = document.getElementById('evaluateRuleBtn');

const ruleOutput = document.getElementById('ruleOutput');
const combinedRuleOutput = document.getElementById('combinedRuleOutput');
const evaluationOutput = document.getElementById('evaluationOutput');

const rule1Select = document.getElementById('rule1');
const rule2Select = document.getElementById('rule2');

// Create Rule API call
createRuleBtn.addEventListener('click', async () => {
    const attribute = document.getElementById('attribute').value;
    const operator = document.getElementById('operator').value;
    const value = document.getElementById('value').value;

    const ruleString = `${attribute} ${operator} ${value}`;
    
    try {
        const response = await fetch(`${BASE_URL}/create_rule/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ rule_string: ruleString })
        });

        const data = await response.json();
        ruleOutput.textContent = JSON.stringify(data, null, 2);
        updateRuleSelections(ruleString);
    } catch (error) {
        ruleOutput.textContent = 'Error creating rule: ' + error;
    }
});

// Combine Rules API call
combineRulesBtn.addEventListener('click', async () => {
    const rule1 = rule1Select.value;
    const rule2 = rule2Select.value;
    const logic = document.getElementById('logic').value;

    try {
        const response = await fetch(`${BASE_URL}/combine_rules/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                rule1: rule1,
                rule2: rule2,
                logic: logic
            })
        });

        const data = await response.json();
        combinedRuleOutput.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        combinedRuleOutput.textContent = 'Error combining rules: ' + error;
    }
});

// Evaluate Rule API call
evaluateRuleBtn.addEventListener('click', async () => {
    const jsonData = document.getElementById('jsonData').value;

    try {
        const response = await fetch(`${BASE_URL}/evaluate_rule/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: jsonData
        });

        const data = await response.json();
        evaluationOutput.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        evaluationOutput.textContent = 'Error evaluating rule: ' + error;
    }
});

// Function to update the rule select dropdowns with new rules
function updateRuleSelections(newRule) {
    const option1 = document.createElement('option');
    option1.value = newRule;
    option1.textContent = newRule;

    const option2 = document.createElement('option');
    option2.value = newRule;
    option2.textContent = newRule;

    rule1Select.appendChild(option1);
    rule2Select.appendChild(option2);
}
