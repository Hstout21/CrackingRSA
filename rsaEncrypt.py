# Hunter Stout, 1/7/2025.

import struct as s
import sys

plaintext = sys.stdin.readline().strip()
e, n = map(int, sys.stdin.readline().strip().split())

encrypted = [pow(ord(char), e, n) for char in plaintext]
sys.stdout.buffer.write(s.pack(f'<{len(encrypted)}Q', *encrypted))