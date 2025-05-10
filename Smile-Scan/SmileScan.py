import cv2
import os

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Buka webcam
cap = cv2.VideoCapture(0)

# Folder penyimpanan
save_folder = "hasil smile scan"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Variabel kontrol
saved = False  # Pastikan hanya satu gambar yang disimpan

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Salin frame asli untuk disimpan tanpa kotak
    original_frame = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    wajah_terdeteksi = len(faces)
    senyum_terdeteksi = 0

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Deteksi senyum di setiap wajah
        smiles = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.3,
            minNeighbors=10,
            minSize=(20, 20)
        )

        if len(smiles) > 0:
            senyum_terdeteksi += 1

            # Simpan frame asli TANPA kotak hanya sekali saat senyum terdeteksi
            if not saved:
                filename = os.path.join(save_folder, 'senyum_terdeteksi.jpg')
                cv2.imwrite(filename, original_frame)  # Simpan frame asli tanpa kotak
                saved = True

        # Gambar kotak wajah dan senyum hanya untuk tampilan
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(frame, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (0, 255, 0), 2)

    # Tampilkan teks jumlah deteksi
    cv2.putText(frame, f'Wajah terdeteksi: {wajah_terdeteksi}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Senyum terdeteksi: {senyum_terdeteksi}', (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Tampilkan frame ke layar
    cv2.imshow('SmileScan - Deteksi Wajah dan Senyum', frame)

    # Tekan spasi untuk keluar
    if cv2.waitKey(1) & 0xFF == 32:
        break

# Bersihkan
cap.release()
cv2.destroyAllWindows()
