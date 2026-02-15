# from flask import Flask, session
# from config import Config
# from models import db
# # Import seed_db to run it automatically
# import seed_db 
# from routes import main_bp

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)
    
#     db.init_app(app)
#     app.register_blueprint(main_bp)
    
#     with app.app_context():
#         # Create Tables
#         db.create_all()

#         # Run Unified Seeder
#         # This handles Admin, Booth, Candidates, Nominations, DigiLocker, and Voters
#         seed_db.run()

#     return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run(port=5000, host="0.0.0.0", debug=True)



import os
from flask import Flask
from config import Config
from models import db
import firebase_admin
from firebase_admin import credentials

# Import the seeder script we fixed earlier
import seed_db 

from routes import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # 1. Initialize SQL Database
    db.init_app(app)
    
    # 2. Initialize Firebase (Realtime Database)
    # Check if already initialized to prevent errors during auto-reload
    if not firebase_admin._apps:
        try:
            cred_path = app.config['FIREBASE_CREDENTIALS']
            db_url = app.config['FIREBASE_DB_URL']
            
            if os.path.exists(cred_path):
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred, {
                    'databaseURL': db_url
                })
                print(f"🔥 Firebase Connected: {db_url}")
            else:
                print(f"⚠️ Warning: Firebase JSON key not found at: {cred_path}")
                print("   Realtime features will not work until the file is added.")
        except Exception as e:
            print(f"❌ Firebase Init Error: {e}")

    # 3. Register Blueprints
    app.register_blueprint(main_bp)
    
    # 4. Create Tables & Seed Data
    with app.app_context():
        db.create_all()
        # Run the unified seeder (Admin, Candidates, Voters, etc.)
        seed_db.run()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, host="0.0.0.0", debug=True)