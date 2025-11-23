# Vityarthi-Project

# Disease Finder - Simple Symptom-Based Disease Prediction

## Introduction
Disease Finder is a simple, command-line Python application designed for educational purposes to demonstrate basic symptom-based disease prediction logic. The project uses a small hard-coded knowledge base of diseases and their associated symptoms. Users input their symptoms as a comma-separated list, and the program predicts the most likely disease by comparing symptom overlaps.

## Features
- Small, predefined database of diseases and symptoms
- User-friendly, interactive command-line interface
- Symptom normalization for flexible input handling
- Calculates match scores based on symptom overlap using set operations
- Identifies and displays the most likely disease along with scores for all diseases
- Clear disclaimer emphasizing educational use only

## How it Works
1. User enters symptoms separated by commas.
2. Input is cleaned and normalized (lowercased, trimmed).
3. The program compares user symptoms with symptoms of each disease.
4. Scores are calculated based on how many symptoms match.
5. The disease with the highest score is presented as the most likely disease.
6. Scores for all diseases are shown for transparency.


## Limitations
- The knowledge base is small and not exhaustive.
- This is not a medical diagnostic tool.
- No support for symptom severity, duration, or machine learning.
- Always consult a healthcare professional for medical advice.

## Future Enhancements
- Expand disease and symptom database.
- Integrate synonym handling and NLP for better symptom matching.
- Add a web or GUI interface for easier access.
- Implement machine learning models for improved predictions.

## License
This project is for educational use and comes without any warranty.

*This tool is a starting point for learning and should not replace professional medical diagnosis.*

