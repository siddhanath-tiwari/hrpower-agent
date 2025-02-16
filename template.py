import os

def create_structure(base_path):
    structure = {
        "customer_support_agent": [
            "__init__.py", "document_understanding.py", "query_handling.py", 
            "escalation_mechanism.py", "ner.py", "sentiment_analysis.py"
        ],
        "candidate_follow_up_agent": [
            "__init__.py", "applicant_initiation.py", "job_description_assistance.py", 
            "application_review.py", "schedule_interview.py", "feedback_loop.py", 
            "resume_parsing.py", "candidate_ranking.py"
        ],
        "interfaces": [
            "__init__.py", "user_interface.py", "email_service.py", "sms_service.py", 
            "whatsapp_service.py", "calendar_service.py", "chromadb_service.py"
        ],
        "static/css": ["styles.css"],
        "templates": ["index.html"],
        "tests": [
            "test_customer_support_agent.py", "test_candidate_follow_up_agent.py", "test_interfaces.py"
        ],
        "data/training_data": [],
    }
    
    # Create directories and files
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("# " + file + "\n")
    
    # Create root-level files
    root_files = ["main.py", "requirements.txt", "setup.py", "README.md", "data/hr_data.csv"]
    for file in root_files:
        file_path = os.path.join(base_path, file)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("# " + file + "\n")

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    create_structure(base_path)
    print("Project structure created successfully!")

if __name__ == "__main__":
    main()
