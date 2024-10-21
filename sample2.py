import sqlite3
import pickle

# 1. Uninitialized variable usage
def example_function():
    print(uninitialized_variable)  # This will cause an error

# 2. SQL Injection vulnerability
def fetch_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

# 3. Insecure deserialization
def load_data(serialized_data):
    data = pickle.loads(serialized_data)  # Insecure deserialization
    return data

# 4. Hardcoded password
def connect_to_service():
    password = "supersecret"  # Hardcoded secret
    print(f"Connecting with password: {password}")

# 5. Use of `eval`
def evaluate_expression(expr):
    result = eval(expr)  # Using eval is dangerous
    return result

if __name__ == "__main__":
    example_function()
    print(fetch_user_data("admin' OR '1'='1"))  # Example of SQL injection
    serialized = pickle.dumps({'key': 'value'})
    print(load_data(serialized))
    connect_to_service()
    print(evaluate_expression("2 + 2"))
