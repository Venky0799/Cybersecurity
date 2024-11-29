def authenticate(username, password):
    # Hardcoded credentials (vulnerability: sensitive data exposure)
    HARDCODED_USERNAME = "admin"
    HARDCODED_PASSWORD = "password123"

    if username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD:
        return "Login successful! Welcome, admin."
    else:
        return "Authentication failed. Invalid credentials."

def main():
    print("Welcome to the Simple Authentication System")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Call the authenticate function
    result = authenticate(username, password)
    print(result)

if __name__ == "__main__":
    main()
