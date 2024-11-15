
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import base64

# Fungsi untuk mengonversi gambar menjadi base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
# Fungsi untuk mengatur gambar sebagai background
def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''  
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size:  100%; 
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: right:; 
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Path ke gambar
login_background_image_path = 'sidotopo2.png'
profile_background_image_path = 'tentangdipo.png'
vision_background_image_path = 'bgsdt.png'



# Inisialisasi session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False


# Fungsi untuk login
if not st.session_state.logged_in:
    set_background(login_background_image_path)

def login(username, password):
    
    if username == "TEKNIKMESIN22" and password == "UPNVJT22":  # Ganti dengan logika autentikasi yang sesuai
        st.session_state.logged_in = True
        st.success("Login berhasil!")
        #st.experimental_rerun()
    else:
        st.error("Username atau password salah.")

# Fungsi untuk logout
def logout():
    st.session_state.logged_in = False
    st.success("Logout berhasil!")
    #st.experimental_rerun()

# Fungsi untuk menampilkan PROFIL DIPO SIDOTOPO

def show_sales_dashboard():

    
    st.title("PROFIL DIPO SIDOTOPO")
    
    st.write('Dipo Lokomotif Sidotopo terletak di Kota Surabaya, Jawa Timur, tepatnya di kawasan Sidotopo,'
            'yang berada di sebelah utara pusat kota. Lokasinya berada dekat dengan Stasiun Sidotopo dan berdekatan dengan kawasan pelabuhan,'
            'sehingga sangat strategis untuk melayani berbagai rute kereta api yang beroperasi di wilayah Jawa Timur dan sekitarnya.')
    
    st.write('Sebagai salah satu fasilitas utama PT Kereta Api Indonesia (KAI) di Pulau Jawa, Dipo Lokomotif Sidotopo dirancang untuk melayani perawatan, perbaikan, dan pemeliharaan beragam jenis lokomotif,'
            'terutama yang beroperasi di wilayah Surabaya, jalur lintas utara, dan wilayah timur Pulau Jawa. Dengan lokasi yang strategis ini, dipo dapat menangani lokomotif-lokomotif dari berbagai rute utama,'
            'baik untuk kereta penumpang maupun kereta barang yang menuju ke dan dari Surabaya.')
    
    st.write('')

    st.write('Depo Lokomotif Sidotopo merupakan tempat perawatan sarana lokomotif yang',
            'berada di wilayah Daerah Operasional (Daop) 8 Surabaya, PT. Kereta Api Indonesia',
            '(Persero) terbatas milik Negara. Perawatan dilakukan dengan pemeliharaan bulanan,',
            'meliputi P1 untuk CC 201/203 dan GCU (General Check Up) untuk CC 206 yang',
            'dilakukan dalam jangka waktu 1 bulan, P3 dilakukan dalam jangka waktu 3 bulan, P6',
            'dilakukan dalam jangka waktu 6 bulan, dan P12 dilakukan dalam jangka waktu 12',
            'bulan. ')
    
    st.write('UPT. Depo Lokomotif Sidotopo adalah salah satu depo milik PT. Kereta Api Indonesia (Persero).'
            'Depo ini mulai dibangun pada tahun 1918 dan selesai pada tahun 1923. Depo Sidotopo masih aktif berfungsi dan telah menginjak usia 100 tahun sejak aktif digunakan pada tahun 1923.' 
            'Depo Sidotopo memiliki sejarah panjang dari masa ke masa.')
    
    st.write('Grafik dibawah menujukan kemajuan dari tahun ke tahun ')

    data = pd.DataFrame({
        'Tahun': ['1918', '1920', '1940', '1942', '1945', '1950', '1970', '1980', '2000-sampai  saat ini'],
        'Skala': ['0', '10', '19', '28', '48', '90', '109','170', '200']
    })
    
    fig = px.line(data, x='Tahun', y='Skala', title='skala Perkembangan Dipo Lokomotif')
    st.plotly_chart(fig)


