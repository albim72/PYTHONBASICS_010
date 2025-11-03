secret = "abc123"
user_code = input("Enter your code: ")
exec(user_code)

def check_login():
    print("Access denied")

malicious = "def check_login():\n    print('Access granted!')"
exec(malicious)

check_login()
