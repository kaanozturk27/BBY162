sorular = [" Fenerbahçe kaç yılında kurulmuştur? ", "77 plakalı ilimiz hangisidir? " , "Süperligin son şampiyon takımı hangisidir?","Basketbol kaç kişiyle oynanan bir spordur?"," Hollanda'nın başkenti neresidir?"]
cevaplar = ["A","C","D","B","A"]

cevapA= ["A: 1907", "A: Ankara","A: Fenerbahçe","A: 7","A: Amsterdam"]
cevapB= ["B: 1987", "B: İstanbul","B: Trabzonspor","B: 5","B: Münih"]
cevapC= ["C: 1807","C: Yalova","C: Beşiktaş","C: 11","C: Roma"]
cevapD= ["D: 1999","D: Manisa","D: Galatasaray","D: 8","D: Paris"]
puan = 0


print("5 soruluk genel kültür testimize hoşgeldiniz.")
print("Başarılar dileriz.")

for i in range(len(sorular)):
    print(sorular[i])
    print(cevapA[i])
    print(cevapB[i])
    print(cevapC[i])
    print(cevapD[i])
    cevap = input("Cevabınızı giriniz: ")
    if (cevaplar[i] == cevap.upper() ):

        puan +=1

print("Testi tamamladınız.")
print("Toplam puanınız:" +str(int(puan/len(sorular))*100))
