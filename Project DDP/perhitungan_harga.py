import streamlit as st

st.title("Perhitungan Harga Bensin")
# Memuat CSS
st.markdown(
    """
    <style>
    body {
        background-color: #E9967A;
        font-family: 'Arial', sans-serif;
    }

    h1 {
        color: #E9967A;
        text-align: center;
    }

    .stButton>button {
        background-color: #E9967A;
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

    .stNumberInput, .stSelectbox {
        margin: 10px 0;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        width: 100%;
        max-width: 700px;
    }

    .stSuccess {
        background-color: #dff0d8;
        color: #E9967A;
        padding: 10px;
        border-radius: 5px;
    }

    .stError {
        background-color: #E9967A;
        color: #E9967A;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set judul aplikasi
#st.markdown('<div class="title">Mileage Money</div>', unsafe_allow_html=True)

# Input untuk volume bensin
st.markdown('<div class="input-label">Masukkan volume bensin yang ingin anda beli (dalam liter):</div>', unsafe_allow_html=True)
volume = st.number_input('', min_value=0.0, step=0.1, key="volume_input")

# Input untuk harga per liter bensin
st.markdown('<div class="input-label">Masukkan harga bensin yang sesuai dengan:</div>', unsafe_allow_html=True)
harga_perliter = st.number_input('', min_value=0.0, step=0.01, key='harga_input')

# Hitung total biaya hanya jika volume dan harga lebih dari nol
if volume > 0 and harga_perliter > 0:
    jumlah = volume * harga_perliter
    # Tampilkan total biaya
    st.success(f"Total Harga Bensin Untuk {volume} liter adalah : Rp {jumlah:,.2f}")
else:
    st.write('Silakan masukkan volume dan harga bensin yang valid.')