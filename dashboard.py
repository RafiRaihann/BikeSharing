import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Set tema Seaborn agar seragam dengan Jupyter Notebook
sns.set_theme(style='dark')

# Fungsi pembantu
def filter_by_workingday(data, workingday_value):
    return data[data['workingday'] == workingday_value]

def generate_descriptive_stats(data, column_name):
    return data[column_name].describe()

def create_statistics_table(deskripsi_hari_kerja, deskripsi_hari_libur):
    tabel_statistik = pd.DataFrame({
        'Hari Kerja': deskripsi_hari_kerja,
        'Hari Libur': deskripsi_hari_libur
    })
    return tabel_statistik

# Memuat dataset
all_df = pd.read_csv("all_data.csv")

# Sidebar untuk pemilihan hari kerja atau hari libur
option = st.sidebar.radio("Pilih Tipe Hari:", ['Hari Kerja', 'Hari Libur'])

# Penggunaan fungsi pembantu
if option == 'Hari Kerja':
    selected_data = filter_by_workingday(all_df, 1)
    st.sidebar.subheader("Statistik Hari Kerja:")
elif option == 'Hari Libur':
    selected_data = filter_by_workingday(all_df, 0)
    st.sidebar.subheader("Statistik Hari Libur:")

# Statistik deskriptif untuk hari yang dipilih
deskripsi_hari = generate_descriptive_stats(selected_data, 'cnt')

# Tampilkan statistik di sidebar
st.sidebar.write("Jumlah Data:", len(selected_data))
st.sidebar.write("Rata-rata:", format_currency(deskripsi_hari['mean'], 'USD', locale='en_US'))
st.sidebar.write("Standar Deviasi:", format_currency(deskripsi_hari['std'], 'USD', locale='en_US'))

# Visualisasi menggunakan Seaborn di Streamlit
st.subheader(f"Distribusi Penggunaan Sepeda pada {option}")
fig, ax = plt.subplots()
sns.histplot(selected_data['cnt'], label=option, kde=True, ax=ax)
plt.legend()
# Menampilkan plot menggunakan st.pyplot()
st.pyplot(fig)

# Visualisasi garis menggunakan Seaborn di Streamlit
st.subheader("Penggunaan Sepeda Harian")
# Menghitung data harian
data_harian = all_df.groupby('hr')['cnt'].sum()
# Membuat line plot menggunakan Seaborn
fig_lineplot, ax_lineplot = plt.subplots(figsize=(12, 6))
sns.lineplot(x=data_harian.index, y=data_harian.values, marker='o', ax=ax_lineplot)
plt.title('Penggunaan Sepeda Harian')
plt.xlabel('Jam dalam Sehari')
plt.ylabel('Jumlah Peminjam Sepeda')
# Menampilkan line plot menggunakan st.pyplot()
st.pyplot(fig_lineplot)
