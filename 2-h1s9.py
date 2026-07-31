urun_fiyati = float(input("Ürün fiyatını girin: "))
kdv_orani = 20
kdv_tutari = urun_fiyati * (kdv_orani / 100)
kdvli_fiyat = urun_fiyati + kdv_tutari
print(f"KDV tutarı: {kdv_tutari:.2f} TL")
print(f"KDV'li fiyat: {kdvli_fiyat:.2f} TL")
