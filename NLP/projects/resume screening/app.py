#imporitng the libraries

import streamlit as st
import pickle 
import re
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words="english")

nltk.download('punkt')
nltk.download('stopwords')

#importing the cliassifier model
clf = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))


def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)  
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText) 
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText

mpp ={6: 'Data Science',
 12: 'HR',
 0: 'Advocate',
 1: 'Arts',
 24: 'Web Designing',
 16: 'Mechanical Engineer',
 22: 'Sales',
 14: 'Health and fitness',
 5: 'Civil Engineer',
 15: 'Java Developer',
 4: 'Business Analyst',
 21: 'SAP Developer',
 2: 'Automation Testing',
 11: 'Electrical Engineering',
 18: 'Operations Manager',
 20: 'Python Developer',
 8: 'DevOps Engineer',
 17: 'Network Security Engineer',
 19: 'PMO',
 7: 'Database',
 13: 'Hadoop',
 10: 'ETL Developer',
 9: 'DotNet Developer',
 3: 'Blockchain',
 23: 'Testing'}

#creating a streamlit app
def main():
    st.title("resume screener app") 
    
    #asking user to upload the resume
    uploaded_file = st.file_uploader("Upload your reseum", type=['pdf', 'txt'])

    #checking if the file is not empty
    if uploaded_file is not None:
        try:
            resume_byte = uploaded_file.read()
            resume_text = resume_byte.decode('utf-8')
        except UnicodeDecodeError:
            #trying latin decoder
            resume_text  = resume_byte.decode('latin-1')
    else:
        return 
    clean_resume = cleanResume(resume_text)
    clean_resume = tfidf.transform([clean_resume])
    prediction_id = clf.predict(clean_resume)[0]
    st.write("job profile : ",mpp[prediction_id])


#python main 
if __name__ == "__main__":
    main()