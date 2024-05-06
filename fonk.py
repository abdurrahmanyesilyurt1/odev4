from collections import Counter

def word_frequency_distance(text1, text2):
    # Her iki metni kelimelere ayır ve sıklık sözlüklerini oluştur
    words1 = text1.lower().split()
    words2 = text2.lower().split()
    freq1 = Counter(words1)
    freq2 = Counter(words2)

    # Tüm benzersiz kelimelerin birleşimini bul
    all_words = set(freq1.keys()).union(set(freq2.keys()))

    # Kelime uzaklığı skorunu hesapla
    distance = sum((freq1[word] - freq2[word]) ** 2 for word in all_words)

    # Normalize skor
    max_word_count = max(sum(freq1.values()), sum(freq2.values()))
    normalized_distance = distance / max_word_count

    return 1 - normalized_distance  # Benzerlik skoru olarak 1'den çıkar

# Örnek metinler ve benzerlik hesaplaması
text1 = "Bu metin de örnek bir metindir ve ortak kelimeler içermektedir."
text2 = "Bu metin de örnek bir metindir ve ortak kelimeler df."

similarity_score = word_frequency_distance(text1, text2)
print(f"Benzerlik Skoru: {similarity_score:.2f}")

# Sonucu bir dosyaya yazdırma
with open('benzerlik_durumu.txt', 'w') as f:
    f.write(f"Benzerlik Skoru: {similarity_score:.2f}")