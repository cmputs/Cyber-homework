# ==========================================
# Q2!!!!
# ==========================================

import sqlite3

def get_user_secure(user_id_input):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE USERS (id TEXT, name TEXT)")
    cursor.execute("INSERT INTO USERS VALUES ('1', 'Alice'), ('2', 'Bob')")
    query = "SELECT * FROM USERS WHERE id = ?"
    cursor.execute(query, (user_id_input,))
    return cursor.fetchall()

if __name__ == "__main__":
    malicious_input = "1' OR '1'='1"
    print("secure results:", get_user_secure(malicious_input))