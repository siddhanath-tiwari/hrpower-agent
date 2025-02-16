from flask import Flask, request, jsonify, render_template, redirect, url_for
from interfaces.user_interface import start_interface 
from werkzeug.utils import secure_filename
import os
import PyMuPDF
# import pdfplumber
from customer_support_agent.document_understanding import document_understanding
from customer_support_agent.query_handling import query_handling
from customer_support_agent.escalation_mechanism import escalation_mechanism
from candidate_follow_up_agent.applicant_initiation import applicant_initiation
from candidate_follow_up_agent.job_description_assistance import job_description_assistance
from candidate_follow_up_agent.application_review import application_review
from candidate_follow_up_agent.schedule_interview import schedule_interview
from candidate_follow_up_agent.feedback_loop import feedback_loop
from candidate_follow_up_agent.resume_parsing import parse_resume
from candidate_follow_up_agent.candidate_ranking import rank_candidates
from interfaces.email_service import send_email
from interfaces.sms_service import send_sms
from interfaces.whatsapp_service import send_whatsapp_message
from interfaces.chromadb_service import store_candidate_data, retrieve_candidate_data

# chat bot service implementation using Groq 

from flask import Flask, request, jsonify, render_template
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")




UPLOAD_FOLDER = 'uploads/resumes'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert HR assistant. You help in resume screening, interview scheduling, and answering HR-related queries."},
                {"role": "user", "content": user_input}
            ],
            api_key=GROQ_API_KEY
        )
        return jsonify({"response": response['choices'][0]['message']['content']})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500






@app.route('/')
def index():
    return render_template('index.html')



# @app.route('/contact')
# def contact():
#     return render_template('contact.html')




# @app.route('/home')
# def home():
#     return redirect(url_for('index'))



# @app.route('/upload_resume', methods=['GET', 'POST'])
# def upload_resume():
#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return redirect(request.url)
#         file = request.files['file']
#         if file.filename == '':
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             # Process the uploaded resume
#             with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r') as f:
#                 resume_text = f.read()
#             parsed_skills = parse_resume(resume_text)
#             # Store candidate data
#             applicant_name = request.form.get('name')
#             email = request.form.get('email')
#             phone = request.form.get('phone')
#             whatsapp_number = request.form.get('whatsapp')
#             store_candidate_data(applicant_name, email, phone, whatsapp_number, parsed_skills)
#             return jsonify({"message": "Resume uploaded and processed successfully"})
#     return render_template('upload_resume.html')


@app.route('/home')
def home():
    return redirect(url_for('index'))

@app.route('/upload_resume', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'r') as f:
                resume_text = f.read()
            parsed_skills = parse_resume(resume_text)
            applicant_name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            whatsapp_number = request.form.get('whatsapp')
            store_candidate_data(applicant_name, email, phone, whatsapp_number, parsed_skills)
            return jsonify({"message": "Resume uploaded and processed successfully"})
    return render_template('upload_resume.html')

# ✅ Contact Route (Yahaan likhna best hai)
@app.route('/contact')
def contact():
    return render_template('contact.html')

# if __name__ == "__main__":
#     app.run(debug=True)


@app.route('/customer_support', methods=['POST'])
def customer_support():
    data = request.json
    document = data['document']
    query = data['query']
    context = document_understanding(document).text
    answer = query_handling(query, context)
    escalation_status = escalation_mechanism(query, resolved=False)
    return jsonify({"answer": answer, "escalation_status": escalation_status})

@app.route('/candidate_follow_up', methods=['POST'])
def candidate_follow_up():
    data = request.json
    applicant_name = data['applicant_name']
    email = data['email']
    phone = data['phone']
    whatsapp_number = data['whatsapp_number']
    resume_text = data['resume_text']
    job_title = data['job_title']
    skills = data['skills']
    job_desc = job_description_assistance(job_title, skills)
    
    # Parse resume and rank candidate
    parsed_skills = parse_resume(resume_text)
    applications = [{"name": applicant_name, "skills": parsed_skills}]
    shortlisted_candidates = rank_candidates(applications, {"skills": skills})
    
    if shortlisted_candidates:
        initiation_status = applicant_initiation(applicant_name, email)
        store_candidate_data(applicant_name, email, phone, whatsapp_number, parsed_skills)
        send_email(email, "Interview Invitation", "You have been shortlisted for an interview.")
        send_sms(phone, "You have been shortlisted for an interview. Please check your email for details.")
        send_whatsapp_message(whatsapp_number, "You have been shortlisted for an interview. Please check your email for details.")
        
        interview_status = schedule_interview(applicant_name, "HR Team", "2025-02-20 10:00:00")
        feedback = ["Great candidate!", "Strong technical skills."]
        feedback_summary = feedback_loop(feedback)
        
        return jsonify({
            "initiation_status": initiation_status,
            "job_desc": job_desc,
            "shortlisted_candidates": shortlisted_candidates,
            "interview_status": interview_status,
            "feedback_summary": feedback_summary
        })
    else:
        return jsonify({"message": "Candidate not shortlisted"}), 400

@app.route('/schedule_interview', methods=['POST'])
def schedule_interview_api():
    data = request.json
    candidate_name = data.get("candidate_name")
    interviewer_name = data.get("interviewer_name", "HR Team")
    date_time = data.get("date_time")

    if not candidate_name or not date_time:
        return jsonify({"error": "Candidate name and date_time required"}), 400

    status = schedule_interview(candidate_name, interviewer_name, date_time)
    return jsonify({"interview_status": status})

# def main():
#     app.run(debug=True)

# if __name__ == "__main__":
#     main()


# print("🔥 HR Agent System Starting...")
#     start_interface(app)  # UI Load करने के लिए
#     app.run(debug=True, use_reloader=False)  # Flask Server Run करो

# if __name__ == "__main__":
#     main()
# def main():
   
# def main():
#     start_interface(app)
#     app.run(debug=True)

# if __name__ == "__main__":
#     main()

# if __name__ == "__main__":
#     start_interface(app)
#     app.run(debug=True)



# if __name__ == "__main__":
#     app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    print("🔥 Starting HR Agent System...")
    start_interface # UI Start Karo
    app.run(debug=True, use_reloader=False)  # Flask Server Run Karo
