# def feedback_loop(interview_feedback):
#     feedback_summary = "Feedback Summary:\n"
#     for feedback in interview_feedback:
#         feedback_summary += f"{feedback}\n"
#     return feedback_summary

from transformers import pipeline

def feedback_loop(interview_feedback):
    if not interview_feedback:
        return "No feedback provided."

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    full_feedback = " ".join(interview_feedback)

    summary = summarizer(full_feedback, max_length=50, min_length=10, do_sample=False)
    # summary = summarizer(full_feedback, max_length=30, min_length=5, do_sample=False, truncation=True)

    return summary[0]['summary_text']

# Example usage
interview_feedback = [
    "The candidate has strong technical skills in Python.",
    "Good communication skills, but needs improvement in problem-solving.",
    "Overall a good fit for the team."
]

summary = feedback_loop(interview_feedback)
print(summary)
