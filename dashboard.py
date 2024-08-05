import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set tema Seaborn agar seragam dengan Jupyter Notebook
sns.set_theme(style='dark')

# Memuat dataset
day_df = pd.read_csv("https://raw.github.com/RafiRaihann/BikeSharing/blob/main/day.csv")
hour_df = pd.read_csv("https://raw.github.com/RafiRaihann/BikeSharing/blob/main/hour.csv")

# Filter data
hari_kerja = day_df[day_df['workingday'] == 1]
hari_libur = day_df[day_df['workingday'] == 0]

# Visualisasi Histogram
st.header('Distribusi Penggunaan Sepeda pada Hari Kerja dan Hari Libur')
fig_histogram, ax_histogram = plt.subplots()
sns.histplot(hari_kerja['cnt'], label='Hari Kerja', kde=True, ax=ax_histogram)
sns.histplot(hari_libur['cnt'], label='Hari Libur', kde=True, ax=ax_histogram)
plt.legend()
st.pyplot(fig_histogram)

# Informasi Pribadi di Sidebar
st.sidebar.subheader("Informasi Pribadi")
st.sidebar.text("Nama: Rafi Raihan")
st.sidebar.text("Email: m299d4ky2948@bangkit.academy")
st.sidebar.text("ID Dicoding: rafi_raihan_r1IS")

# Penggunaan fungsi pembantu tanpa sidebar
selected_data = hour_df  # Menggunakan data harian tanpa memilih tipe hari

# Visualisasi garis menggunakan Seaborn di Streamlit
st.subheader("Penggunaan Sepeda Harian")
# Menghitung data harian
data_harian = selected_data.groupby('hr')['cnt'].sum()
# Membuat line plot menggunakan Seaborn
fig_lineplot, ax_lineplot = plt.subplots(figsize=(12, 6))
sns.lineplot(x=data_harian.index, y=data_harian.values, marker='o', ax=ax_lineplot)
plt.title('Penggunaann Sepeda Harian')
plt.xlabel('Jam dalam Sehari')
plt.ylabel('Jumlah Peminjam Sepeda')
# Menampilkan line plot menggunakan st.pyplot()
st.pyplot(fig_lineplot)
