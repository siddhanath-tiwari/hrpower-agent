# test_customer_support_agent.py
import unittest
from customer_support_agent.document_understanding import document_understanding
from customer_support_agent.query_handling import query_handling
from customer_support_agent.escalation_mechanism import escalation_mechanism

class TestCustomerSupportAgent(unittest.TestCase):
    def test_document_understanding(self):
        document = "Company help document content goes here."
        doc = document_understanding(document)
        self.assertIsNotNone(doc)

    def test_query_handling(self):
        query = "What are the company policies on leave?"
        context = "Company policies on leave include paid leave, sick leave, and casual leave."
        answer = query_handling(query, context)
        self.assertIn("leave", answer)

    def test_escalation_mechanism(self):
        query = "Complex query"
        status = escalation_mechanism(query, resolved=False)
        self.assertEqual(status, "Escalated to human representative")

if __name__ == '__main__':
    unittest.main()