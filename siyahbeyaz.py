import cv2

def convert_to_gray():
    # Kamera bağlantısını başlat
    cap = cv2.VideoCapture(0)

    while True:
        # Kameradan bir kare al
        ret, frame = cap.read()

        # Kareyi siyah beyaz yap
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Kareyi göster
        cv2.imshow("Orjinal", frame)
        cv2.imshow("siyah beyaz", gray_frame)

        # 'q' tuşuna basıldığında döngüyü sonlandır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kamera bağlantısını kapat
    cap.release()
    cv2.destroyAllWindows()

# Fonksiyonu çağır
convert_to_gray()
