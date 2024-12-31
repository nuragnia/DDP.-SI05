import streamlit as st


menu = st.Page("menu.py", title="Menu")
perhitungan = st.Page("perhitungan_harga.py")
estimasi_harga = st.Page("estimasi_bensin.py", title="Estimasi Bensin")
perbandingan = st.Page("perbandingan.py", title="Perbandingan")
biaya_perjalanan = st.Page("biaya_perjalanan.py", title="Biaya Perjalanan")
about = st.Page("about.py", title="Tentang Kami")


pg = st.navigation(
    {
        "Beranda" : [menu],
        " " : [perhitungan],
        "  " : [estimasi_harga],
        "   "  : [perbandingan],
        "    " : [biaya_perjalanan],
        "     " : [about],
    }
)

#if"total_semua" not in st.session_state:
    #st.session_state["total_semua"] = []

pg.run()

