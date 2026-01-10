import streamlit as st
import joblib
import os

st.set_page_config(page_title="SPAM DETEKTOR", page_icon="K")

st.title("SMS SPAM DETEKTOR")

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "model_sms.pkl")
model_vect = os.path.join(current_dir, "vectorizer_sms.pkl")

try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(model_vect)

except:
    st.error("Model tidak ditemukan!")
    st.stop()

sms_user = st.text_area("Masukkan SMS : ")

if st.button("Analisa"):
    if sms_user:
        sms_angka = vectorizer.transform([sms_user])
        hasil = model.predict(sms_angka)[0]

        proba = model.predict_proba(sms_angka).max()

        st.write(f"Tingkat keyakinan AI : {proba*100:.0f}")
        st.progress(int(proba*100))


        if hasil == 0:
            st.success("SMS Aman")

        elif hasil == 1:
            st.error("SMS PENIPUAN! Hati hati")
        
        elif hasil == 2:
            st.warning("SMS Promo Operator")
    



