import subprocess

def generate_explanation(clinical_data):
    prompt = f"Explain in 2 sentences, like a doctor talking to a mother:\n{clinical_data}"

    try:
        result = subprocess.run(
    ['ollama', 'run', 'tinyllama'],
    input=prompt,
    capture_output=True,
    text=True,
    encoding='utf-8',
    timeout= 120
)

        return result.stdout.strip()
    except Exception as e:
        return f"Error generating explanation: {str(e)}"



