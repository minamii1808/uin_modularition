nama = 'Minami'
program = 'Gerak lurus'

print(f'program {program} oleh {nama}')

def hitung_kecepatan(jarak, waktu):
    kecepatan = jarak / waktu
    print (f'jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu/60}menit')
    print (f'sehingga kecepatan = {kecepatan} m/s')
    return jarak / waktu

# jarak = 1000
# waktu = 5 * 60
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan(3000, 70 * 60)


def hitung_kuatarus(bedapotensial, hambatan):
    kuatarus = bedapotensial / hambatan
    print(f'bedapotensial = {bedapotensial}V dibutuhkan dalam hambatan = {hambatan}Ohm')
    print(f'Sehingga kuatarus = {kuatarus} A')
    return bedapotensial / hambatan

# bedapotensial = 300
# hambatan = 10
kuatarus = hitung_kuatarus(300, 10)
kuatarus = hitung_kuatarus(400, 10)



