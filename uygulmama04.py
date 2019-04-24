# Soru1
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesini, bunların ortak kullanımını, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."
metin [0:21]

# soru2
liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]
for x in liste :
  print(x)
  
#soru3
sozluk = {"Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }

x = sozluk["Elma"]
y = sozluk ["Salatalık"]
if x  == input ():
  print(x)
elif y == input() :
  print (y)
else:
  print("Listede böyle bir öğe bulunmamaktadır")
