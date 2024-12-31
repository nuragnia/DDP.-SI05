import streamlit as st

# Fungsi untuk menghitung biaya bensin
def hitung_biaya(jarak, konsumsi_per_liter, harga_per_liter):
    return (jarak / konsumsi_per_liter) * harga_per_liter

# Informasi harga bensin (per liter dalam Rupiah)
harga_bensin = {
    "Pertamax": 13500,
    "Pertalite": 11000,
    "Pertamax Turbo": 16000
}

# Konsumsi rata-rata kendaraan per liter (km/liter)
konsumsi_bensin = {
    "Pertamax": 12,
    "Pertalite": 11,
    "Pertamax Turbo": 15
}

# Header aplikasi
st.title("Estimasi Pengeluaran Bensin Berdasarkan Jarak Tempuh")

# Memuat CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f5;
        font-family: 'Arial', sans-serif;
    }

    h1 {
        color: #4CAF50;
        text-align: center;
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
        color: #3c763d;
        padding: 10px;
        border-radius: 5px;
    }

    .stError {
        background-color: #f2dede;
        color: #a94442;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input pengguna
jarak_tempuh = st.number_input("Masukkan jarak tempuh (km):", min_value=0.0, step=1.0)
jenis_bensin = st.selectbox("Pilih jenis bensin:", list(harga_bensin.keys()))

# Validasi input dan perhitungan
if st.button("Hitung Biaya"):
    if jarak_tempuh > 0 and jenis_bensin:
        konsumsi_per_liter = konsumsi_bensin[jenis_bensin]
        harga_per_liter = harga_bensin[jenis_bensin]
        biaya = hitung_biaya(jarak_tempuh, konsumsi_per_liter, harga_per_liter)
        st.success(f"Estimasi biaya untuk {jarak_tempuh} km dengan {jenis_bensin} adalah Rp {biaya:,.2f}")
    else:
        st.error("Harap masukkan jarak tempuh yang valid dan pilih jenis bensin.")
