import streamlit as st
st.markdown("""
    <style>
        body {
            background-color: #f0f2f5;
            font-family: 'Arial', sans-serif;
        }
        .title {
            font-size: 40px;
            color: #000000;
            text-align: center;
            margin-bottom: 20px;
        }
        .input-label {
            font-size: 20px;
            color: #333;
            margin-top: 20px;
        }
        .result {
            font-size: 24px;
            color: #FF5733;
            text-align: center;
            margin-top: 20px;
            font-weight: bold;
        }
        .radio-label {
            font-size: 18px;
            color: #333;
            margin-top: 20px;
        }
      .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
        .stButton:hover {
            background-color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class= "title">Estimasi Biaya Perjalanan</div>', unsafe_allow_html=True)

def estimasi_biaya_perjalanan():
    
    # Input biaya perjalanan
    biaya_transportasi = st.number_input("Biaya Transportasi: Rp ")

    biaya_akomodasi = st.number_input("Biaya Akomodasi: Rp ")

    biaya_makan = st.number_input("Biaya Makan: Rp ")

    biaya_lain = st.number_input("Biaya Lain-lain: Rp ")
    
    # Hitung total biaya
    if st.button("Hitung Biaya"):
            total_biaya = biaya_transportasi + biaya_akomodasi + biaya_makan + biaya_lain
            st.success(f"Estimasi untuk biaya prjalanan adalah Rp.{total_biaya:,.2f}")
    else:
            st.error("Mohon isi semua input biaya perjalanan")

estimasi_biaya_perjalanan()