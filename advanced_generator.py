"""
Advanced password generator with additional features.
"""

import secrets
from password_generator import PasswordGenerator
from config import CUSTOM_CHARACTER_SETS, PASSWORD_PROFILES

class AdvancedPasswordGenerator(PasswordGenerator):
    """Extended password generator with additional features."""
    
    def __init__(self):
        super().__init__()
        self.custom_sets = CUSTOM_CHARACTER_SETS
        self.profiles = PASSWORD_PROFILES
    
    def generate_with_profile(self, profile_name: str) -> str:
        """
        Generate password using predefined strength profile.
        
        Args:
            profile_name (str): Name of the profile ('weak', 'medium', 'strong', 'very_strong')
        
        Returns:
            str: Generated password
        
        Raises:
            ValueError: If profile name is invalid
        """
        if profile_name not in self.profiles:
            raise ValueError(f"Unknown profile: {profile_name}. Available: {list(self.profiles.keys())}")
        
        profile = self.profiles[profile_name]
        return self.generate_password(
            length=profile['length'],
            lowercase=profile['lowercase'],
            uppercase=profile['uppercase'],
            digits=profile['digits'],
            symbols=profile['symbols']
        )
    
    def generate_with_custom_charset(self, length: int, charset: str) -> str:
        """
        Generate password using custom character set.
        
        Args:
            length (int): Password length
            charset (str): Custom character set string
        
        Returns:
            str: Generated password
        
        Raises:
            ValueError: If charset is empty or too short
        """
        if not charset:
            raise ValueError("Character set cannot be empty")
        
        if len(charset) < 2:
            raise ValueError("Character set must contain at least 2 characters")
        
        return ''.join(secrets.choice(charset) for _ in range(length))
    
    def estimate_strength(self, password: str) -> str:
        """
        Estimate password strength based on character diversity and length.
        
        Args:
            password (str): Password to analyze
        
        Returns:
            str: Strength rating ('Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong')
        """
        if len(password) < 8:
            return "Very Weak"
        
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(not c.isalnum() for c in password)
        
        char_types = sum([has_lower, has_upper, has_digit, has_symbol])
        length = len(password)
        
        if length >= 20 and char_types == 4:
            return "Very Strong"
        elif length >= 16 and char_types >= 3:
            return "Strong"
        elif length >= 12 and char_types >= 2:
            return "Medium"
        elif length >= 8:
            return "Weak"
        else:
            return "Very Weak"

def demo():
    """Demonstrate the advanced generator features."""
    generator = AdvancedPasswordGenerator()
    
    print("=== Password Generator Demo ===")
    
    # Generate with profiles
    for profile in ['weak', 'medium', 'strong', 'very_strong']:
        password = generator.generate_with_profile(profile)
        strength = generator.estimate_strength(password)
        print(f"{profile.title()} profile: {password} [{strength}]")
    
    print("\n=== Custom Character Sets ===")
    
    # Generate with custom character sets
    for name, charset in generator.custom_sets.items():
        if len(charset) > 10:  # Use first 10 chars for display
            display_chars = charset[:10] + "..."
        else:
            display_chars = charset
        
        password = generator.generate_with_custom_charset(12, charset)
        print(f"{name}: {password} (chars: {display_chars})")

if __name__ == "__main__":
    demo()