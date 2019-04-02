sorular = [    " Fenerbahçe 1907 yılında kurulmuştur. E/H ", "77 plakalı ilimiz Yalova'dır. E/H," ,"Süperligin son şampiyonu Galatasaray'dır.E/H","Basketbol 11 kişiyle oynanan bir spordur. E/H"," Hollanda'nın başkenti Berlin'dir. E/H"]
cevaplar = ["E","E","E","H","H"]

puan = 0

print("5 soruluk genel kültür testimize hoşgeldiniz.")
print("Başarılar dileriz.")
print(sorular[0])
ccevap=input("Cevabınız: ")
if cevaplar[0] == ccevap.upper() :
      print("Doğru cevap 20 puan kazadınız.")
      puan =puan+20
      print("Mevcut puanınız: " + " " + str(puan) + "\n")
else :
    print("Cevabınız doğru değil.")
    print("Mevcut puanınız: "+ " " + str(puan)+"\n")

print(sorular[1])
ccevap=input("Cevabınız: ")
if cevaplar[1] == ccevap.upper() :
      print("Doğru cevap 20 puan kazadınız.")
      puan = puan + 20
      print("Mevcut puanınız: " + " " + str(puan) + "\n")
else :
    print("Cevabınız doğru değil.")
    print("Mevcut puanınız: "+ " " + str(puan)+"\n")

print(sorular[2])
ccevap=input("Cevabınız: ")
if cevaplar[2] == ccevap.upper() :
      print("Doğru cevap 20 puan kazadınız.")
      puan =puan+20
      print("Mevcut puanınız: " + " " + str(puan) + "\n")
else :
    print("Cevabınız doğru değil.")
    print("Mevcut puanınız: "+ " " + str(puan)+"\n")

print(sorular[3])
ccevap=input("Cevabınız: ")
if cevaplar[3] == ccevap.upper() :
      print("Doğru cevap 20 puan kazadınız.")
      puan =puan+20
      print("Mevcut puanınız: " + " " + str(puan) + "\n")
else :
    print("Cevabınız doğru değil.")
    print("Mevcut puanınız: "+ " " + str(puan)+"\n")

print(sorular[4])
ccevap=input("Cevabınız: ")
if cevaplar[4] == ccevap.upper() :
      print("Doğru cevap 20 puan kazadınız.")
      puan =puan+20
      print("Mevcut puanınız: " + " " + str(puan) + "\n")
      print("Testimiz bitmiştir katıldığınız için teşekkür ederiz.")

else :
    print("Cevabınız doğru değil.")
    print("Mevcut puanınız: "+ " " + str(puan)+"\n")
    print("Testimiz bitmiştir katıldığınız için teşekkür ederiz.")
