from langchain.evaluation import load_evaluator
from langchain.evaluation import EvaluatorType
from langchain.evaluation import Criteria
from header import print_art, print_json

print_art('Demo - Evaluation')

user_question = "Give me some meeting time suggestions, please"

llm_answer = ("""
How about these times
    - May 21st, 2024 08:00-09:30 CET
    - May 22st, 2024 10:30-11:30 CET
""")

guardrails = ("""
    Facts:
        - Current time is May 19th, 2024, 17:00 CET

    Suggestions should:
        1. Be in the future, 
        2. Within work schedule: 9:00-18:00
    """)

evaluator = load_evaluator("labeled_criteria", criteria=Criteria.CORRECTNESS)

eval_result = evaluator.evaluate_strings(
  input=user_question,
  prediction=llm_answer,
  reference=guardrails
)

print_json(user_question, 'white', 'blue')
print()
print_json(guardrails, 'white', 'blue')
print()
print_json(llm_answer, 'black', 'yellow')
print()

print_json(eval_result, 'white', 'red')
