import cv2 as cv
import numpy as np

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
    
    # BGR to HSV
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    cv.imshow('HSV',hsv)
    
    # Renk aralığı
    lower_red = np.array([0,100,100])
    upper_red = np.array([10,255,255])
    
    mask = cv.inRange(hsv,lower_red,upper_red)
    
    kernel = np.ones((5,5),np.uint8)
    mask =cv.erode(mask,kernel,iterations=2)
    mask=cv.dilate(mask,kernel,iterations=2)
    cv.imshow('Mask',mask) # Sistemin çalışma mantığı daha net anlaşılması için yeni bir pencere ekledim. Nesne belirtilen renk aralığındaysa bu ekran üzerinde beyaz şekilde görünecek.
    
    # Kontür bulma ve nesnenin merkezinin hesaplanması
    contours,_ = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    
    kare_bulundu = False
    
    if contours:
      # En büyük alan bulunur. (nesnenin düzgün tanınması için en büyük alan seçilir.)
      largest_contour = max(contours, key=cv.contourArea)
      area = cv.contourArea(largest_contour)

      # Alan yeterince büyükse kare işleme alınır. 
      if area > 450:
        kare_bulundu = True

        # Karenin etrafına kontür çizilir.
        cv.drawContours(frame, [largest_contour], -1, (0, 255, 0), 3)

        # Momentler yardımıyla nesnemizin merkez koordinatı bulunur.
        M = cv.moments(largest_contour)
        if M["m00"] != 0:
          cx = int(M["m10"] / M["m00"])
          cy = int(M["m01"] / M["m00"])

          # Nesnenin merkez noktası ekranda işaretlenir.
          cv.circle(frame, (cx, cy), 7, (0, 0, 255), -1)
          
          # Nesne merkezinin hangi hücrede olduğu belirlenir.
          # (Sütun olarak kaçıncı sütunda olduğu bulunur.)
          if cx < x1:
              col=1
          elif cx < x2:
              col=2
          else:
              col=3
        
          # (Satır olarak kaçıncı satırda olduğu bulunur.)
          if cy < y1:
              row=1
          elif cy < y2:
              row=2
          else:
              row=3
          
          cell_num=(row - 1)*3 + col  #3x3 gridli ekranda her hücrenin 1den 9a kadar numaralandırılması
          
          # Nesnenin hücre numarası, satır ve sütun numarası ekrana yazdırılır.
          info_text = f"Hucre: {cell_num} (Satır {row}, Sutun {col})"
          cv.putText(frame, info_text, (20,40), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
          
    # Kare görüntüde yoksa "Kare aranıyor" yazısı yazılır. 
    if not kare_bulundu:
        cv.putText(frame, "Kare aranıyor", (20,40), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2)
        
    
    # Ekranda göster
    cv.imshow("3x3 gridli ekran", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
