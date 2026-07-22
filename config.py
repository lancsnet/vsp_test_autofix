DATABASE_PASSWORD = "admin123"
API_KEY = "sk-hardcoded-secret-do-not-do-this"

def connect():
    return db.connect(password=DATABASE_PASSWORD)
