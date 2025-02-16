from transformers import pipeline

def query_handling(query, context):
    qa_pipeline = pipeline("question-answering")
    result = qa_pipeline(question=query, context=context)
    return result['answer']




# from transformers import pipeline

# # Default DistilBERT model
# qa_pipeline_distilbert = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# # RoBERTa-based model for better accuracy
# qa_pipeline_roberta = pipeline("question-answering", model="deepset/roberta-base-squad2")

# # Example usage
# query = "Who developed Python?"
# context = "Python was created by Guido van Rossum and first released in 1991."

# # Using DistilBERT
# print("DistilBERT Answer:", qa_pipeline_distilbert(question=query, context=context)['answer'])

# # Using RoBERTa
# print("RoBERTa Answer:", qa_pipeline_roberta(question=query, context=context)['answer'])
