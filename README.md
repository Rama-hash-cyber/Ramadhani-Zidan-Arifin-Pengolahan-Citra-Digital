# 😊 SmileScan - Deteksi Senyum Otomatis dengan OpenCV

SmileScan adalah aplikasi Python berbasis OpenCV yang mampu mendeteksi wajah dan senyuman secara real-time melalui webcam atau dari gambar yang diupload. Saat senyum terdeteksi, aplikasi akan secara otomatis menyimpan satu gambar dari frame atau gambar upload tanpa kotak deteksi. Cocok untuk demonstrasi AI computer vision berbasis Haar Cascade.

---

## 🛠️ Fitur

- ✅ Deteksi wajah secara real-time menggunakan Haar Cascade
- ✅ Deteksi senyum dalam wajah dari webcam dan gambar upload
- ✅ Menyimpan satu gambar saat senyum pertama kali terdeteksi dari webcam
- ✅ Menyimpan satu gambar saat senyum terdeteksi dari gambar upload
- ✅ Tampilkan jumlah wajah dan senyum yang terdeteksi di layar (baik dari webcam maupun upload)
- ✅ Tekan tombol U untuk mengunggah gambar dari file explorer
- ✅ Tekan tombol Spasi untuk keluar dari aplikasi

---

## ⚙️ Persyaratan

- Python 3.8 atau lebih baru
- OpenCV (cv2) \ (opencv-python)
- Tkinter (biasanya sudah tersedia di Python)
- Webcam (internal atau eksternal)

---

## 📦 Instalasi

1. **Clone repositori ini :**
   ```bash
   git clone https://github.com/username/SmileScan.git
   cd SmileScan
2. **Instal dependensi yang dibutuhkan :**
   pip install opencv-python
3. **Jalankan Aplikasi**
   python smilescan.py
4. **Jalankan Menggunakan VSCode**

---

## 🗂️ Struktur Folder
smilescan_app/
├── smilescan.py                       # Skrip utama
├── hasil smile scan                   # Folder untuk hasil gambar yang terdeteksi
├── SmileScan.ipynb                    # Notebook untuk Persiapan,Konfigurasi Dataset,Eksplorasi Data
├── smile.jpg                          # Contoh senyum
├── SmileScan_Preprocessing.ipynb      # Notebook untuk Pre-Processing Gambar
└── README.txt                         # Dokumentasi proyek

---

## 📝 Cara Penggunaan

- ✅ Aplikasi akan membuka jendela webcam secara otomatis saat dijalankan.
- ✅ Wajah dan senyum akan dideteksi serta ditampilkan dengan kotak berwarna biru dan hijau.
- ✅ Jika senyum terdeteksi dari webcam, aplikasi menyimpan satu gambar tanpa kotak deteksi ke dalam folder hasil smile scan dengan nama senyum_webcam.jpg.
- ✅ Tekan tombol U untuk mengunggah gambar. Jika senyum terdeteksi dari gambar tersebut, aplikasi menyimpan satu gambar ke dalam folder hasil smile scan dengan nama senyum_upload.jpg.
- ✅ Tekan tombol Spasi untuk keluar dari aplikasi.

---

## 🤖 Teknologi yang Digunakan

- ✅ OpenCV
- ✅ Haar Cascade Classifier (pretrained XML dari OpenCV)
- ✅ Tkinter (untuk membuka file explorer saat upload gambar)

---

## 📄 Lisensi

- Proyek ini berada di bawah lisensi MIT. Silakan gunakan, ubah, dan distribusikan untuk tujuan pembelajaran maupun pengembangan.

---

## 🙌 Kontribusi

- Kontribusi sangat terbuka! Silakan fork, ajukan pull request, atau buka issue jika kamu menemukan bug atau punya ide pengembangan baru.
