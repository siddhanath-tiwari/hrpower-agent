# def escalation_mechanism(query, resolved):
#     if not resolved:
#         return "Escalated to human representative"
#     return "Resolved by agent"



import logging

logging.basicConfig(level=logging.INFO)

def escalation_mechanism(query, resolved):
    if not resolved:
        logging.info(f"Query Escalated: {query}")
        return "Escalated to human representative"
    
    logging.info(f"Query Resolved: {query}")
    return "Resolved by agent"
