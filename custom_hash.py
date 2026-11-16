# ==========================================
# Q5!!!!
# ==========================================

def my_custom_hash(text):
    hash_val = 7
    for char in text:
        hash_val = (hash_val * 31 + ord(char)) % 1000000
    return hash_val


def compare_hashes(str1, str2):
    return my_custom_hash(str1) == my_custom_hash(str2)

if __name__ == "__main__":
    print("hash of 'cyber':", my_custom_hash("cyber"))
    print("hash of 'security':", my_custom_hash("security"))
    print("do 'cyber' and 'cyber' match?", compare_hashes("cyber", "cyber"))