from langchain.evaluation import load_evaluator
from langchain.evaluation import EvaluatorType
from langchain.evaluation import Criteria

evaluator = load_evaluator("labeled_criteria", criteria=Criteria.CORRECTNESS)

eval_result = evaluator.evaluate_strings(
  prediction="The Eiffel Tower is a famous landmark located in Paris, France. It was completed in 1889 and stands as an iconic symbol of the city. Tourists from all over the world visit the tower to admire its architecture and enjoy the panoramic views of Paris from its observation decks.",
  input="Tell me about the Eiffel Tower.",
  reference="The Eiffel Tower is in France"
)

print(eval_result)
