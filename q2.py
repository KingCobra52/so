import threading

# The correct password
correct_password = "0000000123"

# Number of threads
NUM_THREADS = 4

# Global variable to indicate whether the password has already been found
found = False

# Lock to protect access to the variable 'found'
lock = threading.Lock()

def worker(id, start, end):
    global found
    for i in range(start, end):
        with lock:
            if found:
                break  # Another thread has already found the password.

        attempt = f"{i:010d}"  # Formats the number with 10 digits, with leading zeros.

        if attempt == correct_password:
            with lock:
                found = True  # Mark as found
                print(f"Password found: {attempt} pela thread #{id}")
            break

def main():
    total_passwords = 10**10
    passwords_per_thread = total_passwords // NUM_THREADS
    threads = []

    for i in range(NUM_THREADS):
        start = i * passwords_per_thread
        end = total_passwords if i == NUM_THREADS - 1 else (i + 1) * passwords_per_thread
        t = threading.Thread(target=worker, args=(i, start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join() #wait for all threads to finish

if __name__ == "__main__":
    main()
