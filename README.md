# Resume Screening NLP app

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
- Text Preprocessing: Uses regex patterns to clean resume text by removing:
  - URLs, special characters
  - Social media handles
  - Extra whitespace
  - Non-ASCII characters

- ML Pipeline**:
  - Feature extraction using TF-IDF Vectorization
  - Multi-class classification using KNeighbors Classifier
  - OneVsRest strategy for handling multiple categories
  - Achieved ~98.7% accuracy on test data
```

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



# Named Entity Recognition Web App

A Flask-based web application that performs Named Entity Recognition (NER) on uploaded text files using spaCy. The app identifies and visualizes entities like person names, organizations, locations, and more.

## Directory Structure
```
Named_Entity_Recognition/
├── app.py              # Flask application with NER logic
├── templates/          # Frontend templates
│   └── index.html     # Main UI template
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Requirements
- Python 3.7+
- Flask
- spaCy
- en_core_web_sm model

## Setup Instructions

1. Clone the repository:
```bash
git clone [your-repo-url]
cd Named_Entity_Recognition
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`
3. Upload a text file
4. Click "Get Entity" to view NER results

## Features
- Text file upload support
- Real-time NER processing
- Visual entity highlighting
- Support for multiple entity types (Person, Organization, Location, etc.)

## Technologies Used
- Flask: Web framework
- spaCy: NLP and NER processing
- displaCy: Entity visualization
- Bootstrap: Frontend styling
