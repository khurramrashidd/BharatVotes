# BharatVotes 🗳️🇮🇳

## Secure Blockchain & Biometric-Based Voting Platform

**BharatVotes** is a secure, transparent, and modern digital voting platform built using **Python (Flask)**.  
It integrates **Blockchain technology (SHA-256 hashing)** for immutable vote recording and **Face Recognition-based biometric authentication** for secure voter verification.

The system simulates a complete election ecosystem including Voters, Candidates, Booth Officers, and the Election Commission, demonstrating how decentralized and cryptographic systems can strengthen democratic processes.

---
    
## 🚀 Key Features

### 🔐 Security & Integrity
- **Blockchain-Based Voting:** Every vote is hashed using SHA-256 and linked to the previous block, forming an immutable chain.
- **Tamper Detection:** Chain integrity verification via `/api/verify_chain`.
- **Biometric Authentication:** Face recognition verification before ballot activation.
- **Secure Password Storage:** Implemented using Werkzeug hashing.

---

### 👥 Multi-Role Election Ecosystem

- 🗳️ **Voter Dashboard**
  - Profile management
  - Voting status tracking
  - Digital vote receipt

- 👤 **Candidate Portal**
  - Nomination filing
  - Affidavit upload
  - Approval tracking

- 🏛️ **ECI (Election Commission) Dashboard**
  - Approve/Reject nominations
  - Monitor election statistics
  - Oversee blockchain verification

- 👮 **Booth Officer Dashboard**
  - Manage polling stations
  - Handle biometric verification issues
  - Manual override controls

---

## 📊 Real-Time Monitoring

- Live vote tallying
- Constituency-wise result tracking
- Blockchain explorer for vote block verification
- Chain integrity validation API

---

## 🛠️ Tech Stack

**Backend:**
- Python
- Flask
- SQLAlchemy (SQLite / PostgreSQL)

**Database & Realtime:**
- Firebase Realtime Database

**Security:**
- Hashlib (SHA-256)
- Werkzeug Security

**Machine Learning:**
- Face Recognition (via `utils.py`)

**Frontend:**
- HTML5
- CSS3
- JavaScript

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/khurramrashidd/bharatvotes.git
cd bharatvotes
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Firebase Configuration

1. Add your Firebase service account JSON file to the project root.
2. Update configuration in `config.py` or set environment variables.

### 5️⃣ Run the Application

```bash
python app.py
```

App will run at:
```
http://0.0.0.0:5000
```

---

## 🔑 Demo Credentials (Development Only)

Default accounts are created via `seed_db.py` for testing purposes.

| Role | Username | Password |
|------|----------|----------|
| ECI Admin | eci | eci123 |
| System Admin | admin | admin123 |
| Candidates | Register via portal | User-defined |
| Voters | Register via portal | User-defined |

⚠️ These credentials are for development/demo use only.

---

## 📂 Project Structure

```
bharatvotes/
│
├── app.py            # Application entry point
├── routes.py         # API routes & controllers
├── models.py         # Database models
├── blockchain.py     # Blockchain logic (hashing, linking, verification)
├── utils.py          # Face recognition & helper utilities
├── seed_db.py        # Database seeding script
├── templates/        # HTML templates
├── static/           # CSS, JS, assets
└── requirements.txt  # Dependencies
```

---

## 🧠 Future Scope

- Integration with Aadhaar-based verification (simulation)
- Deployment using Ethereum / Hyperledger
- Zero-Knowledge Proof-based anonymous validation
- AI-driven anomaly detection in voting patterns
- Cloud-native scalable deployment

---

## 🎯 Use Case & Vision

BharatVotes demonstrates how **Blockchain + Biometric AI** can enhance:
- Transparent governance
- Tamper-proof election systems
- Secure civic-tech platforms
- Digital India & Atmanirbhar Bharat initiatives

---

## 🛡️ License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Khurram Rashid**

If you found this project useful, feel free to ⭐ the repository!