def show_vission_dashboard():
    col1, col2 = st.columns([3, 1])  # Kolom pertama lebih lebar
    with col2:
            st.image("logokai2.png", width=300)
    with col1:
        st.write("")
    st.title("VISION AND MISSION")

    st.title("Vision")
    st.write('”Menjadi solusi ekosistem transportasi terbaik untuk Indonesia” ')
    st.write('Makna Visi pada PT. Kereta Api Indonesia (Persero) yaitu selalu'
            'berusaha untuk menjadi nomor satu dalam mengembangkan solusi kesatuan'
            'hubungan yang dinamis antara pengguna dan mitra kerja transportasi darat,'
            'dengan memberikan seluruh fasilitas yang nyaman, aman, serta memenuhi'
            'kebutuhan setiap penggunan di Indonesia.')

    st.title("Mission")
    st.markdown("Untuk menyediakan sistem transportasi yang aman, efisien, berbasis digital, dan berkembang pesat untuk memenuhi kebutuhan pelanggan.")  
    st.write("Untuk mengembangkan solusi transportasi massal yang terintegrasi melalui investasi dalam sumber daya manusia, infrastruktur, dan teknologi.")
    st.write("Untuk memajukan Pembangunan nasional melalui kemitraan dengan para pemangku kepentingan, termasuk memprakarsi, dan melaksanakan pengembangan infrastruktur – infrastruktur penting terkait transportasi.")





# Fungsi untuk menampilkan dashboard produk
def show_product_dashboard():
   
    st.title("PENGENALAN LOKOMOTIF DI DEPO SIDOTOPO")


    st.title('Lokomotif CC201')
    st.write('Lokomotif CC201, yang merupakan produk Electro-Motive Division (EMD) dari General Motors, adalah lokomotif diesel elektrik yang cukup tua dengan efisiensi bahan bakar yang lebih rendah dibandingkan generasi baru. Teknologi kontrol mesinnya sederhana, sehingga pembakaran bahan bakarnya tidak seefisien lokomotif modern. Sistem transmisinya juga menghasilkan panas lebih banyak, yang menyebabkan efisiensi energi berkurang.')
    st.write('Lokomotif CC201 memiliki fitur keselamatan dasar, namun karena usianya, fitur keselamatan modern seperti monitoring komputerisasi, sistem anti-slip canggih, atau kendali otomatis tidak ada atau terbatas. Lokomotif ini membutuhkan perawatan yang teliti untuk menjaga keamanan operasional, terutama dalam hal pengereman dan stabilitas di rel.')
    
    st.title('Lokomotif CC203')
    st.write('Dibandingkan dengan CC201, CC203 (produk Nippon Sharyo dan Toshiba) memiliki sedikit peningkatan efisiensi karena adanya perbaikan pada sistem penggerak dan penggunaan teknologi diesel elektrik yang lebih modern untuk masa produksinya (akhir 1970-an). Namun, CC203 masih lebih boros jika dibandingkan dengan lokomotif generasi baru, terutama karena teknologi kontrol mesinnya belum mampu mengoptimalkan pembakaran bahan bakar seperti pada lokomotif modern.')
    st.write('CC203 memiliki peningkatan dalam hal sistem pengereman dan kontrol, namun secara umum masih mengandalkan sistem manual dengan kontrol dasar. Walaupun memiliki beberapa fitur keselamatan tambahan dibandingkan CC201, seperti perlindungan mesin dari overheating, namun sistem keselamatannya tetap terbatas bila dibandingkan dengan standar keselamatan terkini.')
    
    st.title('Lokomotif CC206')
    st.write('Lokomotif CC206, yang merupakan produk General Electric (GE), adalah lokomotif dengan efisiensi bahan bakar yang jauh lebih baik dibandingkan kedua seri sebelumnya. Lokomotif ini dilengkapi dengan teknologi kontrol elektronik yang dapat mengoptimalkan konsumsi bahan bakar berdasarkan beban dan kondisi operasi. Mesin yang lebih modern juga mengurangi emisi dan meningkatkan efisiensi termal. Pengaturan multi-unit (MU) memungkinkan pengoperasian beberapa lokomotif secara simultan, sehingga dapat disesuaikan dengan kebutuhan daya dan lebih hemat energi.')
    st.write('Lokomotif CC206 dilengkapi dengan sistem keselamatan yang lebih canggih, seperti lokomotif event recorder (seperti black box pada pesawat), dynamic braking system, sistem anti-slip, dan kontrol traksi otomatis yang meningkatkan keamanan operasional di berbagai kondisi rel. Lokomotif ini juga memiliki fitur Deadman’s Switch untuk menjaga keamanan operator. Dengan sistem monitoring elektronik, CC206 dapat mendeteksi masalah mesin secara real-time, sehingga keselamatan lebih terjaga.')

    st.write('Secara keseluruhan, lokomotif CC206 memiliki tingkat efisiensi dan keselamatan yang jauh lebih tinggi daripada CC201 dan CC203, berkat teknologi mesin dan kontrol elektronik modern yang meningkatkan performa serta keandalan operasionalnya.')
    
    
    lokomotif = ['CC206', 'CC203', 'CC201']
    efisiensi = [300, 250, 150,]
    
    fig, ax = plt.subplots()
    ax.bar(lokomotif, efisiensi)
    ax.set_ylabel('TINGKAT EFISIENSI')
    ax.set_xlabel('TYPE LOKOMOTIF')
    ax.set_title('TINGKAT EFFISIENSI DAN SAFETY')
    st.pyplot(fig)

