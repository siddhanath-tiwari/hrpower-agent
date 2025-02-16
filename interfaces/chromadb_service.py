import chromadb
import pandas as pd
import uuid

# ChromaDB client initialization (compatible with 0.4.15)
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="candidates")

def store_candidate_data(name, email, phone, whatsapp, skills):
    skills_str = ", ".join(skills)  # Convert list to a comma-separated string
    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "whatsapp": whatsapp,
        "skills": skills_str  # Store as string instead of list
    }
    candidate_id = str(uuid.uuid4())  # Unique ID
    collection.add(
        ids=[candidate_id],
        metadatas=[data],
        documents=[skills_str]  # Storing skills as text for retrieval
    )

def retrieve_candidate_data(name):
    results = collection.query(query_texts=[name], n_results=1)
    return results

def load_csv_data(file_path):
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        store_candidate_data(
            row['name'],
            row['email'],
            str(row['phone']),
            str(row['whatsapp']),
            row['skills'].split(', ')  # Ensure skills are split correctly
        )

# Example usage
if __name__ == "__main__":
    load_csv_data('data/hr_data.csv')
    print(retrieve_candidate_data("John Doe"))
