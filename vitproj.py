
# disease_finder.py

# -----------------------------
# 1. Toy knowledge base
# -----------------------------
disease_symptoms = {
    "Common Cold": [
        "cough", "sore throat", "runny nose", "sneezing", "mild fever", "headache"
    ],
    "Flu": [
        "high fever", "chills", "body ache", "fatigue", "cough", "headache"
    ],
    "Migraine": [
        "headache", "nausea", "vomiting", "sensitivity to light", "sensitivity to sound"
    ],
    "Food Poisoning": [
        "vomiting", "nausea", "diarrhea", "stomach pain", "fever"
    ],
    "Dengue": [
        "high fever", "severe headache", "joint pain", "muscle pain", "rash"
    ],
    "COVID-19": [
        "fever", "dry cough", "tiredness", "loss of taste", "loss of smell", "shortness of breath"
    ]
}

# -----------------------------
# 2. Helper functions
# -----------------------------
def clean_symptom(symptom: str) -> str:
    """Normalize symptom text."""
    return symptom.strip().lower()

def get_user_symptoms():
    print("Enter your symptoms separated by commas.")
    print("Example: fever, cough, headache")
    raw = input("Symptoms: ")
    # split and clean
    return [clean_symptom(s) for s in raw.split(",") if s.strip()]

def score_diseases(user_symptoms):
    """
    For each disease, count how many symptoms match the user symptoms.
    Returns a dict: {disease: score}
    """
    scores = {}
    for disease, sym_list in disease_symptoms.items():
        normalized = [clean_symptom(s) for s in sym_list]
        # intersection size = score
        match_count = len(set(user_symptoms) & set(normalized))
        scores[disease] = match_count
    return scores

def predict_disease(user_symptoms, min_matches=1):
    scores = score_diseases(user_symptoms)

    # find disease with maximum score
    best_disease = None
    best_score = 0
    for disease, score in scores.items():
        if score > best_score:
            best_score = score
            best_disease = disease

    # if no disease has enough matches, return None
    if best_score < min_matches:
        return None, scores
    return best_disease, scores

# -----------------------------
# 3. Main program
# -----------------------------
def main():
    print("=== Simple Disease Finder (Educational Only) ===")
    user_symptoms = get_user_symptoms()

    if not user_symptoms:
        print("No symptoms entered. Exiting.")
        return

    disease, scores = predict_disease(user_symptoms, min_matches=1)

    print("\nYour symptoms:", ", ".join(user_symptoms))

    if disease is None:
        print("No likely disease found in the small knowledge base.")
    else:
        print(f"\nMost likely disease (from this small dataset): {disease}")
        print("Match score:", scores[disease])

    print("\nOther disease match scores:")
    for d, s in scores.items():
        print(f"  {d}: {s}")

    print("\nNote: This is a simple educational project and NOT a real medical tool.")

if __name__ == "__main__":
    main()