# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import SimilarToDocument

from header import print_art, print_json, print_exception

print_art('Demo - Similarity')

# Initialize The Guard with this validator
guard = Guard().use(
    SimilarToDocument,
    document="""
    Large language models (LLM) are very large deep learning models that are pre-trained on vast amounts of data. 
    The underlying transformer is a set of neural networks that consist of an encoder and a decoder with self-attention capabilities. 
    The encoder and decoder extract meanings from a sequence of text and understand the relationships between words and phrases in it.
    Transformer LLMs are capable of unsupervised training, although a more precise explanation is that transformers perform self-learning. 
    It is through this process that transformers learn to understand basic grammar, languages, and knowledge.
    """,
    threshold=0.7,
    model="all-MiniLM-L6-v2",
    on_fail="exception",
)

# Test passing response
guard.validate(
    """
    Large Language Models (LLMs) are a type of neural network that can be trained on large amounts of text
    data to generate human-like text. These models have been used in a variety of applications, including
    machine translation, text summarization, and question answering.
    """
)  # Pass

try:
    # Test failing response
    guard.validate(
        """
        Graph neural networks (GNNs) are specialized neural networks that can operate on graph data
        structures. These networks are designed to capture the relationships between nodes in a graph
        and can be used for a variety of tasks, including node classification, link prediction, and graph classification.
        """
    )  # Fail
except Exception as e:
  print_exception(e)
