"""Do stuff with letters."""
import random


class Letters:
    """Class for letters.
    
    Args:
        s (str): The letters to use.
    
    Example:
        A short usage example.
                
        >>> letters = Letters('abc')
        >>> print(letters)
        'abc'
    """
    def __init__(self, s: str):
        if not s.isalpha():
            raise ValueError("String must be only letters.")
        self._s = s
    
    def __repr__(self):
        return f"Letters({self._s})"

    def __str__(self):
        return self._s

    def shuffle(self):
        """Randomly shuffle the letters.
        
        Example:                    
            >>> letters = Letters('abcde')
            >>> letters.shuffle()
            >>> print(letters)
            'cabed'
        """
        self._s = ''.join(random.sample(self._s, len(self._s)))
    
    def get_random_letter(self):
        """Return a random letter.
        
        Returns:
            str: A random letter.
        """
        return random.choice(self._s)
