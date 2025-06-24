"""
One-time script to migrate plaintext passwords to bcrypt hashes
"""
import sys
import os

# Add parent directory to path so we can import from the app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from estudo import db, bcrypt
from estudo.models import User

def hash_passwords():
    """Convert plaintext passwords to bcrypt hashes"""
    users = User.query.all()
    count = 0
    
    for user in users:
        # Check if the password is not already hashed
        # Bcrypt hashes start with $2b$
        if user.senha and not user.senha.startswith('$2b$'):
            print(f"Hashing password for user: {user.email}")
            hashed_password = bcrypt.generate_password_hash(
                user.senha.encode('utf-8')
            )
            user.senha = hashed_password
            count += 1
    
    if count > 0:
        db.session.commit()
        print(f"Successfully hashed {count} passwords")
    else:
        print("No plaintext passwords found. All passwords are already hashed.")

if __name__ == "__main__":
    hash_passwords()