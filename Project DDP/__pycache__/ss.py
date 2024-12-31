import streamlit as st

st.markdown("""
<style>
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
            color: #000000;
            text-align: center;
            margin-bottom: 20px;
    }
    .profile-card {
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #00FFFF;
        transition: transform 0.3s ease;
    }
    .profile-card:hover {
        transform: translateY(-10px);
    }
    .profile-card img {
        border-radius: 50%;
        margin-bottom: 10px;
    }
    .profile-card h3 {
        margin: 0;
        font-size: 18px;
        color: #00FFFF;
    }
            page_bg_img = '''
            <style>
            body {
            background-image: src("foto/logo.jpg");
            background-size: cover;
            }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class= "title">Profiel Kelompok</div>', unsafe_allow_html=True)

col1, col2,col3 = st.columns(3)  # Membuat tiga kolom
col2.image("foto/ferdi.jpg", width=200, caption="Eka Ferdi Febriansyah")
col1, col2,col3 = st.columns(3)  # Membuat tiga kolom
col1.image("foto/nia.jpg", width=150, caption="Nur Aghnia")
col2.image("foto/ezra.jpg", width=180, caption="Erza Rizfia")
col3.image("foto/zahra.jpg", width=210, caption="Zahra Zuliyani Utami")