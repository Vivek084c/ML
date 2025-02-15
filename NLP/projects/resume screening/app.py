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


#creating a streamlit app
def main():
    st.title("resume screener app") 
    
    #asking user to upload the resume
    st.file_uploader("Upload your reseum", type=['pdf', 'txt'])


#python main 
if __name__ == "__main__":
    main()