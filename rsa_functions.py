import number_theory_functions

class RSA():
    def __init__(self, public_key, private_key = None):
        self.public_key = public_key
        self.private_key = private_key


    @staticmethod
    def generate_e(a, phi):
        counter = 0
        while counter < phi:
            if number_theory_functions.extended_gcd(a%phi, phi)[0] == 1:
                return a
            a = a+1 
            counter = counter+1

    @staticmethod
    def generate(digits = 10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        q = number_theory_functions.generate_prime(digits // 2)
        p = number_theory_functions.generate_prime((digits // 2) - 1)
        N = q*p
        phi = (q-1) * (p-1)
        a = number_theory_functions.randrange(0, phi)
        e = RSA.generate_e(a, phi)
        d = number_theory_functions.modular_inverse(e, phi)
        
        return RSA((N,e), (N,d))

    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """

        c = number_theory_functions.modular_exponent(m, self.public_key[1], self.public_key[0])
        return c

    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        m = number_theory_functions.modular_exponent(c, self.private_key[1], self.private_key[0])
        return m
