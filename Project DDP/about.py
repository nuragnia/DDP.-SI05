import streamlit as st

# Menambahkan CSS untuk styling
st.markdown("""
<style>
    body {
        background-color: #f0f0f0; /* Warna latar belakang halaman */
    }

    .profile-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-wrap: wrap;
        gap: 20px;
        margin-top: 20px;
    }

    .title {
        font-size: 40px;
        color: #333; /* Warna judul */
        text-align: center;
        margin-bottom: 20px;
        font-family: 'Pacifico', cursive; /* Menggunakan font Pacifico */
    }

    .profile-card {
        text-align: center;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #fff; /* Warna latar belakang kartu */
        transition: transform 0.3s ease;
    }

    .profile-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }

    .profile-image {
        border-radius: 50%;
        margin-bottom: 15px;
        width: 150px; /* Atur ukuran gambar */
        border: 4px solid #3498db; /* Tambahkan border biru */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3); /* Tambahkan bayangan */
    }
</style>
""", unsafe_allow_html=True)

# Judul dengan gaya
st.markdown('<div class="title">Profil Kelompok</div>', unsafe_allow_html=True)

# Menggunakan container untuk mengatur tata letak
with st.container():
    col1, col2, col3 = st.columns(3)

    with col2:
        st.markdown(
            '<div class="profile-card">'
            '<p>Eka Ferdi Febriansyah <br> 01101240187</p>'
            '</div>',
            unsafe_allow_html=True
        )
        st.image("foto/ferdi.jpg", width=220)

with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            '<div class="profile-card">'
            '<p>Nur Agnia <br> 0110124146 <br> nur_agnia26</p>'
            '</div>',
            unsafe_allow_html=True
        )
        st.image("foto/nia.jpg", width=220)

    with col2:
        st.markdown(
            '<div class="profile-card">'
            '<p>Erza Rizfia  <br> 0110124146 <br> azreee_15</p>'
            '</div>',
            unsafe_allow_html=True
        )
        st.image("foto/ezra.jpg", width=220)

    with col3:
        st.markdown(
            '<div class="profile-card">'
            '<p>Zahra Zuliyani Utami <br>0110124042 <br> zhraazlyn_</p>'
            '</div>',
            unsafe_allow_html=True
        )
        st.image("foto/zahra.jpg", width=220)
