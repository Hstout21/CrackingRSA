# Hunter Stout, 1/7/2025.

from sympy import mod_inverse
import struct as s
import sys

cipher = ((sys.stdin.buffer.readline().strip()).replace(b'\\n', b'\n')).rstrip(b'\n')
if len(cipher) % 8 != 0:
    padding = 8 - (len(cipher) % 8)
    cipher += b'\x00' * padding

e, n = map(int, sys.stdin.readline().strip().split())

encryptedList = list(s.unpack(f'<{len(cipher) // 8}Q', cipher))

def Decrypt(encryptedList, e, n):
    for p in range(2, n):
        if n % p == 0:
            q = n // p
            break
    return ''.join(chr(pow(i, mod_inverse(e, (p - 1) * (q - 1)), n)) for i in encryptedList)

print(Decrypt(encryptedList, e, n))