import streamlit as st

# Menambahkan CSS untuk styling
st.markdown("""
<style>
    .profile-card {
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #fff; /* Warna latar belakang kartu */
    }

    .profile-image {
        border-radius: 50%;
        width: 150px; /* Atur ukuran gambar */
        border: 4px solid #3498db; /* Tambahkan border biru */
    }
</style>
""", unsafe_allow_html=True)

# Menampilkan gambar dengan styling
st.markdown('<div class="profile-card">', unsafe_allow_html=True)
st.image("foto/nia.jpg", class_="profile-image")  # Menampilkan gambar
st.markdown('<p>Nia</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)