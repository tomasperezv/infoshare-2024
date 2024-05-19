from guardrails.hub import DetectPII
from guardrails import Guard
from header import print_art, print_json, print_exception

guardrails = [
    'EMAIL_ADDRESS',
    'PHONE_NUMBER'
]

llm_answer = """
Hi,

You can reach out to your customer support representative support@gokatch.ai

Thanks
"""

print_json(guardrails, 'white', 'blue')
print('\n')
print_json(llm_answer, 'black', 'yellow')

guard = Guard().use(DetectPII, guardrails, "exception")

try:
    guard.validate(llm_answer)
except Exception as e:
    print_exception(e)

guard = Guard().use(DetectPII, guardrails, "fix")
res = guard.validate(llm_answer)

print()
print_json(res.validated_output, 'white', 'green')
