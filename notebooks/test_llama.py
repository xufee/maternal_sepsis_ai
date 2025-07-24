from llama_explainer import generate_explanation

fake_patient = {
    "WBC": 17.2,
    "Temperature_C": 39.4,
    "Blood_Loss_ml": 850,
    "C_section_type": "Emergency",
    "Antibiotics_given": False
}

print("🧪 Sending data to TinyLLaMA...\n")
explanation = generate_explanation(fake_patient)

print("🧠 AI Explanation:\n", explanation)



