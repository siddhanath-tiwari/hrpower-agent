# def job_description_assistance(job_title, skills):
#     job_description = f"Job Title: {job_title}\nSkills: {', '.join(skills)}"
#     return job_description


from transformers import pipeline

def job_description_assistance(job_title, skills):
    generator = pipeline("text-generation", model="gpt2")
    prompt = f"Generate a job description for {job_title} requiring skills: {', '.join(skills)}"
    job_description = generator(prompt, max_length=150, num_return_sequences=1)
    
    return job_description[0]['generated_text']

# Example usage
print(job_description_assistance("Software Engineer", ["Python", "Machine Learning", "NLP"]))
