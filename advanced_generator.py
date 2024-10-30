"""
Advanced password generator with pattern-based generation
"""

import secrets
from typing import List, Optional
from password_generator import PasswordGenerator


class AdvancedPasswordGenerator(PasswordGenerator):
    """
    Extended password generator with advanced features
    """
    
    def generate_memorable_password(self, 
                                  word_count: int = 4,
                                  separator: str = '-',
                                  capitalize: bool = True) -> str:
        """
        Generate a memorable but secure password using word-like patterns
        
        Args:
            word_count: Number of word-like segments
            separator: Character to separate segments
            capitalize: Whether to capitalize segments
            
        Returns:
            Memorable password string
        """
        # Common syllable patterns for pronounceable passwords
        syllables = [
            'ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu',
            'da', 'de', 'di', 'do', 'du', 'fa', 'fe', 'fi', 'fo', 'fu',
            'ga', 'ge', 'gi', 'go', 'gu', 'ha', 'he', 'hi', 'ho', 'hu',
            'ja', 'je', 'ji', 'jo', 'ju', 'ka', 'ke', 'ki', 'ko', 'ku',
            'la', 'le', 'li', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu',
            'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu',
            'ra', 're', 'ri', 'ro', 'ru', 'sa', 'se', 'si', 'so', 'su',
            'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu',
            'za', 'ze', 'zi', 'zo', 'zu', 'cha', 'che', 'chi', 'cho', 'chu',
            'sha', 'she', 'shi', 'sho', 'shu', 'tha', 'the', 'thi', 'tho', 'thu'
        ]
        
        words = []
        for _ in range(word_count):
            # Create word-like pattern (2-3 syllables)
            syllable_count = secrets.choice([2, 3])
            word = ''.join(secrets.choice(syllables) for _ in range(syllable_count))
            
            if capitalize:
                word = word.capitalize()
            
            words.append(word)
        
        # Add a random number at the end for extra security
        words.append(str(secrets.randbelow(90) + 10))  # 10-99
        
        return separator.join(words)
    
    def generate_pattern_password(self, pattern: str = "lllddss") -> str:
        """
        Generate password based on pattern
        
        Args:
            pattern: Pattern where:
                   l = lowercase, u = uppercase, d = digit, s = symbol
                   
        Returns:
            Pattern-based password
        """
        char_map = {
            'l': string.ascii_lowercase,
            'u': string.ascii_uppercase,
            'd': string.digits,
            's': string.punctuation
        }
        
        password = []
        for char_type in pattern:
            if char_type in char_map:
                password.append(secrets.choice(char_map[char_type]))
            else:
                # If pattern character not recognized, use all available
                self.configure_character_set()
                password.append(secrets.choice(self.available_chars))
        
        return ''.join(password)
    
    def generate_passphrase(self, 
                          word_list: Optional[List[str]] = None,
                          word_count: int = 6,
                          separator: str = ' ') -> str:
        """
        Generate a passphrase using a word list
        
        Args:
            word_list: Custom word list (uses default if None)
            word_count: Number of words in passphrase
            separator: Word separator
            
        Returns:
            Generated passphrase
        """
        if word_list is None:
            # Common words for passphrases
            word_list = [
                'apple', 'river', 'mountain', 'sunshine', 'whisper', 'crystal',
                'forest', 'ocean', 'butterfly', 'thunder', 'silence', 'journey',
                'garden', 'mirror', 'shadow', 'diamond', 'freedom', 'harmony',
                'victory', 'wonder', 'courage', 'passion', 'mystery', 'treasure',
                'horizon', 'melody', 'twilight', 'destiny', 'infinity', 'universe'
            ]
        
        if len(word_list) < word_count:
            raise ValueError("Word list too small for requested passphrase")
        
        words = secrets.SystemRandom().sample(word_list, word_count)
        return separator.join(words)


# Example usage
if __name__ == '__main__':
    advanced_gen = AdvancedPasswordGenerator()
    
    print("Memorable Password:", advanced_gen.generate_memorable_password())
    print("Pattern Password:", advanced_gen.generate_pattern_password("lluudds"))
    print("Passphrase:", advanced_gen.generate_passphrase())