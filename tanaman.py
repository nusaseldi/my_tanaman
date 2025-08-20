import pandas as pd
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Tentukan scope untuk Sheets dan Drive
scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Autentikasi dengan file JSON
creds = Credentials.from_service_account_info(st.secrets["google_api"], scopes=scope)
client = gspread.authorize(creds)

# Buka spreadsheet berdasarkan URL atau nama
sheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1PQCkKhfaL7K8lc2HUPZdG2S_hBoEYaR0aUNTiJm2PXQ/edit?usp=sharing').sheet1

# Fetch semua data dari worksheet 
data = sheet.get_all_records()

# Convert data ke pandas DataFrame
df = pd.DataFrame(data)

# Title untuk page
st.set_page_config(page_title='My Tanaman', page_icon="🌱" ,layout='wide', initial_sidebar_state='auto')
st.title("Daftar Tanaman")

# Tambah sidebar
add_sidebar = st.sidebar.date_input("Hari ini", value="today", format="DD/MM/YYYY", disabled=True)
st.sidebar.write("Note: This is personal record of the plants in my house and how to care for them")

# Checkbox penyiraman
st.sidebar.write("Apakah hari ini tanaman sudah disiram?")
penyiraman = st.sidebar.checkbox("Yes!")

# Tabel yang menampilkan data
st.dataframe(df, hide_index=True, row_height=100, height=800, column_config= {"Gambar":st.column_config.ImageColumn()})


