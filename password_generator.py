"""
Secure Password Generator
Generates cryptographically secure random passwords with customizable options.
"""

import secrets
import string
import argparse
from typing import List

class PasswordGenerator:
    """A secure password generator with customizable character sets."""
    
    def __init__(self):
        self.character_sets = {
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'digits': string.digits,
            'symbols': string.punctuation
        }
    
    def generate_password(self, length: int = 16, **options) -> str:
        """
        Generate a secure random password.
        
        Args:
            length (int): Length of the password (default: 16)
            **options: Character set options (lowercase, uppercase, digits, symbols)
        
        Returns:
            str: Generated password
        
        Raises:
            ValueError: If no character sets are selected or length is too short
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
        
        # Default to all character sets if none specified
        use_lowercase = options.get('lowercase', True)
        use_uppercase = options.get('uppercase', True)
        use_digits = options.get('digits', True)
        use_symbols = options.get('symbols', True)
        
        # Build character pool
        char_pool = ""
        if use_lowercase:
            char_pool += self.character_sets['lowercase']
        if use_uppercase:
            char_pool += self.character_sets['uppercase']
        if use_digits:
            char_pool += self.character_sets['digits']
        if use_symbols:
            char_pool += self.character_sets['symbols']
        
        if not char_pool:
            raise ValueError("At least one character set must be selected")
        
        # Ensure at least one character from each selected set
        password_chars = []
        if use_lowercase:
            password_chars.append(secrets.choice(self.character_sets['lowercase']))
        if use_uppercase:
            password_chars.append(secrets.choice(self.character_sets['uppercase']))
        if use_digits:
            password_chars.append(secrets.choice(self.character_sets['digits']))
        if use_symbols:
            password_chars.append(secrets.choice(self.character_sets['symbols']))
        
        # Fill remaining characters randomly from the pool
        remaining_length = length - len(password_chars)
        for _ in range(remaining_length):
            password_chars.append(secrets.choice(char_pool))
        
        # Shuffle the password to randomize character positions
        secrets.SystemRandom().shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def generate_multiple_passwords(self, count: int = 5, length: int = 16, **options) -> List[str]:
        """
        Generate multiple passwords at once.
        
        Args:
            count (int): Number of passwords to generate
            length (int): Length of each password
            **options: Character set options
        
        Returns:
            List[str]: List of generated passwords
        """
        return [self.generate_password(length, **options) for _ in range(count)]

def main():
    """Command-line interface for the password generator."""
    parser = argparse.ArgumentParser(description='Generate secure random passwords')
    parser.add_argument('-l', '--length', type=int, default=16, 
                       help='Password length (default: 16)')
    parser.add_argument('-n', '--number', type=int, default=1,
                       help='Number of passwords to generate (default: 1)')
    parser.add_argument('--no-lowercase', action='store_true',
                       help='Exclude lowercase letters')
    parser.add_argument('--no-uppercase', action='store_true',
                       help='Exclude uppercase letters')
    parser.add_argument('--no-digits', action='store_true',
                       help='Exclude digits')
    parser.add_argument('--no-symbols', action='store_true',
                       help='Exclude symbols')
    
    args = parser.parse_args()
    
    generator = PasswordGenerator()
    
    options = {
        'lowercase': not args.no_lowercase,
        'uppercase': not args.no_uppercase,
        'digits': not args.no_digits,
        'symbols': not args.no_symbols
    }
    
    try:
        if args.number == 1:
            password = generator.generate_password(args.length, **options)
            print(f"Generated password: {password}")
        else:
            passwords = generator.generate_multiple_passwords(args.number, args.length, **options)
            print(f"Generated {args.number} passwords:")
            for i, password in enumerate(passwords, 1):
                print(f"{i}. {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()