# Fungsi untuk menampilkan dashboard pelanggan
def show_customer_dashboard():
    
    st.title("LOKASI DIPO LOKOMOTIF SIDOTOPO")
    
    st.write('Dipo Lokomotif Sidotopo terletak di Kota Surabaya, Jawa Timur, tepatnya di kawasan Sidotopo,'
             'yang berada di sebelah utara pusat kota. Lokasinya berada dekat dengan Stasiun Sidotopo dan berdekatan dengan kawasan pelabuhan,'
            'sehingga sangat strategis untuk melayani berbagai rute kereta api yang beroperasi di wilayah Jawa Timur dan sekitarnya.')
    
    st.write('Sebagai salah satu fasilitas utama PT Kereta Api Indonesia (KAI) di Pulau Jawa, Dipo Lokomotif Sidotopo dirancang untuk melayani perawatan, perbaikan, dan pemeliharaan beragam jenis lokomotif,'
             'terutama yang beroperasi di wilayah Surabaya, jalur lintas utara, dan wilayah timur Pulau Jawa. Dengan lokasi yang strategis ini, dipo dapat menangani lokomotif-lokomotif dari berbagai rute utama,'
              'baik untuk kereta penumpang maupun kereta barang yang menuju ke dan dari Surabaya.')

    st.write('Lokasi Dipo Lokomotif Sidotopo teptanya ada di Jl. Sidotopo Lor No.2, Simokerto, Kec. Simokerto, Surabaya, Jawa Timur 60143') 
    # Data lokasi
    df = pd.DataFrame(
    np.random.randn(1, 1) / [100000, 100000] + [-7.236646, 112.755870],
    columns=["lat", "lon"],
    )
    st.map(df)  
    col1, col2, col3 = st.columns([1, 2, 1])  
    with col1:
        st.write("") 
    with col2:
        st.write("https://maps.app.goo.gl/AtC59khzHP6SXA6E9!") 
    with col3:
        st.write("")  


    st.write('LOKASI KAMPUS KE DIPO SIDOTOPO')
    from PIL import Image
    # Menampilkan gambar dari file lokal
    image = Image.open('lokasi sdt.jpg')
    st.image(image, caption='Lokasi univ ke lokasi magang')
   

