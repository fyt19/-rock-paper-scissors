import random

# Seçenekler listesi
secenekler = ['taş', 'kağıt', 'makas']

# Skorlar
oyuncu_skor = 0
bilgisayar_skor = 0

while True:
    # Kullanıcı girişi
    oyuncu_secimi = input("Taş mı, kağıt mı, makas mı? (Çıkış için 'q' tuşuna basın)")

    # Çıkış kontrolü
    if oyuncu_secimi == 'q':
        break

    # Bilgisayar seçimi
    bilgisayar_secimi = random.choice(secenekler)

    # Kazananı belirle
    if oyuncu_secimi == bilgisayar_secimi:
        print("Berabere!")
    elif oyuncu_secimi == 'taş':
        if bilgisayar_secimi == 'makas':
            print("Oyuncu kazandı!")
            oyuncu_skor += 1
        else:
            print("Bilgisayar kazandı!")
            bilgisayar_skor += 1
    elif oyuncu_secimi == 'kağıt':
        if bilgisayar_secimi == 'taş':
            print("Oyuncu kazandı!")
            oyuncu_skor += 1
        else:
            print("Bilgisayar kazandı!")
            bilgisayar_skor += 1
    elif oyuncu_secimi == 'makas':
        if bilgisayar_secimi == 'kağıt':
            print("Oyuncu kazandı!")
            oyuncu_skor += 1
        else:
            print("Bilgisayar kazandı!")
            bilgisayar_skor += 1

# Oyun bittiğinde skorları yazdır
print("Oyuncu skoru:", oyuncu_skor)
print("Bilgisayar skoru:", bilgisayar_skor)
