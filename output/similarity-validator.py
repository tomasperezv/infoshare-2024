# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import SimilarToDocument

from header import print_art, print_json, print_exception

print_art('Demo - Similarity')

document="""
    Our support team is available 24/7 via phone, email, and live chat. We aim to resolve issues promptly
    and ensure customer satisfaction. Visit our FAQ section for quick answers to common questions.
    """
llm_answer= """
    Hey there! Need help? Our customer service folks are around, but mostly during the day. 
    You can shoot us an email or hit us up on chat. For quick stuff, check out our FAQ page!
"""

print_json(document, 'white', 'blue')
print('\n')
print_json(llm_answer, 'black', 'yellow')

guard = Guard().use(
    SimilarToDocument,
    document=document,
    threshold=0.7,
    model="all-MiniLM-L6-v2",
    on_fail="exception",
)

try:
    guard.validate(llm_answer)
except Exception as e:
  print_exception(e)

#print(guard.history.last.tree)