# Fungsi untuk menampilkan dashboard keuangan
def show_finance_dashboard():

    st.title("JADWAL PERAWATAN DAN PERBAIKAN LOKOMOTIF")
    
    # Membuat DataFrame menggunakan pandas menampilkan tabel pertama  
    data1    = {
        'TANGGAL': ['05 AGUSTUS 2024','06 AGUSTUS 2024','07 AGUSTUS 2024','08 AGUSTUS 2024','09 AGUSTUS 2024','10 AGUSTUS 2024','11 AGUSTUS 2024','12 AGUSTUS 2024','13 AGUSTUS 2024','14 AGUSTUS 2024','15 AGUSTUS 2024','16 AGUSTUS 2024','17 AGUSTUS 2024','18 AGUSTUS 2024','19 AGUSTUS 2024','20 AGUSTUS 2024','21 AGUSTUS 2024','22 AGUSTUS 2024','23 AGUSTUS 2024','24 AGUSTUS 2024','25 AGUSTUS 2024','26 AGUSTUS 2024','27 AGUSTUS 2024','28 AGUSTUS 2024','29 AGUSTUS 2024','30 AGUSTUS 2024','31 AGUSTUS 2024'],
        'LOKOMOTIF CC': [2061388, 2061345, 2030203, 2061314, 2061504, 2061326,  2030201, 2061318, 2039814, 2017706, 2061315 , 2019838, 2061335, 2039832,2017766, 2061341, 2039822, 2061326, 2017794, 2017752, 2039874, 2061392, 2039899, 2061342, 2017716,2061331, 2061382],
        'PERBAIKAN DAN PERAWATAN' : ['COPS Crankcase','Perawatan triwulanan','Perawatan enam bulan','Perawatan enam bulan','GCU & Cek axle TM 1','Pergantian TM ','Perbaikan pada Gearbox','GCU/GFF & Perbaikan flexible air','Perawatan satu bulan','Perawatan duabelas bulan','Perawatan duabelas bulan','Perbaikan tenaga lemah','Perbaikan baut mounting engine patah','Pemeriksaan AGCB','Pemeriksaan high resistence lemah','General check up/GCU','Perawwatan enam bulan','Perawatan satu bulan','Perawatan triwulanan','Pergantian AUXGEN','Perawatan enam bulan','Pergantian TM','Perbaikan pada gearbox turbin','Perbaikan pada injector','Perawatan celah klep pada MD','Perawwatan triwulanan','Perawatan satu bulan']
    }
    df1 = pd.DataFrame(data1)
    st.write("AGUSTUS")
    #untuk mengubah angka awal
    df1.index = df1.index + 1 
    #untuk mengubah koma pada angka
    df1 = df1.style.format({"LOKOMOTIF": lambda x: '{}'.format(x).replace(',', '')})
    st.dataframe(df1, height=983, width=17000)

