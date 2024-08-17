import pytest
#Testing the rule-based system with pytest
from src.rule_based_system import predict_relevance

def test_predict_relevance():
    # Test case where each 'Content' column contains a keyword
    document = {"Content": "Payment Transactions are crucial for compliance."}
    assert predict_relevance(document) == True, "The document should be considered relevant due to the presence of the keyword 'Payment Transactions'."

    # Test case where 'Content' does not contain any keywords
    document = {"Content": "This document discusses unrelated topics."}
    assert predict_relevance(document) == False, "The document should not be considered relevant as it contains no keywords from the list of relevant keywords."

    # Additional test cases for comprehensive coverage
    # Test case with a keyword in different case
    document = {"Content": "The central bank is mentioned here."}
    assert predict_relevance(document) == True, "The document should be considered relevant due to the presence of the keyword 'Central Bank'."

    # Test case with multiple keywords
    document = {"Content": "Assets and Securities and Exchange are key topics."}
    assert predict_relevance(document) == True, "The document should be considered relevant due to the presence of multiple keywords."

    # Test case with no content
    document = {"Content": ""}
    assert predict_relevance(document) == False, "An empty document should not be considered relevant."

    # Test case with None content
    document = {"Content": None}
    assert predict_relevance(document) == False, "A document with None as content should not be considered relevant."
