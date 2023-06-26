import cv2

def rotate_image():
    # Kamera bağlantısını başlat
    cap = cv2.VideoCapture(0)

    while True:
        # Kameradan bir kare al
        ret, frame = cap.read()

        # Kareyi 180 derece döndür
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_180)

        # Kareyi göster
        cv2.imshow("Orjinal", frame)
        cv2.imshow("ters dönmüş ", rotated_frame)

        # 'q' tuşuna basıldığında döngüyü sonlandır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamera bağlantısını kapat
    cap.release()
    cv2.destroyAllWindows()

# Fonksiyonu çağır
rotate_image()
