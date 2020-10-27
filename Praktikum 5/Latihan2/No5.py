#5
print('Hai...nama saya mr, lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silahkan tebak ya!!!')
ta=int(input('Tebakan Anda : '))
while True:
    if(ta<10):
        print('Hehehe.....Bilangan tebakan anda terlalu kecil')
        ta=int(input('Tebakan Anda : '))
    elif(ta>10):
        print('Hehehe.....Bilangan tebakan anda terlalu besar')
        ta=int(input('Tebakan Anda : '))
    elif(ta==10):
        print('yeeee...Bilangan tebakan anda benar')
        break
