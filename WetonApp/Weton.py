HarKel_Lanang = input("Hari Kelahiran Umum (Pria): Minggu(1), Senin(2), Selasa(3), Rabu(4), Kamis(5), Jumat(6), Sabtu(7): ")
KelJa_Langan = input("Hari Kelahiran Jawa (Pria): Paing(1), Pon(2), Wage(3), Kliwon(4), Legi(5): ")

HarKel_Wedok = input("Hari Kelahiran Umum (Wanita): Minggu(1), Senin(2), Selasa1(3), Rabu(4), Kamis(5), Jumat(6), Sabtu(7): ")
KelJa_Wedok = input("Hari Kelahiran Jawa (Wanita): Paing(1), Pon(2), Wage(3), Kliwon(4), Legi(5): ")

#Itungan Hari Jawa
if KelJa_Langan == "Paing" or KelJa_Langan == "1":
    KelJa_Langan = 9
elif KelJa_Langan == "Pon" or KelJa_Langan == "2":
    KelJa_Langan = 7
elif KelJa_Langan == "Wage" or KelJa_Langan == "3":
    KelJa_Langan = 4
elif KelJa_Langan == "Kliwon" or KelJa_Langan == "4":
    KelJa_Langan = 8
elif KelJa_Langan == "Legi" or KelJa_Langan == "5":
    KelJa_Langan = 5

if KelJa_Wedok == "Paing" or KelJa_Wedok == "1":
    KelJa_Wedok = 9
elif KelJa_Wedok == "Pon" or KelJa_Wedok == "2":
    KelJa_Wedok = 7
elif KelJa_Wedok == "Wage" or KelJa_Wedok == "3":
    KelJa_Wedok = 4
elif KelJa_Wedok == "Kliwon" or KelJa_Wedok == "4":
    KelJa_Wedok = 8
elif KelJa_Wedok == "Legi" or KelJa_Wedok == "5":
    KelJa_Wedok = 5

#Itungan Hari Biasa
if HarKel_Lanang == "Minggu" or HarKel_Lanang == "1":
    HarKel_Lanang = 5
elif HarKel_Lanang == "Senin" or HarKel_Lanang == "2":
    HarKel_Lanang = 4
elif HarKel_Lanang == "Selasa" or HarKel_Lanang == "3":
    HarKel_Lanang = 3
elif HarKel_Lanang == "Rabu" or HarKel_Lanang == "4":
    HarKel_Lanang = 7
elif HarKel_Lanang == "Kamis" or HarKel_Lanang == "5":
    HarKel_Lanang = 8
elif HarKel_Lanang == "Jumat" or HarKel_Lanang == "6":
    HarKel_Lanang = 6
elif HarKel_Lanang == "Sabtu" or HarKel_Lanang == "7":
    HarKel_Lanang = 9

if HarKel_Wedok == "Minggu" or HarKel_Wedok == "1":
    HarKel_Wedok = 5
elif HarKel_Wedok == "Senin" or HarKel_Wedok == "2":
    HarKel_Wedok = 4
elif HarKel_Wedok == "Selasa" or HarKel_Wedok == "3":
    HarKel_Wedok = 3
elif HarKel_Wedok == "Rabu" or HarKel_Wedok == "4":
    HarKel_Wedok = 7
elif HarKel_Wedok == "Kamis" or HarKel_Wedok == "5":
    HarKel_Wedok = 8
elif HarKel_Wedok == "Jumat" or HarKel_Wedok == "6":
    HarKel_Wedok = 6
elif HarKel_Wedok == "Sabtu" or HarKel_Wedok == "7":
    HarKel_Wedok = 9

#Rumus
Lanang = int(HarKel_Lanang + KelJa_Langan)
Wedok = int(HarKel_Wedok + KelJa_Wedok)

Jumlah = Lanang + Wedok

#Output
if Jumlah == 1 or Jumlah == 9 or Jumlah == 17 or Jumlah == 25 or Jumlah == 33:
    print(Jumlah, "Pegat: Yen tibo PEGAT bakal nemu masalah, mbuh kuwi songko segi ekonomi, kekuasaan, selingkuh sing akhire iso pegatan")
elif Jumlah == 2 or Jumlah == 10 or Jumlah == 18 or Jumlah == 26 or Jumlah == 34:
    print(Jumlah, "Ratu: Yen tibo RATU iki jodoh banget. Di ajeni karo tonggo teparo lan wong liyo. Akeh wong iri karo keharmonisane")
elif Jumlah == 3 or Jumlah == 11 or Jumlah == 19 or Jumlah == 27 or Jumlah == 35:
    print(Jumlah, "Jodoh: Yen tibo JODOH cocok siji karo sijine. Iso podo-podo nerimo keluwehan lan kekurangan. Omah-omah lancar teko tuwo")
elif Jumlah == 4 or Jumlah == 12 or Jumlah == 20 or Jumlah == 28 or Jumlah == 36:
    print(Jumlah, "Topo: Yen tibo TOPO iki awal-awal e susah nanging tembe mburi penak. Awal-awal e kerep kenek masalah embuh kuwi songko segi ekonomi utowo liyone. Nanging yen wis ndue anak lan wis suwe anggone omah-omah bakal mulyo uripe")
elif Jumlah == 5 or Jumlah == 13 or Jumlah == 21 or Jumlah == 29:
    print(Jumlah, "Tinari: Yen tibo TINARI iki bakal nemu seneng. Penak anggone golek rejeki lan ora sampek urip kekurangan. Penak e tembung kerep nemu bejo anggone omah")
elif Jumlah == 6 or Jumlah == 14 or Jumlah == 22 or Jumlah == 30:
    print(Jumlah, "Padu: Yen tibo PADU iki bakal sering tukaran. Nanging sejana saben ndino tukaran tapi ora sampek pegatan. Mulo anggone omah-omah meh saben ndino tukaran embuh kui masalah opo wae")
elif Jumlah == 7 or Jumlah == 15 or Jumlah == 23 or Jumlah == 31:
    print(Jumlah, "Sujanan: Yen tibo SUJANAN iki kerep tukaran lan akeh-akeh masalah selingkuh. Embuh kuwi sing lanang po sing wadon opo malah loro-lorone podo la nduwe selingkuhan")
elif Jumlah == 8 or Jumlah == 16 or Jumlah == 24 or Jumlah == 32:
    print(Jumlah, "Pesthi: Yen tibo PESTHI iki omah-omah e bakal rukun, tentrem, adem ayem sampek tuwo. Senajan eneng masalah opo ae ora bakal ngrusak keharmonisan e")