import streamlit as st

st.title("Halaman Nabung")

#Formulir Input
with st.form("Menabung"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("Waktu")
    submit_botton = st.form_submit_button(label="Menabung")


    if submit_botton and jumlah >= 50000:
        st.session_state["total_semua"].append({
            "Tipe" : "Menabung",
            "Jumlah" : jumlah
        })
        st.success("Menabung Berhasil")
    else:
        st.error("Menabung Gagal")