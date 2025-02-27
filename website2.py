import streamlit as st

st.title("Portal JDM - Informasi dan Galeri Mobil JDM")
st.sidebar.header("Pilih Kategori")
kategori = st.sidebar.selectbox("Kategori", ["Sejarah JDM", "Mobil Legendaris", "Galeri Gambar"])

if kategori == "Sejarah JDM":
    st.header("Sejarah Mobil JDM")
    st.write("JDM (Japanese Domestic Market) adalah istilah untuk mobil yang dibuat khusus untuk pasar Jepang. Mobil JDM terkenal dengan performa tinggi, teknologi canggih, dan desain unik.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/7/73/Nissan_Skyline_R34_GT-R_N%C3%BCr_001.jpg", caption="Nissan Skyline GT-R R34")

elif kategori == "Mobil Legendaris":
    st.header("Mobil JDM Legendaris")
    mobil = st.selectbox("Pilih Mobil", ["Nissan Skyline GT-R", "Toyota Supra MK4", "Mazda RX-7 FD3S", "Honda NSX"])
    gambar = {
        "Nissan Skyline GT-R": "https://upload.wikimedia.org/wikipedia/commons/7/73/Nissan_Skyline_R34_GT-R_N%C3%BCr_001.jpg",
        "Toyota Supra MK4": "https://upload.wikimedia.org/wikipedia/commons/7/72/1994_Toyota_Supra_Sport_Roof_in_Red%2C_front_left.jpg",
        "Mazda RX-7 FD3S": "https://upload.wikimedia.org/wikipedia/commons/1/10/Tuned_Mazda_RX-7_Type_RB_%28GF-FD3S%29_front.jpg",
        "Honda NSX": "https://upload.wikimedia.org/wikipedia/commons/a/a1/Honda_NSX_reg_1991_2977_cc.JPG"
    }
    st.image(gambar[mobil], caption=mobil)
    st.write(f"**{mobil}** adalah salah satu ikon dari dunia JDM dengan performa luar biasa dan desain klasik.")

elif kategori == "Galeri Gambar":
    st.header("Galeri Mobil JDM")
    st.image(["https://upload.wikimedia.org/wikipedia/commons/7/73/Nissan_Skyline_R34_GT-R_N%C3%BCr_001.jpg", 
              "https://upload.wikimedia.org/wikipedia/commons/7/72/1994_Toyota_Supra_Sport_Roof_in_Red%2C_front_left.jpg", 
              "https://upload.wikimedia.org/wikipedia/commons/1/10/Tuned_Mazda_RX-7_Type_RB_%28GF-FD3S%29_front.jpg", 
              "https://upload.wikimedia.org/wikipedia/commons/a/a1/Honda_NSX_reg_1991_2977_cc.JPG"], 
             caption=["Nissan Skyline GT-R R34", "Toyota Supra MK4", "Mazda RX-7 FD3S", "Honda NSX"], width=300)

st.write("\n🚗 Nikmati dunia JDM dan eksplorasi mobil-mobil legendaris Jepang!")
