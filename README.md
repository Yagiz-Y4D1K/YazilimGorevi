# YazilimGorevi

UYGULAMANIN AMACI
Bu uygulamayı, webcam'den alınan görüntüdeki kareyi 3x3'lük gridin hangi hücresinde olduğunu tespit edecek şekilde tasarlamayı amaçladım.

PROGRAMIN TASARIMI
İlk olarak, ekranı 3x3 gride bölerek hücre, satır ve sütunları ekranda oluşturmuş oldum. Sonrasında bir renk aralığı belirledim. Bu renk aralığına göre HSV maskeleme yaparak, nesnenin eğer uygun renk aralığındaysa beyaz pikseller ile işaretlenmesini ayarladım. Uygun renk aralığında olmayan nesneleri ise siyah pikseller ile işaretlenecek şekilde ayarladım. Kare böylece belirgin hale geldikten sonra kontur bulma işlemi yaparak karenin etrafının yeşil bir şeritle çevrili halde ekranda gösterilmesini sağladım. Geometrideki kütle merkezi formülünden yararlanarak, momentler ile görüntüdeki karenin merkezini tespit ettim. Daha sonrasında, kare merkezinin koordinatlarına göre hangi hücrede olduğunu ekranda gösterecek şekilde ayarladım. 

TASARIM SÜRECİNDE KARŞILAŞILAN ZORLUKLAR
Tasarım esnasında, programın kareyi doğru bir şekilde bulması konusunda ne yapacağıma karar vermekte zorluk yaşadım. Son olarak, yapılan uygulamaları, ekranda yer alan uygun aralıktaki karelerden en yüksek pikselli (en fazla alanı) olana uygulanacak şekilde ayarladım. Bu şekilde tek bir nesneyi tespit etmekte sorun kalmadı. Bir de bazı hücrelerdeyken nesne etrafındaki yeşil konturde titreme ve bozulmalar oluyordu. Bunları giderebilmeye çalıştım ancak bazı nesneler için hala yetersiz bir görüntü oluşabiliyor.   
