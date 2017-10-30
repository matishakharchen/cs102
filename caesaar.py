def encrypt_caesar(plaintext):
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    text = str(plaintext)
    ciphertext = ""
    alphabet = 26
    step = 3
    for i in range(len(text)):
        char = text[i]
        if (97 <= ord(char)+step <= 122) or (65 <= ord(char)+step <= 90):
            ciphertext += chr(ord(char)+step)
        else:
            ciphertext += chr(ord(char)-alphabet+step)
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    text = str(ciphertext)
    plaintext = ""
    alphabet = 26
    step = 3
    for i in range(len(text)):
        char = text[i]
        if (97 <= ord(char)-step <= 122) or (65 <= ord(text[i])-step <= 90):
            plaintext += chr(ord(char)-step)
        else:
            plaintext += chr(ord(char)+alphabet-step)
    return plaintext


