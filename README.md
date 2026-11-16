# cybersecurity homework repository

this repository shows important ideas in cybersecurity through code python.

## files description

1. **`vulnerable_sql.py`**: creates a database using `sqlite3` in memory (Mock DB). it adds user input directly into the query running a payload of `1' OR '1'='1` which makes the database show all records.



2. **`secure_sql.py`**: does the job but uses Prepared Statements (`?` placeholder). the same payload does not work because the DB engine safely handles the input string.



3. **`trojan_calculator.py`**: a simple calculator class. it has a Logic Bomb that waits for the sum `10` to happen. when it is triggered the internal state changes and all next operations return `10`.



4. **`worm.py`**: a script that copies itself. when it runs it reads its code and makes a new `.py` file with a random name. it has a way to stop copying if 5 copies are made in the folder.



5. **`custom_hash.py`**: a way to create a hash. it processes a string one character at a time, with modulo math giving an integer as the hash. has a check function.



6. **`test_all.py`**: a complete `unittest` set that covers everything in the repository checking exploits, fixes and limits of behavior.

## how to run

run the test suite to run all modules in a fake environment:

`python test_all.py`