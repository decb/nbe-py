import string

class NameGenerator:
    alphabet = string.ascii_lowercase

    def __init__(self):
        self.alphabet_size = len(self.alphabet)
        self._count = 0
   
    def next(self):
        result = ""
        n = self._count
        while n:
            result += self.alphabet[n % self.alphabet_size]
            n //= self.alphabet_size
        self._count += 1
        return result[::-1] or self.alphabet[0]
