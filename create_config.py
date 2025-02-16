import os
import json

config_dir = "C:/Users/HP/Desktop/finnle HR project/config"
file_path = os.path.join(config_dir, "service_account.json")

# Folder agar exist nahi karta to create karo
os.makedirs(config_dir, exist_ok=True)

# ✅ Actual Google Service Account JSON Data Structure
data = {
    "type": "service_account",
    "project_id": "your_project_id",
    "private_key_id": "your_private_key_id",
    "private_key": "-----BEGIN PRIVATE KEY-----\nYourKeyHere\n-----END PRIVATE KEY-----\n",
    "client_email": "your_service_account@your_project.iam.gserviceaccount.com",
    "client_id": "your_client_id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your_service_account@your_project.iam.gserviceaccount.com"
}

# ✅ JSON File me data write karo
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"✅ service_account.json created successfully at: {file_path}")
