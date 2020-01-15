from math import sqrt
import random

LOWER = 10000
UPPER = 20000
alphabet = ['_', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
              'U', 'V', 'W', 'X', 'Y', 'Z']

def isPrime(nr):
    if nr < 1:
        return False
    elif nr == 2 or nr == 1:
        return True
    else:
        d = 3
        while d <= sqrt(nr):
                if nr % d == 0 or nr % 2 == 0:
                    return False
                d = d + 2
        return True

def generatePrimeNumber(lower, upper):
    nr = random.randint(lower, upper)
    if isPrime(nr):
        return nr
    else:
        return generatePrimeNumber(lower, upper)

def generatePQ():
    p = generatePrimeNumber(LOWER, UPPER)
    q = generatePrimeNumber(LOWER, UPPER)
    while p == q:
        q = generatePrimeNumber(LOWER, UPPER)
    return p, q

def computePhi(p, q):
    return (p-1)*(q-1)

def gcd(a, b):
    if a == b:
        return a
    else:
        if a > b :
            return gcd(a-b, b)
        else:
            return gcd(a, b-a)

def coprime(a, b):
    return gcd(a, b) == 1

def modulo_inverse(n, m):
    for i in range(1, m):
        if (n * i) % m == 1:
            return i
    return -1

def generateAlicePublic():
    p, q = generatePQ()
    phi = computePhi(p, q)
    e = random.randint(1, phi - 1)
    while not coprime(e, phi):
        e = random.randint(1, phi - 1)
    d = modulo_inverse(e, phi)
    return (p * q, e), d

def determineBlockSizes(n):
    low_k = 1
    alphabet_size = len(alphabet)
    acc = alphabet_size
    while acc < n:
        acc = acc * alphabet_size
        low_k += 1
    k = random.randint(2, low_k)
    l = random.randint(low_k + 1, 2*low_k)
    return k, l

def splitMessage(message,k):
    put_in_block = 0
    blocks = []
    for char in message:
        if put_in_block == 0:
            blocks.append(char)
        else:
            blocks[-1] += char
        put_in_block += 1
        if put_in_block == k:
            put_in_block = 0
    while put_in_block < k:
        blocks[-1] += " "
        put_in_block += 1
    return blocks

def numericalEquivalent(messageBlocks):
    numbers = []
    alphabet_size = len(alphabet)
    for block in messageBlocks:
        reverse = block[::-1]
        currentPow = 0
        blockNumber = 0
        for char in reverse:
            blockNumber += alphabet.index(char) * (alphabet_size ** currentPow)
            currentPow += 1
        numbers.append(blockNumber)
    return numbers

def encryptBlocks(numerical_eqivalence, e, n):
    encrypted_blocks = []
    for number in numerical_eqivalence:
        enc = pow(number, e, n)
        encrypted_blocks.append(enc)
    return encrypted_blocks

def textEquivalent(numerical_blocks, l):
    text_blocks = []
    alphabet_size = len(alphabet)
    current_pow = l - 1
    for number in numerical_blocks:
        text = ""
        while current_pow >= 0:
            digit = number // (alphabet_size ** current_pow)
            number = number % (alphabet_size ** current_pow)
            letter = alphabet[digit]
            text += letter
            current_pow -= 1
        text_blocks.append(text)
        current_pow = l - 1
    return text_blocks


def decryptBlocks(num_blocks, d, n):
    decrypted = []
    for number in num_blocks:
        dec = pow(number, d, n)
        decrypted.append(dec)
    return decrypted


def encrypt(message):
    private, d = generateAlicePublic()
    n = private[0]
    e = private[1]
    k, l = determineBlockSizes(n)
    numerical_blocks = numericalEquivalent(splitMessage(message, k))
    encrypted_numbers = encryptBlocks(numerical_blocks, e, n)
    text_encrypted = textEquivalent(encrypted_numbers, l)
    print("Encrypted text is :")
    print(text_encrypted)
    return encrypted_numbers, d, n, k


def decrypt(encrypted_blocks, d, n, k):
    decrypted_blocks = decryptBlocks(encrypted_blocks, d, n)
    text_decrypted = textEquivalent(decrypted_blocks, k)
    print("Decrypted text is:")
    print(text_decrypted)
    return text_decrypted


def main():
    while True:
        message = input("Give the message(" "A-Z): ")
        numbers, d, n, k = encrypt(message)
        decrypt(numbers, d, n, k)

if __name__ == '__main__':
    main()