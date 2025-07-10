import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model_random_forest.pkl')  # Pastikan file ini ada di folder yang sama

st.title("Prediksi Penyakit Berdasarkan Data Kesehatan")
st.write("Masukkan data kesehatan pasien:")

# Form input
age = st.number_input("Usia (dalam hari)", min_value=1000, max_value=30000, value=18393)
gender = st.selectbox("Jenis Kelamin", options=["Perempuan", "Laki-laki"])
height = st.number_input("Tinggi (cm)", min_value=100, max_value=250, value=165)
weight = st.number_input("Berat (kg)", min_value=20.0, max_value=200.0, value=60.0)
ap_hi = st.number_input("Tekanan Darah Sistolik (atas)", min_value=50, max_value=250, value=120)
ap_lo = st.number_input("Tekanan Darah Diastolik (bawah)", min_value=30, max_value=200, value=80)
cholesterol = st.selectbox("Kadar Kolesterol", options=["Normal", "Di atas normal", "Jauh di atas normal"])
gluc = st.selectbox("Kadar Glukosa", options=["Normal", "Di atas normal", "Jauh di atas normal"])
smoke = st.selectbox("Perokok?", options=["Tidak", "Ya"])
alco = st.selectbox("Konsumsi Alkohol?", options=["Tidak", "Ya"])
active = st.selectbox("Aktif Secara Fisik?", options=["Tidak", "Ya"])
years = st.number_input("Perkiraan Usia (tahun)", min_value=1, max_value=120, value=50)

# Konversi input ke format numerik
input_data = np.array([[
    age,
    2 if gender == "Perempuan" else 1,
    height,
    weight,
    ap_hi,
    ap_lo,
    ["Normal", "Di atas normal", "Jauh di atas normal"].index(cholesterol) + 1,
    ["Normal", "Di atas normal", "Jauh di atas normal"].index(gluc) + 1,
    1 if smoke == "Ya" else 0,
    1 if alco == "Ya" else 0,
    1 if active == "Ya" else 0,
    years
]])

# Prediksi
if st.button("Prediksi Penyakit"):
    hasil = model.predict(input_data)
    if hasil[0] == 1:
        st.error("⚠️ Pasien berisiko memiliki penyakit!")
    else:
        st.success("✅ Pasien diperkirakan sehat.")
