# Password Migration Script

This directory contains a script to migrate plaintext passwords to secure bcrypt hashes.

## Usage

After upgrading the application code, run the migration script to convert any existing plaintext passwords in the database:

```
python scripts/hash_existing_passwords.py
```

This is a one-time script that should be run after deploying the code changes. The script:

1. Checks all users in the database
2. Identifies plaintext passwords (those not starting with '$2b$')
3. Converts them to bcrypt hashes
4. Updates the database records

## Important Notes

- The script is safe to run multiple times - it will only convert passwords that aren't already hashed
- After running this script, all passwords will be securely stored as bcrypt hashes
- The application code has been updated to support both hashed and plaintext passwords during the transition, but will eventually only support hashed passwords