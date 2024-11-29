import os
import pickle
import random
import time
import threading

# 1. Insecure Deserialization (Pickle vulnerability)
def insecure_deserialization(serialized_data):
    try:
        # Deserializing user-provided data (pickle is dangerous when deserializing untrusted data)
        deserialized_obj = pickle.loads(serialized_data)
        print("Deserialized Object:", deserialized_obj)
    except Exception as e:
        print(f"Deserialization error: {e}")

# 2. Simulating Buffer Overflow (via unsafe input)
def simulate_buffer_overflow(user_input):
    # This is a simulation; Python handles memory safety better than C/C++, but in some cases (e.g., using C extensions), buffer overflow can happen
    if len(user_input) > 100:
        print("Buffer Overflow Detected: Input exceeds buffer limit!")
    else:
        print("Input is safe.")

# 3. Path Traversal (unsafe file access)
def unsafe_file_access(file_name):
    # Path traversal vulnerability (allows navigating outside the intended directory)
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except Exception as e:
        print(f"File access error: {e}")

# 4. Weak Randomness (predictable random numbers)
def weak_randomness():
    # Using a predictable random number generator (unsafe for cryptography)
    print(f"Predictable random number: {random.randint(0, 100)}")

# 5. Race Condition (simulated via threads)
def race_condition():
    balance = 0

    # This function simulates a simple bank account update
    def update_balance():
        nonlocal balance
        # Simulate a race condition by accessing and updating balance without synchronization
        temp = balance
        temp += 1
        time.sleep(0.1)  # Simulate a delay
        balance = temp
        print(f"Updated balance: {balance}")

    threads = []
    for _ in range(5):
        thread = threading.Thread(target=update_balance)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final balance: {balance}")

# 6. Improper Error Handling (stack trace exposure)
def improper_error_handling():
    try:
        # Simulating a runtime error (ZeroDivisionError)
        result = 10 / 0
    except Exception as e:
        # Exposing detailed stack trace or error messages (bad practice)
        print(f"An error occurred: {e}")

# Main function to run the vulnerabilities
def main():
    print("Welcome to the vulnerable Python application!")

    # 1. Insecure Deserialization
    serialized_data = input("Enter serialized data for deserialization test: ")
    insecure_deserialization(serialized_data.encode())  # Simulate a pickle deserialization

    # 2. Buffer Overflow simulation
    user_input = input("Enter a string to test buffer overflow simulation: ")
    simulate_buffer_overflow(user_input)

    # 3. Path Traversal (unsafe file access)
    file_name = input("Enter a file name for path traversal test: ")
    unsafe_file_access(file_name)

    # 4. Weak Randomness
    print("Testing weak randomness...")
    weak_randomness()

    # 5. Race Condition simulation
    print("Simulating race condition (threading) issue...")
    race_condition()

    # 6. Improper Error Handling
    print("Testing improper error handling...")
    improper_error_handling()

if __name__ == "__main__":
    main()
