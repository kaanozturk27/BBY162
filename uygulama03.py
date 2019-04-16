from random import randint

adamCan = 5

kelimeler = ["amigo", "makedonya", "illegal", "kanıt"]
kelimelerA=["Çoğunlukla spor yarışmalrında seyircileri coşturan kimse","Antik Yunaninstan'da bir krallık ve bugün orta avrupadaki bir ülke","Yasa dışı olan şey","Bir şeyin doğruluğu, gerçekçiliği konusunda kanaat verici belge, delil, iz."]


kelimeSayisi = len(kelimeler)

secilen = randint(0, kelimeSayisi-1)

secilenKelime = kelimeler[secilen]
dizilenKelime = []
for diz in kelimeler[secilen]:
    dizilenKelime.append("_")
print(dizilenKelime)

if secilenKelime == kelimeler[0] :
  print(kelimelerA[0])
elif secilenKelime == kelimeler[1]  :
    print(kelimelerA[1])
elif secilenKelime == kelimeler[2]  :
  print(kelimelerA[2])
elif secilenKelime == kelimeler [3] :
  print(kelimelerA[3])

while adamCan > 0:
    girilenHarf = input("Bir harf giriniz: ")
    canKontrol = girilenHarf in secilenKelime
    if canKontrol == False:
        adamCan-=1
    i = 0
    for kontrol in secilenKelime:
        if secilenKelime[i] == girilenHarf:
            dizilenKelime[i] = girilenHarf
        i+=1
    print(dizilenKelime)
    print("Kalan can: "+ str(adamCan))

    if "_" not in dizilenKelime:
      print("Tebrikler kelimeyi bildiniz!")
      break
    if adamCan == 0:
      print ("Malesef kelimeyi bilemediniz...")