cüzdandakipara = float(input("Cüzdandaki para miktarını giriniz: "))
alışveriş = float(input("Alışveriş tutarını giriniz: "))
kalanpara = cüzdandakipara - alışveriş
if kalanpara < 0:
    print("Yetersiz bakiye!")
else:
    print(f"Kalan para: {kalanpara:.2f}")
