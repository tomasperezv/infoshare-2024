from guardrails import Guard
from guardrails.hub import QuotesPrice

from header import print_art, print_json, print_exception

print_art('Demo - Business Logic')

# Setup the Guard with the validator
guard = Guard().use(QuotesPrice, on_fail="exception")

guardrails = { 'currency': 'GBP' }
llm_answer = "The new Airpods Max are available at a crazy discount! It's only $9.99!"

print_json(guardrails, 'white', 'blue')
print('\n')
print_json(llm_answer, 'black', 'yellow')

# Test failing response
try:
    response = guard.validate(
        llm_answer,
        metadata=guardrails
    )
except Exception as e:
    print()
    print_exception(e)
