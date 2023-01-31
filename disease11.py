import streamlit as st

symptoms = []
diseases = {
    "fever": ["influenza", "malaria"],
    "headache": ["migraine", "tension headache"],
    "cough": ["cold", "bronchitis"],
    "body ache": ["influenza", "malaria"],
    "runny nose": ["cold"],
}

def diagnose_disease():
    symptom = st.text_input("Enter a symptom (or 'done' to finish):")
    if symptom == "done":
        return
    symptoms.append(symptom)
    if st.button("Add another symptom"):
        diagnose_disease()
    
    possible_diseases = []
    for symptom in symptoms:
        if symptom in diseases:
            possible_diseases += diseases[symptom]
    
    st.write("Possible diseases:", set(possible_diseases))

diagnose_disease()