# Menampilkan tabel kedua
    data2 = {
        'TANGGAL': ['01 SEPTEMBER 2024', '02 SEPTEMBER 2024', '03 SEPTEMBER 2024', '04 SEPTEMBER 2024', '05 SEPTEMBER 2024','06 SEPTEMBER 2024','07 SEPTEMBER 2024','08 SEPTEMBER 2024','09 SEPTEMBER 2024','10 SEPTEMBER 2024','11 SEPTEMBER 2024','12 SEPTEMBER 2024','13 SEPTEMBER 2024','14 SEPTEMBER 2024','15 SEPTEMBER 2024','16 SEPTEMBER 2024','17 SEPTEMBER 2024','18 SEPTEMBER 2024','19 SEPTEMBER 2024','20 SEPTEMBER 2024','21 SEPTEMBER 2024','22 SEPTEMBER 2024','23 SEPTEMBER 2024','24 SEPTEMBER 2024','25 SEPTEMBER 2024','26 SEPTEMBER 2024','27 SEPTEMBER 2024','28 SEPTEMBER 2024','29 SEPTEMBER 2024','30 SEPTEMBER 2024'],
        'LOKOMOTIF CC': [2061388, 2030201, 2017702, 2061316, 2061354, 2061326, 2061334, 2061338, 2061335, 2061332, 2061334, 2061338, 2061335, 2061332,2061366, 2061341, 2061322, 2061326, 2061394, 2061352, 2061374, 2061392, 2061399, 2061342, 2061346,2061331, 2061382,2061346,2061331, 2061382],
        'PERBAIKAN DAN PERAWATAN' : ['Perbaikan seal crankcase','perbaikan membran independent brake','Perawatan triwulanan','Perawatan enam bulan','Pengelasan skin plat','Perbaikan axle TM','Perbaikan tenaga lemah','Perawatan duabelas bulan','Perawatan satu bulan','Perbaikan axlepot bocor','Perbaikan holder cable gronding patah','Perbaikan anloader compresor','Perawatan satu bulan','Perawatan triwulanan','Perawatan satu bulan','Perawatan enam bulan','Perawatan triwulanan','Perbaikan kebocoran cylinder brake','Perbaikan saluran pemasir','Perawatan duabelas bulan','Pearawatan satu bulan','Perawatan duabelas bulan','Perawawtan triwulanan','Perbaikan main generator','Perbaikan injector','Perbaikan intercoler compresor','Perawatan duabelas bulan','Perawata triwulanan','Perbaikan komutator pada TM','Perawatan satu bulan']
    }

    df2 = pd.DataFrame(data2)
    st.write("SEPTEMBER")  
    df2.index = df2.index + 1 
    df2 = df2.style.format({"LOKOMOTIF": lambda x: '{}'.format(x).replace(',', '')})
    st.dataframe(df2, height=1087, width=17000)

    #Untuk menampilkan tabel ketiga
    data3 = {
        'TANGGAL': ['01 OKTOBER 2024', '02 OKTOBER 2024', '03 OKTOBER 2024', '04 OKTOBER 2024', '05 OKTOBER 2024','06 OKTOBER 2024','07 OKTOBER 2024','08 OKTOBER 2024','09 OKTOBER 2024','10 OKTOBER 2024','11 OKTOBER 2024','12 OKTOBER 2024','13 OKTOBER 2024','14 OKTOBER 2024','15 OKTOBER 2024','16 OKTOBER 2024','17 OKTOBER 2024','18 OKTOBER 2024','19 OKTOBER 2024','20 OKTOBER 2024','21 OKTOBER 2024','22 OKTOBER 2024','23 OKTOBER 2024','24 OKTOBER 2024','25 OKTOBER 2024','26 OKTOBER 2024','27 OKTOBER 2024','28 OKTOBER 2024','29 OKTOBER 2024','30 OKTOBER 2024'],
        'LOKOMOTIF CC': [2017788, 2039841, 2017705, 2061316, 2039819, 2017726, 2039884, 2017738, 2017735, 2017732, 2061334, 2061338, 2039835, 2017712,2039866, 2017741, 2061322, 2061326, 2061394, 2017752, 2017774, 2017792, 2039899, 2039842, 2061346,2061331, 2017782,2061346,2061331, 2039882],
        'PERBAIKAN DAN PERAWATAN' : ['Pergantian TM 2',' Penyetelan Celah klep pada MD','Perbaikan pada exhaust MD','Perawatan satu bulan','Perawatan dua belas bulan','Perbaikan turbin turbo pada MD','Perawatan duabelas bulan','Perawatan satu bulan','Perbaikan axle TM','Pergantian accu','Perawatan triwulanan','Perawatan satu bulan','Perawatan satu bulan','Pergantian anloader compresor','Perbaikan exiter','Perbaikan intercoller pada MD','Perawatan satu bulan','Perawatan satu bulan','Pearawatan satu bulan','Perbaikan power contactor lemah','Perbaikan gearbox TM','Perbaikan axlepot pada TM','Perawatan duabelas bulan','Perawatan enam bulan','Perawatan triwulanan','Perawatan satu bulan','Perawatan satu bulan','Perawaatan satuu bulan','Pergantian TM 3','Perawatan triwulanan']
    }
    df3 = pd.DataFrame(data3)
    st.write("OKTOBER")  
    df3.index = df3.index + 1 
    df3 = df3.style.format({"LOKOMOTIF": lambda x: '{}'.format(x).replace(',', '')})
    st.dataframe(df3, height=1087, width=17000)

    #Untuk menampilkan tabel keempat
    data4 = {
        'TANGGAL': ['01 NOVEMBER 2024', '02 NOVEMBER 2024', '03 NOVEMBER 2024', '04 NOVEMBER 2024', '05 NOVEMBER 2024','06 NOVEMBER 2024','07 NOVEMBER 2024','08 NOVEMBER 2024','09 NOVEMBER 2024','10 NOVEMBER 2024','11 NOVEMBER 2024','12 NOVEMBER 2024','13 NOVEMBER 2024','14 NOVEMBER 2024','15 NOVEMBER 2024','16 NOVEMBER 2024','17 NOVEMBER 2024','18 NOVEMBER 2024','19 NOVEMBER 2024','20 NOVEMBER 2024','21 NOVEMBER 2024','22 NOVEMBER 2024','23 NOVEMBER 2024','24 NOVEMBER 2024','25 NOVEMBER 2024'],
        'LOKOMOTIF CC': [2061318, 2030203, 2017712, 2017717, 2061354, 2039826, 2039834, 2017738, 2061335, 2017722, 2061334, 2061338, 2039835, 2039832,2017709, 2061341, 2061322, 2039814, 2061394, 2061352, 2039814, 2017792, 2039899, 2061342, 2061346],
        'PERBAIKAN DAN PERAWATAN' : ['Perawatan satu bulan','Perawatan satu bulan','Pergantian seal head pada MD','Perawatan satu bulan','Perawatan triwulanan','Perbaikan injector pada MD','Pergantian anloader compreesor','Perawatan duabelas bulan','Perbaikan kabel grounding TM','Perbaikan axlepot TM','Perbaikan skin plat','Perawatan satu bulan','Perawatan enam bulan','Perawatan satu bulan','Perawatan satu bulan ','Perbaikan baut mounting MD patah','Pergantian AUXGEN','Pergantian power contactor','Pperbaikan intercoler pada compresor','Perawatan satu bulan','Perbaikan pada sensor LOP,LWP,COP,MAP,EFT','Peawatan enam bulan','Perawatan satu bulan','Perbaikan oilcooler pada MD','Perbaikan pada exiter']
    }

    df4 = pd.DataFrame(data4)
    st.write("NOVEMBER")  
    df4.index = df4.index + 1 
    df4 = df4.style.format({"LOKOMOTIF": lambda x: '{}'.format(x).replace(',', '')})
    st.dataframe(df4, height=912, width=17000)



def main():
    #Untuk memberi  logo pada ojok kanan atas menggunakan coloum
    col1, col2 = st.columns([3, 1])  
    with col2:
            st.image("logokai2.png", width=300)
    with col1:
        st.write("")

    if not st.session_state.logged_in:
        st.title("SELAMAT DATANG")
        st.write("Silahkan masukan userame dan password")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            login(username, password)
    
    else:
        # Sidebar untuk navigasi
        st.sidebar.title("MENU")
        menu = st.sidebar.radio("", ["ABOUT US", "VISION & MISSION", "LOKOMOTIF", "LOKASI", "DATA", "Logout"])
        
        if menu == "ABOUT US":
            set_background('tentangdipo.png')
            show_sales_dashboard()
        elif menu == "VISION & MISSION":
            show_vission_dashboard()
            set_background('bgsdt.png')
        elif menu == "LOKOMOTIF":
            show_product_dashboard()
            set_background('bglok.png')
        elif menu == "LOKASI":
            show_customer_dashboard()
            set_background('bgkarnaval.png')
        elif menu == "DATA":
            show_finance_dashboard()
            set_background('bgkarnaval2.png')
        elif menu == "Logout":
            logout()

if __name__ == "__main__":
    main()
