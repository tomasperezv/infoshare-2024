# Import Guard and Validator
from guardrails import Guard
from guardrails.hub import CompetitorCheck

from header import print_art, print_json, print_exception

print_art('Demo - Business Logic 2')


# Setup Guard
guard = Guard().use(CompetitorCheck, ["Apple", "Samsung"], "exception")

response = guard.validate(
    "The apple doesn't fall far from the tree."
)  # Validator passes

try:
    response = guard.validate("Apple just released a new iPhone.")  # Validator fails
except Exception as e:
    print_exception(e)
