Rule Engine Project

This project is a Rule Engine system designed to evaluate user eligibility based on various attributes such as age, department, income, and spending. The system uses an Abstract Syntax Tree (AST) to represent conditional rules and provides a 3-tier application architecture including a simple UI, API, and backend, with functionalities for creating, combining, and evaluating dynamic rules.

Table of Contents
Project Overview
Features
Architecture
Technologies Used
Installation
Usage
API Endpoints
Future Enhancements
Contributing
License
Project Overview
The Rule Engine Project is built to provide an efficient way to create and evaluate business rules. It can determine eligibility for a specific set of criteria by evaluating conditional rules using attributes like age, department, income, and spend. By using an Abstract Syntax Tree (AST) for rule representation, this system allows for dynamic and complex rule combinations.

Features
Dynamic Rule Creation: Create custom rules based on various attributes.
Rule Combination: Combine multiple rules into logical sets using operators (AND, OR).
Rule Evaluation: Evaluate rules against user data to determine eligibility.
3-Tier Architecture: Organized into UI, API, and backend layers for scalability and ease of maintenance.
AST-Based Rule Representation: Supports complex rule expressions with clear structure and evaluation flow.
Architecture
The project follows a 3-tier architecture:

UI Layer: A simple web interface where users can create and view rules and their evaluations.
API Layer: RESTful API that allows CRUD operations for rules and handles rule evaluation requests.
Backend Layer: Contains business logic, the rule evaluation engine, and data storage.
The use of an AST allows for efficient rule parsing and evaluation, while each tier interacts seamlessly to deliver a cohesive experience.

Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: .NET (C#), ASP.NET Core
Database: SQL Server or SQLite (for testing purposes)
Version Control: Git and GitHub
Installation
Prerequisites
.NET 6.0 SDK or later
SQL Server or SQLite
Git
Steps
Clone the Repository:

bash
Copy code
git clone https://github.com/Thenila/zeotapRuleEngine.git
cd zeotapRuleEngine
Setup Database:

Configure your database connection string in the appsettings.json file.
Run Database Migrations:

bash
Copy code
dotnet ef database update
Build and Run:

bash
Copy code
dotnet build
dotnet run
Usage
Creating a Rule: Use the UI to define a new rule by specifying conditions (e.g., Age > 18 AND Income > 50000).
Evaluating a Rule: Submit user data via the API to check eligibility against defined rules.
Combining Rules: Use logical operators (AND, OR) to create complex rules by combining simple ones.
API Endpoints
POST /api/rules: Create a new rule
GET /api/rules/{id}: Retrieve a rule by ID
PUT /api/rules/{id}: Update an existing rule
DELETE /api/rules/{id}: Delete a rule
POST /api/evaluate: Evaluate user data against a rule
Refer to the API documentation for detailed request/response structures.

Future Enhancements
User Interface Improvements: Add more visual tools for rule creation.
Support for Additional Attributes: Add support for more attributes in rule creation.
Enhanced Logging: Implement detailed logging for rule evaluations and user activity.
Integration with External Systems: Allow importing and exporting rules to integrate with other systems.
Contributing
Contributions are welcome! Please fork the repository and create a pull request with a detailed description of the changes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

