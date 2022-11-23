# importing useful libraries
import streamlit as st
import base64
import pickle
import sklearn
from nltk.stem.porter import PorterStemmer
import nltk
nltk.download('punkt')
import re
import string
nltk.download('stopwords')
from nltk.corpus import stopwords
from scipy.sparse import hstack
ps = PorterStemmer()
# adding background image in webpage
def add_bg_from_local(image_file):
    '''
    Function to add the background image in the app
    '''
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(     f"""     <style>
        .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """, unsafe_allow_html=True)
add_bg_from_local('bg_img.PNG')



# Data Preprocesing Function
def data_preprocessing(text):
    '''
    Function to prepreocess and clean the data
    '''

    # lowercasing the text
    text = text.lower()

    # Expanding Contractions(Decontractions)
    def decontracted(text):
        '''
        Function to expand the contractions
        '''
        # specific
        text = re.sub(r"won't", "will not", text)
        text = re.sub(r"can\'t", "can not", text)

        # general
        text = re.sub(r"n\'t", " not", text)
        text = re.sub(r"\'re", " are", text)
        text = re.sub(r"\'s", " is", text)
        text = re.sub(r"\'d", " would", text)
        text = re.sub(r"\'ll", " will", text)
        text = re.sub(r"\'t", " not", text)
        text = re.sub(r"\'ve", " have", text)
        text = re.sub(r"\'m", " am", text)
        return text
    text = decontracted(text)

    # remove text in square brackets
    text = re.sub('\[.*?\]', '', text)

    # remove links
    text = re.sub('https?://\S+|www\.\S+', '', text)

    # remove punctuation and special characters
    def remove_punctuation(text):
        '''
        Function to remove special character and punctuation from text
        '''
        text = nltk.word_tokenize(text)
        lst = []
        for i in text:
            if i not in string.punctuation:
                lst.append(i)
        text = lst[:]
        return ' '.join(lst)
    text = remove_punctuation(text)

    # remove stopwords
    def remove_stopwords(text):
        '''
        Function to rmove stopwords from a given text
        '''
        lst = []
        for char in text.split():
            if char not in stopwords.words('english'):
                lst.append(char)
        return ' '.join(lst)

    text = remove_stopwords(text)

    # remove digits
    def remove_digits(text):
        '''
        Fuction to remove digits from a given text
        '''
        lst = []
        for char in text:
            if not char.isdigit():
                lst.append(char)
        return ''.join(lst)
    text = remove_digits(text)

    # remove everything except alphabet
    text = re.sub(r'[^a-zA-Z ]+', '', text)

    # remove extra spaces from the text
    text = re.sub(' +', ' ', text)

    # Stemming
    text = ' '.join(ps.stem(word) for word in text.split(' '))

    return text


# Function to compute Digits Count Feature
def digits_count(string):
    '''
    Function to compute number of digits in a given text
    '''
    digit_count = 0
    for i in range(len(string)):
        if (string[i].isalpha()):
            continue
        elif (string[i].isdigit()):
            digit_count += 1
        elif (string[i] == ' '):
            continue
        else:
            continue
    return digit_count

# Loading Tfidf Vectorizer and Model
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


# Title
st.markdown("<h1 style='text-align:left ; color: white;position:relative;'>SMS Spam Detector</h1>", unsafe_allow_html=True)


#Textbox
input_sms = st.text_area("Enter the message")

# Predict Button
# After Clicking on Predict button
   # 1.Compute digit count feature from message
   # 2.Preprocess the input message
   # 3.Compute Length Feature
   # 4.Vectorize text (tfidf)
   # 5.Stacking features (vectorizer + length + digits_count)
   # 6.predict
   # 7.Display (Ham or Spam)




if st.button('Detect'):
    # Computing Length feature from input message
    length = len(input_sms)

    # Computing digit count feature from input message
    digits = digits_count(input_sms)

    # Text preprocessing
    transformed_sms = data_preprocessing(input_sms)

    # Computing Length feature from input message
    length = len(input_sms)

    # Vectorizing the text data
    vectorizer = tfidf.transform([transformed_sms])

    # Stacking Features
    features = hstack([vectorizer,length,digits]).toarray()

    # Prediction
    result = model.predict(features)[0]

    # Probability
    probability_spam = model.predict_proba(features)[0][1]
    probability_ham = model.predict_proba(features)[0][0]




    if  input_sms == "":
        st.error("Please Enter the Message!")


    elif result == 1:
        st.markdown("<h3 style='text-align:left ; color: red;'> SPAM </h3>", unsafe_allow_html=True)
        # st.markdown("<h5 style='text-align:left ; color: white;'>Probability : {}</h3>".format(probability_spam), unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='text-align:left ; color: white;'>NOT spam </h3>",
                    unsafe_allow_html=True)
        # st.markdown("<h5 style='text-align:left ; color: white;'>Probability : {}</h3>".format(probability_ham),
        #            unsafe_allow_html=True)