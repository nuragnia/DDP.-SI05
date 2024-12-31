import streamlit as st

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-size: 30px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 20px;
    }
    .section {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .section-title {
        font-size: 24px;
        font-weight: bold;
        color: #34495e;
        margin-bottom: 10px;
    }
    .section-content {
        font-size: 16px;
        color: #2c3e50;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# Judul Aplikasi
st.markdown('<div class="title">Selamat Datang Di Aplikasi Milage Money</div>', unsafe_allow_html=True)

# Tujuan Aplikasi
st.markdown('<div class="section"><div class="section-title">Tujuan Aplikasi</div><div class="section-content">1. Perhitungan harga bensin berdasarkan volume dan harga perliter. (total biaya yang harus dibayar) <br>2. Estimasi pengeluaran bensin berdasarkan jarak tempuh <br> 3. Kalkulator estimasi biaya perjalanan <br> 4. Perbandingn harga bensin di berbagai pulau</div></div>', unsafe_allow_html=True)

# Latar Belakang Aplikasi
st.markdown('<div class="section"><div class="section-title">Latar Belakang Aplikasi</div><div class="section-content">Latar belakang dinamakannya aplikasi mileage money adalah nama ini lebih fokus pada aspek penghematan, menyiratkan bahwa aplikasi mileage money ini dapat membatu pengguna mengelola pengeluaran untuk jarak tempuh tertentu.</div></div>', unsafe_allow_html=True)