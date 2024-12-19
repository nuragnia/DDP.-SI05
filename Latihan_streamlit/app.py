import streamlit as st

dashboart = st.Page("./fitur/dashboart.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")

pg = st.navigation(
    {
        "Menu Utama" : [dashboart],
        "Transaksi" : [nabung],
    }
)

if"total_semua" not in st.session_state:
    st.session_state["total_semua"] = []

pg.run()

