import math

# Öklid Mesafesi Fonksiyonu
def oklidMesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0])**2 + (nokta2[1] - nokta1[1])**2)

# Noktalar listesi (2D uzayında)
noktalari = [(1, 2), (4, 6), (5, 8), (9, 3), (7, 1)]  # Buradaki noktaları istediğiniz gibi değiştirebilirsiniz

# Tüm nokta çiftleri arasındaki mesafeleri hesapla
mesafeler = []
for i in range(len(noktalari)):
    for j in range(i + 1, len(noktalari)):
        mesafe = oklidMesafesi(noktalari[i], noktalari[j])
        mesafeler.append(mesafe)

# Minimum mesafeyi bul
min_mesafe = min(mesafeler)

# Sonucu yazdır
print("Minimum Öklid mesafesi:", min_mesafe)
