# 😊 SmileScan - Deteksi Senyum Otomatis dengan OpenCV

SmileScan adalah aplikasi berbasis Python yang menggunakan OpenCV untuk mendeteksi wajah dan senyuman secara real-time melalui webcam. Ketika senyuman terdeteksi, aplikasi akan otomatis menyimpan satu gambar dari frame tanpa kotak deteksi. Cocok untuk demo AI computer vision berbasis Haar Cascade.

---

## 🛠️ Fitur

- ✅ Deteksi wajah secara real-time menggunakan Haar Cascade
- ✅ Deteksi senyum di dalam wajah yang terdeteksi
- ✅ Menyimpan satu gambar saat senyum pertama kali terdeteksi
- ✅ Menampilkan jumlah wajah dan senyum yang terdeteksi pada layar

---

## ⚙️ Persyaratan

- Python 3.6 atau lebih baru
- OpenCV (cv2)
- Webcam internal atau eksternal

---

## 📦 Instalasi

1. **Clone repositori ini :**
   ```bash
   git clone https://github.com/username/SmileScan.git
   cd SmileScan
2. **Instal dependensi yang dibutuhkan :**
   pip install opencv-python
3. **Jalankan Aplikasi**
   python smile_scan.py

---

## 🗂️ Struktur Folder
SmileScan/
├── smile_scan.py              # Skrip utama
├── hasil smile scan          # Folder untuk hasil gambar yang disimpan
└── README.md                  # Dokumentasi proyek

---

## 📝 Cara Penggunaan
- ✅ Aplikasi akan membuka jendela webcam.
- ✅ Wajah dan senyum akan terdeteksi dan ditampilkan dengan kotak berwarna.
- ✅ Gambar akan disimpan otomatis di folder hasil smile scan saat senyum pertama kali terdeteksi.
- ✅ Tekan spasi (spacebar) untuk keluar dari aplikasi.

---

## 🤖 Teknologi yang Digunakan
- ✅ OpenCV
- ✅ Haar Cascade Classifier (pretrained XML dari OpenCV)

---

## 📄 Lisensi
- MIT License. Silakan digunakan dan dimodifikasi untuk keperluan pribadi maupun edukasi.

---

## 🙌 Kontribusi
-Kontribusi sangat terbuka! Silakan fork, ajukan pull request, atau buka issue jika kamu menemukan bug atau punya     ide pengembangan.
