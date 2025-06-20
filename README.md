# Hashed-Password-Cracker

Description

This is a simple Python script that attempts to crack a hashed password using a dictionary attack. It takes a target hash, a hashing algorithm (e.g., sha256), and a wordlist file as inputs. The script hashes each password in the wordlist using the specified algorithm and checks if it matches the target hash.

Note: This project is for educational purposes only. Unauthorized password cracking is illegal and unethical.

Requirements

Python 3.x

No additional dependencies are required as the script uses standard Python libraries.

Usage

Prepare a wordlist file: Create a text file with one password per line (e.g., wordlist.txt).


Run the script with the following command:

python cracker.py <target_hash> <algorithm> <wordlist_file>

<target_hash>: The hash you want to crack.

<algorithm>: The hashing algorithm used (e.g., sha256, md5).

<wordlist_file>: Path to the wordlist file.



If a matching password is found, it will be displayed. Otherwise, a message will indicate that no match was found.

Example

To crack a SHA256 hash using a wordlist named wordlist.txt, run:

python cracker.py 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 sha256 wordlist.txt


In this example, if the wordlist contains the password "password", the script will find a match since the provided hash corresponds to "password" hashed with SHA256.

Generating a Test Hash

To generate a hash for testing purposes, use the following Python code:

import hashlib
password = "password123"
hash_value = hashlib.sha256(password.encode()).hexdigest()
print(hash_value)

Replace "password123" with any password you want to test.

Important Notes




This script is intended for educational use only.



Always ensure you have permission before attempting to crack any password.



The script's performance depends on the size of the wordlist and the computational power available.



The wordlist should contain one password per line with no extra spaces or blank lines.

Supported Algorithms

The script supports hashing algorithms available in Python's hashlib library, including but not limited to:

md5

sha1

sha256

sha512

To see all available algorithms on your system, run:

import hashlib
print(hashlib.algorithms_available)

Troubleshooting

File Not Found: Ensure the wordlist file path is correct and the file exists in the specified location.



Unsupported Algorithm: Check the spelling of the algorithm and ensure it is supported by hashlib.



No Match Found: The password may not be in the wordlist, or the hash may have been generated with a different algorithm.

License

This project is licensed under the MIT License - see the LICENSE file for details.
