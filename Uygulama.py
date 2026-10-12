import cv2 as cv

cap = cv.VideoCapture(0)

print("Kayıt başladı. Çıkmak için 'q' tuşuna basın.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Kayıt başlamadı.")
        break
    
    # Görüntü boyutlarını alma
    h, w, _ = frame.shape  # Görüntünün yükseklik(h), genişlik(w) ve kanal sayısını(_) ifade eder.

    # 3x3 grid için bölme noktalarını hesaplama 
    x1, x2 = w//3, 2*(w//3)     # Pikseller yarım olmayacağı için tam sayı kullanılmalı. 
    y1, y2 = h//3, 2*(h//3)     # "//" bu ifade kalansız bölmek için kullanılır.

    # Dikey çizgileri çizme
    cv.line(frame,(x1,0),(x1,h),(0,255,0),2)
    cv.line(frame,(x2,0),(x2,h),(0,255,0),2)
    
    # Yatay çizgileri çizme
    cv.line(frame,(0,y1),(w,y1),(0,255,0),2)
    cv.line(frame,(0,y2),(w,y2),(0,255,0),2)

    # Ekranda göster
    cv.imshow("3x3 gridli ekran", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
