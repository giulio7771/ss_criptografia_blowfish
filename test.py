import blowfish

BS = 8
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[0:-ord(s[-1])]

def app():
    cipher = blowfish.Cipher(b"ABCDE")
    data = "FURB"
    data = bytes(pad(data), encoding='utf8')
    print(data)
    vi = b"12345678"
    data_encrypted = b"".join(cipher.encrypt_cbc(data, vi))
    data_decrypted = b"".join(cipher.decrypt_cbc(data_encrypted, vi))

    print(data_encrypted.hex())
    print(data_decrypted)

app()