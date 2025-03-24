# 1)Basic ML Pipeline Implementation using ZenML and MLFlow

## Project Structure
```
MLOPS/mlop_1/
├── src/
│   ├── __init__.py
│   ├── data_ingestion.py
│   ├── data_validation.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│   └── utils.py
├── config/
│   └── config.yaml
├── artifacts/
│   ├── raw_data/
│   ├── processed_data/
│   └── models/
├── notebooks/
│   └── trials.ipynb
├── tests/
│   ├── __init__.py
│   ├── test_data_ingestion.py
│   └── test_model_trainer.py
├── logs/
├── README.md
├── requirements.txt
└── setup.py
```

## Directory Structure Explanation

### Source Code (`src/`)
- `data_ingestion.py`: Handle data loading and initial preprocessing
- `data_validation.py`: Validate data schema and quality
- `data_transformation.py`: Feature engineering and data transformation
- `model_trainer.py`: Model training and evaluation
- `utils.py`: Common utility functions

### Configuration (`config/`)
- `config.yaml`: Configuration parameters for the pipeline

### Artifacts (`artifacts/`)
- `raw_data/`: Store raw input data
- `processed_data/`: Store processed/transformed data
- `models/`: Store trained models

### Notebooks (`notebooks/`)
- `trials.ipynb`: Experimental notebooks for development

### Tests (`tests/`)
- Unit tests for each pipeline component

## Setup Instructions

1. Create Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Mac
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install package in development mode:
```bash
pip install -e .
```

## Usage

1. Update configuration in `config/config.yaml`
2. Run the pipeline:
```bash
python src/model_trainer.py
```

3. Run tests:
```bash
pytest tests/
```

## Project Requirements
```
numpy>=1.21.0
pandas>=1.3.0
scikit-learn>=0.24.2
pytest>=6.2.4
pyyaml>=5.4.1
```

## Logging
- All logs are stored in `logs/` directory
- Logs include timestamp and module information

## Development Guidelines
1. Follow PEP 8 style guide
2. Write unit tests for new features
3. Update requirements.txt when adding new dependencies
4. Document code using docstrings


# NLP Text Preprocessing pipeline using MLFLOW, ZenML and AWS

## Project Overview
This project implements a robust Natural Language Processing (NLP) preprocessing pipeline designed for text classification tasks. It handles text normalization, including lowercase conversion, tokenization, stopword removal, and stemming, while maintaining proper logging and error handling. The pipeline is specifically designed to prepare text data for machine learning models.

## Project Directory Structure

```
mlops_3/
├── data/
│   ├── raw/                  # Directory for original, immutable data
│   │   ├── train.csv        # Raw training dataset
│   │   └── test.csv         # Raw testing dataset
│   ├── interim/             # Intermediate processed data
│   │   ├── train_processed.csv  # Preprocessed training data
│   │   └── test_processed.csv   # Preprocessed testing data
│   └── processed/           # Final, canonical datasets for modeling
│
├── src/
│   ├── __init__.py         # Makes src a Python module
│   ├── data_preprocessing.py # Main preprocessing script
│   └── utils/              # Utility functions and helper modules
│       └── __init__.py
│
├── logs/
│   └── data_preprocessing.log  # Logging output
│
├── tests/                  # Test files directory
│   ├── __init__.py
│   └── test_preprocessing.py
│
├── notebooks/             # Jupyter notebooks for exploration
│   └── data_exploration.ipynb
│
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
└── .gitignore           # Specifies which files Git should ignore
```

## Tech Stack
- **Python 3.x**: Primary programming language for its extensive ML/NLP libraries
- **NLTK**: Natural Language Toolkit for text processing operations
- **pandas**: Efficient data manipulation and CSV handling
- **scikit-learn**: For LabelEncoder and ML utilities
- **logging**: Python's built-in logging for tracking execution flow

### Why This Tech Stack?
- NLTK provides comprehensive text processing tools and is industry-standard
- pandas offers robust DataFrame operations and CSV handling
- scikit-learn integrates well with other ML libraries
- Built-in logging enables better debugging and monitoring

## How It Works
The pipeline reads raw CSV data, applies text preprocessing steps (lowercase conversion, tokenization, stopword removal, stemming), handles target encoding, and saves processed data. It includes error handling and logging throughout the process, making it production-ready and maintainable.

## Reproduction Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd mlops_3
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
```

3. Install dependencies:
```bash
pip install pandas nltk scikit-learn
```

4. Prepare your data:
   - Place your raw data files in `./data/raw/`
   - Required format: CSV files with 'text' and 'target' columns
   - Files should be named 'train.csv' and 'test.csv'

5. Run the preprocessing:
```bash
python src/data_preprocessing.py
```

The processed data will be saved in `./data/interim/` directory.


## Logging
- Logs are stored in `./logs/data_preprocessing.log`
- Includes DEBUG, INFO, and ERROR level logging
- Tracks all major processing steps and errors

## Error Handling
The pipeline includes robust error handling for:
- Missing files
- Empty datasets
- Missing columns
- General processing errors


# 3)Resume Screening NLP app

```markdown
# Resume Screening Project

## Directory Structure

NLP/projects/resume screening/
├── app.py                 # Streamlit web application
├── resume_screening.ipynb # Training notebook
├── clf.pkl               # Trained classifier model
├── tfidf.pkl            # TF-IDF vectorizer
└── data.csv             # Training dataset (gitignored)

```
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



# 4)Named Entity Recognition Web App

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
