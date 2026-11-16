# ==========================================
# Q4!!!!
# ==========================================

import os
import sys
import random
import string

def spread_worm():
    existing_copies = [f for f in os.listdir('.') if f.startswith('worm_') and f.endswith('.py')]
    if len(existing_copies) >= 5:
        return
    random_name = "worm_" + ''.join(random.choices(string.ascii_letters, k=5)) + ".py"
    with open(sys.argv[0], 'r', encoding='utf-8') as original_file:
        code = original_file.read()
    with open(random_name, 'w', encoding='utf-8') as copy_file:
        copy_file.write(code)

if __name__ == "__main__":
    spread_worm()
    print("worm executed. new copy is created if is under the limit of 5.")