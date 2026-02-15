# import os

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY', 'my-secret-key')
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'election_nominations.db')
#     # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(BASE_DIR, 'election_nominations.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static/uploads')
#     MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB limit for uploads

# # Ensure the upload folder exists
# os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)


import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Core Flask Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    
    # Database Config (SQLite)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'election_nominations.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File Uploads
    UPLOAD_FOLDER = os.path.join(basedir, 'static/uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max limit

    # Firebase Config
    # Assumes the file 'serviceAccountKey.json' is in the root folder (same as app.py)
    FIREBASE_CREDENTIALS = os.path.join(basedir, 'firebase_credentials.json')
    FIREBASE_DB_URL = "https://fir-demo1-4f0eb-default-rtdb.firebaseio.com"