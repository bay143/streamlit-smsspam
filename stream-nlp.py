import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from PIL import Image


# load save model
model_fraud = pickle.load(open('model_fraud.sav' , 'rb'))

tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("new_selected_feature_tf-idf.sav1","rb"))))

# Load gambar
image = Image.open('logo.png')

# Judul halaman
st.title('Identifikasi SMS Spam')

# Baris kosong untuk memisahkan judul dan gambar
st.write("")

# Tampilkan gambar
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(image, use_column_width=False)

clean_teks = st.text_input('Masukkan Teks SMS')

fraud_detection = ''

if st.button('Hasil Identifikasi'):
    predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))

    if (predict_fraud == 0):
        fraud_detection = 'SMS Normal'
    elif(predict_fraud == 1):
        fraud_detection = 'SMS Penipuan'
    else :
        fraud_detection = 'SMS Promo'

st.success(fraud_detection)

