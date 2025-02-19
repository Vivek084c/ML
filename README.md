## **Directory Structure**
|– data/                   
|– models/                 
|– scripts/                
|– dvc.yaml                
|– params.yaml             
|– requirements.txt        
|– README.md               

The project is organized as follows:

## **MLOps with DVC and Amazon S3

This repository contains a subproject dedicated to implementing MLOps practices using DVC for data versioning and Amazon S3 for data storage. The goal of this project is to streamline the machine learning lifecycle by ensuring reproducibility, scalability, and efficient data management.

# **Project Overview

This subproject focuses on:
	•	Setting up and managing a data pipeline with DVC.
Streamline the handling of large datasets with DVC’s efficient tracking and version control.
	•	Storing and versioning datasets in Amazon S3.
Leverage cloud storage to maintain dataset accessibility and scalability.
	•	Automating workflows for machine learning models.
Enable reproducible pipelines for training, evaluation, and deployment.

Features
	•	Data Versioning: Track and manage changes to datasets using DVC.
	•	Cloud Storage: Utilize Amazon S3 for secure and scalable dataset storage.
	•	Reproducible Pipelines: Automate key stages of the ML lifecycle, from data preparation to model deployment.


## ** Resume Screening NLP app**

```markdown
# Resume Screening Project

## Directory Structure

NLP/projects/resume screening/
├── app.py                 # Streamlit web application
├── resume_screening.ipynb # Training notebook
├── clf.pkl               # Trained classifier model
├── tfidf.pkl            # TF-IDF vectorizer
└── data.csv             # Training dataset (gitignored)


## Project Overview
This project implements an automated resume screening system that classifies resumes into 25 different job categories including Data Science, HR, Software Development, etc. The system uses Natural Language Processing (NLP) and Machine Learning to analyze and categorize resumes.

## Technical Implementation
- **Text Preprocessing**: Uses regex patterns to clean resume text by removing:
  - URLs, special characters
  - Social media handles
  - Extra whitespace
  - Non-ASCII characters

- **ML Pipeline**:
  - Feature extraction using TF-IDF Vectorization
  - Multi-class classification using KNeighbors Classifier
  - OneVsRest strategy for handling multiple categories
  - Achieved ~98.7% accuracy on test data

## How to Run

1. **Setup Environment**
```bash
pip install streamlit nltk scikit-learn
```

2. **Download Required NLTK Data**
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

3. **Run the Web Application**
```bash
streamlit run app.py
```

## Usage
1. Launch the Streamlit app
2. Upload a resume in PDF or TXT format
3. The system will automatically classify the resume into one of 25 job categories

## Model Training
To retrain the model:
1. Place your labeled resume dataset as 'data.csv'
2. Run the resume_screening.ipynb notebook
3. New model files (clf.pkl and tfidf.pkl) will be generated
```
