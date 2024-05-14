# infoshare-2024

Code snippets from my talk at Infoshare 2024 (Poland)

## Setup

### Pre-requisites

Python 3
Virtual Env `pip install virtualenv`

### Installing required dependencies

```
python3 -m venv ./demo-env
source demo-env/bin/activate
pip install requirements.txt
guardrails hub install hub://guardrails/similar_to_document
guardrails hub install hub://guardrails/wiki_provenance
guardrails hub install hub://cartesia/quotes_price
guardrails hub install hub://guardrails/competitor_check
```

## Examples

### Example 1

Output String Evaluation

```
OPENAI_API_KEY=[YOUR_OPENAI_KEY] python ./output/1-output-string-evaluation.py
```

### Example 2

Similarity Validators

```
python ./output/2-similarity-validator.py
```

### Example 3

Reliability

```
OPENAI_API_KEY=[YOUR_OPENAI_KEY] python ./output/3-reliability-validator.py
```

### Example 4

Business Domain Logic

```
python ./output/4-business-domain-validator.py
```

### Example 5

Business Domain Logic 2

```
python ./output/5-business-domain-2-validator.py
```

### Example 6

Constitutional Principles

```
OPENAI_API_KEY=[YOUR_OPENAI_KEY] python ./output/6-constitutional.py
```
