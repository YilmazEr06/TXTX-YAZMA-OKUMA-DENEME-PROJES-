a='1'
with open("icerik.txt","r+",encoding="utf-8") as dosya:
    dosya.seek(0)
    metin= dosya.readlines()

    isim = metin[0].split("=")
    isim1= isim[1][:-1]

    ilkgiris=metin[1].split("=")
    ilkgiris1=ilkgiris[1][:-1]

    lisansdurum=metin[2].split("=")
    lisansdurum1=lisansdurum[1][:-1]

    lisans = metin[3].split("=")
    lisans1 = lisans[1][:-1]

    if (ilkgiris1=="0"):
        a= input("aramıza hoşgeldiniz adınız: " )
        metin[0]="isim="+a+"\n"
        metin[1]="ilkgiris=1\n"
        a = input("lisanssız ürün lisanslamak istermisniz? Y/N ")
        if (a == "y"):
            while True:
                b = input("lisans anahtarı girin ")
                if (b == lisans1):
                    print("tebrikler zengin")
                    metin[2] = "lisansdurum=1\n"
                    break
                else:
                    print("fakir bir daha dene")

    else:
        print("tekrar hoş geldiniz "+isim1)
        if (lisansdurum1=="0"):
            a=input("lisanssız ürün lisanslamak istermisniz? Y/N ")
            if(a=="y"):
                while True:
                    b= input("lisans anahtarı girin ")
                    if (b==lisans1):
                        print("tebrikler zengin")
                        metin[2] = "lisansdurum=1\n"
                        break
                    else:
                        print("fakir bir daha dene")

        else:
            print("mal sağlam")




    dosya.seek(0)
    dosya.writelines(metin)





