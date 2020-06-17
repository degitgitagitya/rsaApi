def RSA():
    p=int(input('Enter prime p: '))
    q=int(input('Enter prime q: '))
    print("Choosen primes:")
    print("p =", p, ", q =", q)
    n=p*q
    print("n = p * q = " + str(n) + "\n")
    phi=(p-1)*(q-1)
    print("Euler's function (totient) [phi(n)]:", phi)
    def gcd(a, b):
        while b != 0:
            c = a % b
            a = b
            b = c
        return a
    def modinv(a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None
    def coprimes(a):
        l = [x for x in range(2, a) 
             if gcd(a, x) == 1 
                 and modinv(x, phi) is not None
                 and modinv(x, phi) != x]
        return l
    print("Pilih satu bilangan koprima dibawah ini:\n")
    print(coprimes(phi), "\n")
    e=int(input())
    d=modinv(e,phi)
    print("\nKunci Publik (e=" + str(e) + ", n=" + str(n) + ").\n")
    print("Kunci Private (d=" + str(d) + ", n=" + str(n) + ").\n")
    def encrypt_block(m):
        c = modinv(m**e, n)
        if c == None: print('Tidak ada invers multiplikasi modular blok ' + str(m) + '.')
        return c
    def decrypt_block(c):
        m = modinv(c**d, n)
        if m == None: print('Tidak ada invers multiplikasi modular blok ' + str(c) + '.')
        return m
    def encrypt_string(s):
        return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
    def decrypt_string(s):
        return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])

    def main(): 
        print('--------------------')
        print('--------------------')
        pilihan = int(input('1.Enkripsi\n2.Dekripsi\n------------------------\nPilih menu: '))
        if pilihan == 1: 
            s = input("Masukkan pesan: ")
            print("\nPesan: " + s + "\n")
            enc = encrypt_string(s)
            print("Enkrispi: " + enc + "\n")
        if pilihan == 2: 
            s = input("Masukkan ciphertext: ")
            print("\nciphertext: " + s + "\n")
            dec = decrypt_string(s)
            print("Dekripsi: " + dec + "\n")

    if __name__ == '__main__': 
        main()

if __name__ == '__main__': 
    RSA()

input()