import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
    h1 {
        color: #4CAF50; /* Green color */
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 20px;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin-top: 20px;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 12px;
        text-align: center;
    }
    th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
    .header {
        text-align: center;
        margin-bottom: 30px;
    }
    .price {
        font-size: 1.5em;
        color: #FF5733; /* A vibrant color for prices */
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# input data harga bensin
#st.markdown('<div class="data"')
data_harga = {
    'pulau' : ['jawa barat', 'sumatra utara', 'kalimantan selatan', 'sulawesi selatan', 'papua'], 
    'harga pertalite' : [10000, 10000, 10000, 10000, 10000],
    'harga pertamax' : [12100, 12400, 12650, 12400, 12400],
    'harga pertamax turbo' : [13500, 13850, 14150, 13850, 13850]
}
df = pd.DataFrame(data_harga)

st.markdown("<h1>PERBANDINGAN HARGA BENSIN DI BERBAGAI PULAU</h1>", unsafe_allow_html=True)

# tampilkan data
st.write(" Data Harga Bensin:")
st.dataframe(df)

#pilih pulau untuk melihat harga
pulau = st.selectbox("Pilih pulau:", df['pulau'])
harga = df[df['pulau'] == pulau].iloc[0]

# menampilkan harga bensin
st.write(f"Harga bensin di {pulau}:")
st.write(f"Pertalite: Rp {harga['harga pertalite']}")
st.write(f"Pertamax: Rp {harga['harga pertamax']}")
st.write(f"Pertamax Turbo: Rp {harga['harga pertamax turbo']}")
