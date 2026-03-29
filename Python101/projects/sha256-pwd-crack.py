from pwn import *
import sys

if len(sys.argv) != 2:
    print("Invalid arguments!")
    print(f">> {sys.argv[0]} <sha256sym>")
    exit(1)

wanted_hash = sys.argv[1]

password_file = "projects/Pwdb_top-1000.txt"
attempts = 0

with log.progress(f"Attempting to crack: {wanted_hash}") as p:
    with open(password_file, "r") as password_list:
        for password in password_list:
            attempts += 1
            password = password.strip("\n").encode("utf-8")
            password_hash = sha256sumhex(password)
            p.status(f"{attempts} {password} == {password_hash}")
            if password_hash == wanted_hash:
                p.success(f"Password found after {attempts} attempt! {password} hashes to {password_hash}")
                exit(0)
        p.failure("Password hash not found!")