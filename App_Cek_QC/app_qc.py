import streamlit as st
import joblib

st.set_page_config(page_title="AI QC", page_icon="🤖")
st.header("Sistem Prediksi QC")

try:
    model = joblib.load("../model_qc.pkl")

except:
    st.error("Model tidak ditemukan!")
    st.stop()

st.sidebar.header("Input Data Baru")

input_suhu = st.sidebar.slider("Suhu (Celcius): ", 50, 150)
input_tekanan = st.sidebar.number_input("Tekanan (Bar): ", min_value=0)
input_waktu = st.sidebar.number_input("Waktu Proses (Detik) : ", min_value=0)

if st.sidebar.button("Cek Produk"):

    data_baru = [[input_suhu, input_tekanan, input_waktu]]
    hasil = model.predict(data_baru)[0]
    prob = model.predict_proba(data_baru)[0][0]

    st.write(f"Probabilitas Cacat (NG) : {prob * 100:.0f}%")
    st.progress(int(prob*100))

    if hasil == 0:
        st.error("⛔ STOP MESIN! Kemungkinan Produk NG")
    
    else:
        st.success("✅ Lanjutkan Proses")
        st.balloons()