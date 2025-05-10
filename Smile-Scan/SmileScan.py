import cv2
import os
from tkinter import filedialog, Tk

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
saved_webcam = False
saved_upload = False

def proses_gambar_static(img, is_upload=False):
    global saved_webcam, saved_upload
    original_frame = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    wajah_terdeteksi = len(faces)
    senyum_terdeteksi = 0

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=10, minSize=(20, 20))

        if len(smiles) > 0:
            senyum_terdeteksi += 1

            # Simpan hanya jika belum pernah disimpan
            if is_upload and not saved_upload:
                filename = os.path.join(save_folder, 'senyum_upload.jpg')
                cv2.imwrite(filename, original_frame)
                saved_upload = True
            elif not is_upload and not saved_webcam:
                filename = os.path.join(save_folder, 'senyum_webcam.jpg')
                cv2.imwrite(filename, original_frame)
                saved_webcam = True

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(img, (x + sx, y + sy), (x + sx + sw, y + sy + sh), (0, 255, 0), 2)

    cv2.putText(img, f'Wajah terdeteksi: {wajah_terdeteksi}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(img, f'Senyum terdeteksi: {senyum_terdeteksi}', (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return img

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_result = proses_gambar_static(frame.copy(), is_upload=False)
    cv2.imshow('SmileScan - Deteksi Wajah dan Senyum', frame_result)

    key = cv2.waitKey(1) & 0xFF
    if key == 32:  # Spasi untuk keluar
        break
    elif key == ord('u'):  # Tekan 'u' untuk upload gambar
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
        root.destroy()
        if file_path:
            img_upload = cv2.imread(file_path)
            if img_upload is not None:
                img_result = proses_gambar_static(img_upload.copy(), is_upload=True)
                cv2.imshow('SmileScan - Deteksi Gambar Upload', img_result)

# Bersihkan
cap.release()
cv2.destroyAllWindows()
