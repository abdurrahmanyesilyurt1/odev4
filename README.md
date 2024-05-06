Fonksiyonun aldığı iki metin, text1 ve text2, kelimelere ayrılmadan önce küçük harfe dönüştürülür.
Daha sonra, .split() metodu kullanılarak kelimelere bölünür ve her kelimenin sıklığı collections.Counter ile hesaplanır.
freq1 ve freq2, bu kelime sıklıklarını tutan sözlüklerdir.
all_words değişkeni, freq1 ve freq2 sözlüklerinde bulunan tüm benzersiz kelimelerin bir birleşimini tutar.
set ile sıklık sözlüklerinin anahtarları kümeye dönüştürülerek, .union ile birleştirilir.
distance değişkeni, her bir kelimenin freq1 ve freq2 içindeki sıklık farklarının karesinin toplamıdır.
for word in all_words ile tüm benzersiz kelimelerde dolaşılır, freq1[word] - freq2[word] ile kelimenin iki metindeki sıklık farkı hesaplanır.
Farkların karesi alınarak toplama eklenir.
max_word_count, iki metinde bulunan toplam kelime sayılarının en büyüğüdür.
normalized_distance, distance değerinin max_word_count’a bölünmesiyle elde edilir.
Benzerlik skoru, 1 - normalized_distance formülüyle elde edilir.
Uzaklık ne kadar büyükse benzerlik o kadar düşük olacaktır.
sqlite3 modülünü kullanarak bir SQLite veritabanı (metinler.db) oluşturur ve metinleri saklamak için bir tablo (metinler) tanımlar.
add_text_to_db, verilen metni veritabanındaki tabloya eklemek için kullanılır.
İki örnek metin veritabanına eklenir ve ardından veritabanı kapatılır.
