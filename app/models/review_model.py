from transformers import pipeline

def suggest_improvements(code_snippet):
    model = pipeline("text2text-generation", model="t5-small")
    input_text = f"Improve this code: {code_snippet}"
    result = model(input_text, max_length=100, truncation=True)
    return result[0]['generated_text']