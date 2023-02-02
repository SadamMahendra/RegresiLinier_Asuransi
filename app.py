import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in = open('model_uas.pkl', 'rb')
lr = pickle.load(pickle_in)

def welcome():
    return 'Selamat Datang'

def prediction(age, sex, bmi, children, smoker):

    prediction = lr.predict([[age, sex, bmi, children, smoker]])
    print(prediction)
    return prediction

def main():
    st.title("Aplikasi Prediksi Premi Asuransi Dengan Algoritma Linier Regression")
    st.markdown('Muhammad Sadam Mahendra (2019230044) | Universitas Darma Persada | UAS Datamining')
    st.write('\n')
    st.markdown('Silakan isi form berikut terlebih dahulu :')
    
    st.write('\n')
    age = st.number_input("age", 0)
    sex = st.number_input("sex", 0)
    bmi = st.number_input("bmi", 0)
    children = st.number_input("children", 0)
    smoker = st.number_input("smoker", 0)
    result =""
    
    if st.button("PREDIKSI"):
        result = prediction(age, sex, bmi, children, smoker)
    st.success('Hasil Prediksi Premi Asuransi anda = {}'.format(result))
    
if __name__=='__main__':
    main()