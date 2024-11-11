"""
Secure Password Generator Module
Generates cryptographically secure random passwords
"""

import secrets
import string
from typing import List, Dict

class PasswordGenerator:
    """Secure password generator with customizable character sets"""
    
    # Predefined character sets
    CHARACTER_SETS = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'digits': string.digits,
        'symbols': string.punctuation,
        'hex': string.hexdigits,
        'alphanumeric': string.ascii_letters + string.digits
    }
    
    def __init__(self):
        self.available_chars = ""
    
    def set_character_set(self, char_types: List[str]) -> None:
        """
        Set the character set for password generation
        
        Args:
            char_types: List of character types to include
                      Options: 'lowercase', 'uppercase', 'digits', 
                              'symbols', 'hex', 'alphanumeric'
        """
        self.available_chars = ""
        for char_type in char_types:
            if char_type in self.CHARACTER_SETS:
                self.available_chars += self.CHARACTER_SETS[char_type]
        
        if not self.available_chars:
            raise ValueError("No valid character types specified")
    
    def set_custom_character_set(self, custom_chars: str) -> None:
        """
        Set a custom character set for password generation
        
        Args:
            custom_chars: String containing custom characters to use
        """
        if not custom_chars:
            raise ValueError("Custom character set cannot be empty")
        self.available_chars = custom_chars
    
    def generate_password(self, length: int = 16) -> str:
        """
        Generate a secure random password
        
        Args:
            length: Length of the password (default: 16)
            
        Returns:
            str: Generated password
            
        Raises:
            ValueError: If character set is not set or length is invalid
        """
        if not self.available_chars:
            raise ValueError("Character set not configured. Use set_character_set() first.")
        
        if length < 1:
            raise ValueError("Password length must be at least 1")
        
        # Use secrets module for cryptographically secure random generation
        password = ''.join(secrets.choice(self.available_chars) for _ in range(length))
        return password
    
    def generate_multiple_passwords(self, length: int = 16, count: int = 5) -> List[str]:
        """
        Generate multiple passwords at once
        
        Args:
            length: Length of each password
            count: Number of passwords to generate
            
        Returns:
            List[str]: List of generated passwords
        """
        return [self.generate_password(length) for _ in range(count)]
    
    def get_password_strength(self, password: str) -> Dict[str, bool]:
        """
        Analyze password strength
        
        Args:
            password: Password to analyze
            
        Returns:
            Dict with strength indicators
        """
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)
        
        return {
            'length_adequate': len(password) >= 12,
            'has_lowercase': has_lower,
            'has_uppercase': has_upper,
            'has_digits': has_digit,
            'has_symbols': has_symbol,
            'is_strong': len(password) >= 12 and has_lower and has_upper and has_digit
        }