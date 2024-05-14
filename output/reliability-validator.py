# Import Guard and Validator
from guardrails.hub import WikiProvenance
from guardrails import Guard

# Use the Guard with the validator
guard = Guard().use(
    WikiProvenance,
    topic_name="Apple company",
    validation_method="sentence",
    llm_callable="gpt-3.5-turbo",
    on_fail="exception"
)

# Test passing response
guard.validate("Apple was founded by Steve Jobs in April 1976.", metadata={"pass_on_invalid": True})  # Pass

# Test failing response
try:
    guard.validate("Ratan Tata founded Apple in September 1998 as a fruit selling company.")  # Fail
except Exception as e:
    print(e)
