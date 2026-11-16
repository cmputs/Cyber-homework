# ==========================================
# Q1!!!!
# ==========================================

import sqlite3

def get_user_vulnerable(user_id_input):
    # (Mock DB)
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE USERS (id TEXT, name TEXT)")
    cursor.execute("INSERT INTO USERS VALUES ('1', 'Alice'), ('2', 'Bob')")
    query = "SELECT * FROM USERS WHERE id = '" + user_id_input + "'"
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    malicious_input = "1' OR '1'='1"
    print("vulnerable result:", get_user_vulnerable(malicious_input))
