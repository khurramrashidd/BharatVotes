from datetime import datetime, timedelta
import random
from models import (
    db, Admin, BoothOfficer, Candidate, DigiLockerDummy, 
    CandidateUser, Nomination, Voter
)

def run():
    """Seed database with initial demo data. Safe to run multiple times."""
    print("🌱 Starting Database Seeding...")

    # ---------------- 1. Admin ----------------
    if not Admin.query.filter_by(username='admin').first():
        admin = Admin(username='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        print("✅ Admin created (admin/admin123)")
    else:
        print("   Admin already exists.")

    # ---------------- 2. Booth Officer ----------------
    if not BoothOfficer.query.filter_by(username='booth').first():
        booth = BoothOfficer(username='booth', booth_number='B1')
        booth.set_password('booth123')
        db.session.add(booth)
        print("✅ Booth Officer created (booth/booth123)")
    else:
        print("   Booth Officer already exists.")

    # ---------------- 3. Election Candidates ----------------
    if Candidate.query.count() == 0:
        entries = [
            ('C1', 'Ram Kumar', 'BJP', 'Patna'),
            ('C2', 'Sita Devi', 'RJD', 'Gaya'),
            ('C3', 'Ajay Singh', 'JD(U)', 'Hajipur'),
            ('C4', 'Meera Sharma', 'INC', 'Purnia'),
            ('C5', 'Vikas Yadav', 'LJP', 'Nalanda'),
            ('C6', 'Raju Prasad', 'HAM', 'Muzaffarpur'),
            ('C7', 'Sunita Kumari', 'RLSP', 'Darbhanga'),
            ('C8', 'Anil Kumar', 'JAP', 'Siwan'),
            ('C9', 'Kiran Patel', 'CPI(ML)', 'Bhagalpur'),
            ('C10', 'Asad Khan', 'AIMIM', 'Samastipur'),
        ]
        for cid, name, party, const in entries:
            c = Candidate(candidate_id=cid, name=name, party=party, constituency=const)
            db.session.add(c)
        print("✅ 10 Candidates created")
    else:
        print("   Candidates already exist.")

    # ---------------- 4. DigiLocker Dummy Records ----------------
    if DigiLockerDummy.query.count() == 0:
        dummy_records = [
            DigiLockerDummy(
                name="Ramesh Kumar", dob="1985-03-15", aadhaar="123456789012",
                address="Ward 5, Patna", party="Independent", constituency="Patna Sahib",
                email="ramesh.kumar@example.com", phone="9876543210"
            ),
            DigiLockerDummy(
                name="Sushila Devi", dob="1978-07-22", aadhaar="987654321098",
                address="Sector 12, Hajipur", party="People’s Party", constituency="Hajipur",
                email="sushila.devi@example.com", phone="9123456780"
            ),
            DigiLockerDummy(
                name="Mohammad Ali", dob="1990-11-05", aadhaar="456789123456",
                address="Gaya City, Bihar", party="Progressive Front", constituency="Gaya",
                email="mohammad.ali@example.com", phone="9001122334"
            ),
        ]
        db.session.bulk_save_objects(dummy_records)
        print("✅ DigiLocker Dummy Records created")
    else:
        print("   DigiLocker data already exists.")

    # ---------------- 5. Candidate User Accounts & Nominations ----------------
    # Create Users first
    cands_data = [
        ("123456789012", "candidate123"),
        ("987654321098", "candidate123"),
        ("456789123456", "candidate123")
    ]
    
    created_users = {}
    for aadhaar, pwd in cands_data:
        user = CandidateUser.query.filter_by(aadhaar=aadhaar).first()
        if not user:
            user = CandidateUser(aadhaar=aadhaar)
            user.set_password(pwd)
            db.session.add(user)
            db.session.flush() # Flush to get ID if needed
        created_users[aadhaar] = user

    # Create Nominations
    if Nomination.query.count() == 0:
        now = datetime.utcnow()
        nominations = [
            Nomination(
                name="Ramesh Kumar", dob="1985-03-15", aadhaar="123456789012",
                address="Ward 5, Patna", party="Independent", constituency="Patna Sahib",
                email="ramesh.kumar@example.com", phone="9876543210",
                affidavit="uploads/sample.pdf", property_cert="uploads/sample.pdf",
                education_cert="uploads/sample.pdf", criminal_record="uploads/sample.pdf",
                status="Pending", username="123456789012",
                password=created_users["123456789012"].password,
                created_at=now - timedelta(days=1)
            ),
            Nomination(
                name="Sushila Devi", dob="1978-07-22", aadhaar="987654321098",
                address="Sector 12, Hajipur", party="People’s Party", constituency="Hajipur",
                email="sushila.devi@example.com", phone="9123456780",
                affidavit="uploads/sample.pdf", property_cert="uploads/sample.pdf",
                education_cert="uploads/sample.pdf", criminal_record="uploads/sample.pdf",
                status="Approved", username="987654321098",
                password=created_users["987654321098"].password,
                created_at=now - timedelta(hours=12)
            ),
            Nomination(
                name="Mohammad Ali", dob="1990-11-05", aadhaar="456789123456",
                address="Gaya City, Bihar", party="Progressive Front", constituency="Gaya",
                email="mohammad.ali@example.com", phone="9001122334",
                affidavit="uploads/sample.pdf", property_cert="uploads/sample.pdf",
                education_cert="uploads/sample.pdf", criminal_record="uploads/sample.pdf",
                status="Rejected", username="456789123456",
                password=created_users["456789123456"].password,
                created_at=now
            ),
        ]
        db.session.add_all(nominations)
        print("✅ Sample Nominations created")
    else:
        print("   Nominations already exist.")

    # ---------------- 6. Dummy Voters (Moved from app.py) ----------------
    if Voter.query.count() < 10:
        print("🌱 Seeding 60 Dummy Voters...")
        states = ["Maharashtra", "Delhi", "UP", "Karnataka", "Bihar"]
        assemblies = ["Panvel", "Hajipur", "Chandni Chowk", "Bangalore South", "Patna"]
        
        for i in range(1, 61):
            vid = f"VOT{10000+i}"
            aadhaar = f"9999{10000000+i}"
            state = random.choice(states)
            
            # Check if exists to be safe
            if not Voter.query.filter_by(voter_id=vid).first():
                v = Voter(
                    voter_id=vid,
                    aadhaar=aadhaar,
                    name=f"Voter {i}",
                    dob=datetime(1980 + (i%20), 1, 1).date(),
                    father_name=f"Father of Voter {i}",
                    gender="Male" if i % 2 == 0 else "Female",
                    address=f"House No {i}, Sector {i%10}, {state}",
                    assembly=random.choice(assemblies),
                    part_no=f"Part-{i%5 + 1}",
                    serial_no=f"SL-{i}",
                    face_image=None 
                )
                db.session.add(v)
        print("✅ Dummy Voters created")
    else:
        print("   Voters already exist.")

    # ---------------- Commit ----------------
    try:
        db.session.commit()
        print("✅ Database Seeding Complete!")
    except Exception as e:
        db.session.rollback()
        print(f"❌ Seeding Error: {e}")

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    with app.app_context():
        run()