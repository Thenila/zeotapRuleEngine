import sqlite3

def init_db():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rule_string TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_rule(rule_string):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rules (rule_string) VALUES (?)', (rule_string,))
    conn.commit()
    conn.close()

def get_rules():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rules')
    rules = cursor.fetchall()
    conn.close()
    return rules
