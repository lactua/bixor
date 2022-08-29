from hashlib import sha256

def encrypt(
    content: str,
    key: str
):
    key = sha256(key.encode()).hexdigest()

    content_bins = ' '.join([bin(ord(char)).removeprefix('0b') for char in content])
    key_bins = ''.join([bin(ord(char)).removeprefix('0b') for char in key])

    return ''.join([' ' if char == ' ' else '1' if char == key_bins[index - len(key_bins) * (index // len(key_bins))] else '0' for index, char in list(enumerate(content_bins))])

def decrypt(
    encrypted_bins: str,
    key: str
):
    key = sha256(key.encode()).hexdigest()

    key_bins = ''.join([bin(ord(char)).removeprefix('0b') for char in key])

    decrypted_bins = ''.join([' ' if char == ' ' else '1' if char == key_bins[index - len(key_bins) * (index // len(key_bins))] else '0' for index, char in list(enumerate(encrypted_bins))])
    decrypted_bins = decrypted_bins.split()

    return ''.join([chr(int(char,2)) for char in decrypted_bins])