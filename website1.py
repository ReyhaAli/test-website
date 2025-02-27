import streamlit as st

def konversi_panjang(nilai, dari, ke):
    konversi = {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Milimeter": 1000
    }
    return nilai * (konversi[ke] / konversi[dari])

def konversi_berat(nilai, dari, ke):
    konversi = {
        "Kilogram": 1,
        "Gram": 1000,
        "Miligram": 1_000_000,
        "Ton": 0.001
    }
    return nilai * (konversi[ke] / konversi[dari])

def konversi_suhu(nilai, dari, ke):
    if dari == "Celsius":
        return nilai if ke == "Celsius" else nilai * 9/5 + 32 if ke == "Fahrenheit" else nilai + 273.15
    elif dari == "Fahrenheit":
        return (nilai - 32) * 5/9 if ke == "Celsius" else nilai if ke == "Fahrenheit" else (nilai - 32) * 5/9 + 273.15
    elif dari == "Kelvin":
        return nilai - 273.15 if ke == "Celsius" else (nilai - 273.15) * 9/5 + 32 if ke == "Fahrenheit" else nilai

st.title("Aplikasi Konversi Satuan")
st.sidebar.header("Pilih Kategori Konversi")
kategori = st.sidebar.selectbox("Kategori", ["Panjang", "Berat", "Suhu"])

if kategori == "Panjang":
    satuan = ["Meter", "Kilometer", "Centimeter", "Milimeter"]
    nilai = st.number_input("Masukkan nilai:", min_value=0.0)
    dari = st.selectbox("Dari", satuan)
    ke = st.selectbox("Ke", satuan)
    hasil = konversi_panjang(nilai, dari, ke)
elif kategori == "Berat":
    satuan = ["Kilogram", "Gram", "Miligram", "Ton"]
    nilai = st.number_input("Masukkan nilai:", min_value=0.0)
    dari = st.selectbox("Dari", satuan)
    ke = st.selectbox("Ke", satuan)
    hasil = konversi_berat(nilai, dari, ke)
elif kategori == "Suhu":
    satuan = ["Celsius", "Fahrenheit", "Kelvin"]
    nilai = st.number_input("Masukkan nilai:")
    dari = st.selectbox("Dari", satuan)
    ke = st.selectbox("Ke", satuan)
    hasil = konversi_suhu(nilai, dari, ke)

st.write(f"**Hasil Konversi:** {hasil} {ke}")
