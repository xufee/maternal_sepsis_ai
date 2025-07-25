# SepsisGuard: AI-Powered Early Warning System for Post-Cesarean Sepsis Prediction
by Zainab Umar Faruq FE/23/14748402 &  Umar Lawal Jari FE/23/33736272

# 🏷️ Project Overview
SepsisGuard is a Python-based clinical AI system designed to predict the risk of maternal sepsis in post-cesarean patients. Leveraging synthetic vital signs data, it demonstrates the full machine learning pipeline—from data preprocessing and model training to deployment in a user-friendly Streamlit interface.
The system includes interpretable AI outputs using a large language model (LLM) for transparent, clinician-friendly explanations. Built as a real-world proof-of-concept for clinical decision support, SepsisGuard showcases how AI can empower early intervention, reduce maternal mortality, and enhance trust in AI-driven healthcare.

# 🏷️ The Problem We’re Solving
Maternal sepsis after C-section remains a leading cause of preventable deaths. SepsisGuard uses AI to turn vital signs into early risk alerts.

# 🏷️ Tech Stack
Data: Python Faker synthetic clinical data, Model: Scikit-learn ML classification,  AI: Local LLM- model explanations,  Deployment: Streamlit healthcare dashboard

# 📁 Files Included
maternal_sepsis_dataset.csv — Faker-generated synthetic patient dataset

maternal_sepsis_outcome.ipynb — Exploratory data analysis and model development notebook

sepsis_model.pkl — Trained Random Forest classifier

app.py — Streamlit web interface for sepsis risk prediction



# ⚕️ Deployment Potential in Healthcare Settings
This project demonstrates how machine learning can be used to support early detection of maternal sepsis—a critical issue in many healthcare systems, especially in low-resource settings.

With minimal infrastructure (internet access and a basic computer), this web-based tool can be deployed in hospitals, especially at the Primary and Secondary healthcare levels.

Potential Adoption Pathway:

1. Pilot Testing in hospitals using synthetic or retrospective patient data.

2. Integration with electronic health records (EHRs) to automate risk scoring.

3. Training of clinical staff to use the tool for triage and early decision support.

4. Feedback Loop to retrain and improve the model using local hospital data.

By aiding early recognition of high-risk patients, the tool can reduce delays in diagnosis and treatment—ultimately improving maternal outcomes and saving lives.




# 🧪 Proof of Concept Highlights
Predicts maternal sepsis risk post-C-section using vital signs.

End-to-end ML pipeline with training, evaluation, and deployment.

LLM-based explanations for clinical interpretability.

Streamlit app enables lightweight, real-time use.

Validates synthetic data for health AI prototyping.

# 🔑 Data Keys
Patient_ID — Unique identifier for each patient

Age — Maternal age

Parity — Number of previous births

BMI — Body Mass Index

Pre_existing_conditions — Any known health conditions

C_section_type — Type of cesarean procedure (e.g., elective or emergency)

Duration_surgery_min — Duration of the C-section in minutes

Blood_loss_ml — Estimated blood loss during surgery

Antibiotics_given — Whether prophylactic antibiotics were administered (Yes/No)

Indication_for_C_section — Clinical reason for the procedure

Sepsis_Label — Target variable (1 = Sepsis, 0 = No Sepsis)




# 3-MINUTE VIDEO SUNMISSION
https://drive.google.com/file/d/1nztyjxKTmxxiY3FvWwjks0R9ylB5JL2b/view?usp=drive_link


#3MTTLearningCommunity #My3MTT
