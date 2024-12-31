import streamlit as st
from PIL import Image

# Judul aplikasi
st.title("Struktur Organisasi")

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
        color: pink;
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

# Fungsi untuk menampilkan anggota tim dengan foto
def display_team_member(name, photo_path, role):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(photo_path, width=100)
    with col2:
        st.write(f"**Nama:** {name}")
        st.write(f"**Peran:** {role}")

# Data anggota tim
team_members = [
    {"name": "John Doe", "photo": "ferdi.jpg", "role": "ketua"},
    {"name": "Jane Smith", "photo": "nia.jpg", "role": "anggota"},
    {"name": "Alice Johnson", "photo": "ezra.jpg", "role": "anggota"},
    {"name": "Bob Brown", "photo": "zahra.jpg", "role": "anggota"},
]

# Menampilkan setiap anggota tim
for member in team_members:
    display_team_member(member["name"], member["photo"], member["role"])
    st.write("---")

# Catatan: Pastikan file foto (john_doe.jpg, jane_smith.jpg, dll.) ada di direktori yang sama dengan script ini.