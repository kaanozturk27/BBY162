# Soru1
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
print(metin [0:21])

# soru2
liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for x in liste :
  print(x)
  
#soru3
sozluk = {"Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }

x =input("Bir kelime giriniz")

if x == "Elma":
  print(sozluk["Elma"])
elif x == "Salatalık" :
  print (sozluk["Salatalık"])
else:
  print("Listede böyle bir öğe bulunmamaktadır")
