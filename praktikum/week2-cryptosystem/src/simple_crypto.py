import random

CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

def generate_key(seed):
    """Membangkitkan kunci acak deterministik dari seed (key)"""
    random.seed(seed)
    shuffled = list(CHARSET)
    random.shuffle(shuffled)
    return ''.join(shuffled)

def encrypt(plaintext, key):
    enc_table = generate_key(key)
    result = ""
    for char in plaintext:
        if char in CHARSET:
            index = CHARSET.index(char)
            result += enc_table[index]
        else:
            result += char  # spasi & simbol tetap
    return result

def decrypt(ciphertext, key):
    enc_table = generate_key(key)
    result = ""
    for char in ciphertext:
        if char in enc_table:
            index = enc_table.index(char)
            result += CHARSET[index]
        else:
            result += char
    return result


if __name__ == "__main__":
    message = "Nur Fatahillah 230202772"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
