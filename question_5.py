import rsa_functions
import number_theory_functions

p = 7919
q = 6841
N = p*q
phi = (q-1) * (p-1)
a = number_theory_functions.randrange(0, phi)
e = rsa_functions.RSA.generate_e(a, phi)
d = number_theory_functions.modular_inverse(e, phi)
rsa = rsa_functions.RSA((N,e), (N,d))
print("e:")
print(e)
M = 42
encrypted = rsa_functions.RSA.encrypt(rsa, 42)
print("encrypted:")
print(encrypted)
decrypted = rsa_functions.RSA.decrypt(rsa, encrypted)
print("decrypted:")
print(decrypted)
