from guardrails.hub import RedundantSentences
from guardrails import Guard, OnFailAction

from header import print_art, print_json, print_exception

llm_answer = """
Thanks for your inquiry.

You can reach out to your customer support representative support@gokatch.ai

We are currently checking your case.

You can reach out to your customer support representative support@gokatch.ai
"""

print_json(llm_answer, 'black', 'yellow')

guard = Guard().use(RedundantSentences, on_fail="exception")

try:
    guard.validate(llm_answer)
except Exception as e:
    print()
    print_exception(e)

guard = Guard().use(RedundantSentences, on_fail="fix")
res = guard.validate(llm_answer)
print()
print_json(res.validated_output, 'white', 'green')
