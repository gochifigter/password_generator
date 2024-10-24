"""
Secure Password Generator Module
Generates cryptographically secure random passwords
"""

import secrets
import string
from typing import List, Dict, Optional


class PasswordGenerator:
    """
    A secure password generator with customizable character sets and length
    """
    
    # Predefined character sets
    CHARACTER_SETS = {
        'lowercase': string.ascii_lowercase,
        'uppercase': string.ascii_uppercase,
        'digits': string.digits,
        'symbols': string.punctuation,
        'hexdigits': string.hexdigits,
        'letters': string.ascii_letters
    }
    
    def __init__(self):
        self.available_chars = ""
        self.min_length = 8
        self.max_length = 128
    
    def configure_character_set(self, 
                              include_lowercase: bool = True,
                              include_uppercase: bool = True,
                              include_digits: bool = True,
                              include_symbols: bool = True,
                              custom_chars: str = "") -> None:
        """
        Configure which character sets to include in password generation
        
        Args:
            include_lowercase: Include lowercase letters (a-z)
            include_uppercase: Include uppercase letters (A-Z)
            include_digits: Include digits (0-9)
            include_symbols: Include symbols (!@#$% etc.)
            custom_chars: Additional custom characters to include
        """
        self.available_chars = ""
        
        if include_lowercase:
            self.available_chars += self.CHARACTER_SETS['lowercase']
        if include_uppercase:
            self.available_chars += self.CHARACTER_SETS['uppercase']
        if include_digits:
            self.available_chars += self.CHARACTER_SETS['digits']
        if include_symbols:
            self.available_chars += self.CHARACTER_SETS['symbols']
        
        self.available_chars += custom_chars
        
        # Ensure we have at least some characters
        if not self.available_chars:
            self.available_chars = string.ascii_letters + string.digits
    
    def generate_password(self, length: int = 16) -> str:
        """
        Generate a secure random password
        
        Args:
            length: Desired password length (8-128 characters)
            
        Returns:
            str: Generated password
            
        Raises:
            ValueError: If length is invalid or no characters available
        """
        if not self.available_chars:
            self.configure_character_set()  # Use default configuration
        
        if length < self.min_length or length > self.max_length:
            raise ValueError(f"Password length must be between {self.min_length} and {self.max_length}")
        
        if len(self.available_chars) < 4:
            raise ValueError("Character set too small for secure password generation")
        
        # Generate password using cryptographically secure random
        password = ''.join(secrets.choice(self.available_chars) for _ in range(length))
        
        return password
    
    def generate_multiple_passwords(self, count: int = 5, length: int = 16) -> List[str]:
        """
        Generate multiple passwords at once
        
        Args:
            count: Number of passwords to generate
            length: Length of each password
            
        Returns:
            List of generated passwords
        """
        return [self.generate_password(length) for _ in range(count)]
    
    def get_password_strength(self, password: str) -> Dict[str, bool]:
        """
        Analyze password strength based on common criteria
        
        Args:
            password: Password to analyze
            
        Returns:
            Dictionary with strength indicators
        """
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_symbol = any(c in string.punctuation for c in password)
        sufficient_length = len(password) >= 12
        
        return {
            'has_lowercase': has_lower,
            'has_uppercase': has_upper,
            'has_digits': has_digit,
            'has_symbols': has_symbol,
            'sufficient_length': sufficient_length,
            'is_strong': all([has_lower, has_upper, has_digit, has_symbol, sufficient_length])
        }


def create_default_generator() -> PasswordGenerator:
    """Create a generator with secure default settings"""
    generator = PasswordGenerator()
    generator.configure_character_set(
        include_lowercase=True,
        include_uppercase=True,
        include_digits=True,
        include_symbols=True
    )
    return generator