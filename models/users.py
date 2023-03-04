import db

def get_user_by_email(email):
    user = db.select_one('SELECT * FROM users WHERE email=%s', [email])
    return user

def insert_user(name, email, password_hash):
    db.write(
        "INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)",
        [name, email, password_hash]
    )