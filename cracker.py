import sys
import hashlib

def crack_password(target_hash, algorithm, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                password = line.strip()
                hashed = hashlib.new(algorithm, password.encode()).hexdigest()
                if hashed == target_hash:
                    return password
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_path}")
        sys.exit(1)
    except ValueError:
        print(f"Unsupported algorithm: {algorithm}")
        sys.exit(1)
    return None

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python cracker.py <target_hash> <algorithm> <wordlist_file>")
        sys.exit(1)

    target_hash = sys.argv[1]
    algorithm = sys.argv[2]
    wordlist_path = sys.argv[3]

    if algorithm not in hashlib.algorithms_available:
        print(f"Unsupported algorithm: {algorithm}. Available algorithms: {', '.join(hashlib.algorithms_available)}")
        sys.exit(1)

    result = crack_password(target_hash, algorithm, wordlist_path)
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found in the wordlist.")