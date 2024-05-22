from langchain.evaluation import load_evaluator

from header import print_art, print_json, print_exception

print_art('Demo - Comparison')

llm_answer1 = ("""
Hello,

I have compiled a list of meeting time suggestions according to the requested parameters.

Based on that, the list is:

- Monday 20st May, 15:00-15:30
- Tuesday 21st May, 16:00-16:30

Please, read the provided list and let me know what is your preference. Including a confirmation of what's your ideal slot.

Thanks
""")

llm_answer2 = ("""
Hello,

Find the provided options:

- Monday 20st May, 15:00-15:30
- Tuesday 21st May, 16:00-16:30

Please, let me know which one do you prefer.
""")

guardrails = {
    "simplicity": "Is the language straightforward and unpretentious?",
    "clarity": "Are the sentences clear and easy to understand?",
    "precision": "Is the writing precise, with no unnecessary words or details?"
}

evaluator = load_evaluator("pairwise_string", criteria=guardrails)

result = evaluator.evaluate_string_pairs(
    prediction=llm_answer1,
    prediction_b=llm_answer2,
    input="Find me some meeting time suggestions!",
)

print_json(guardrails, 'white', 'blue')
print()
print_json(llm_answer1, 'black', 'yellow')
print()
print_json(llm_answer2, 'black', 'yellow')
print()

print_json(result, 'white', 'green')
