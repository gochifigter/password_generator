"""
Example usage of the password generator
"""

from password_generator import PasswordGenerator, create_default_generator
from advanced_generator import AdvancedPasswordGenerator


def basic_examples():
    """Basic password generation examples"""
    print("=== BASIC PASSWORD GENERATION ===")
    
    # Simple usage with defaults
    generator = create_default_generator()
    password = generator.generate_password(12)
    print(f"Default password: {password}")
    
    # Check strength
    strength = generator.get_password_strength(password)
    print(f"Strength: {strength}")
    
    # Generate multiple passwords
    print("\nMultiple passwords:")
    passwords = generator.generate_multiple_passwords(3, 16)
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}. {pwd}")


def custom_configuration():
    """Examples with custom configuration"""
    print("\n=== CUSTOM CONFIGURATION ===")
    
    generator = PasswordGenerator()
    
    # Only letters and digits
    generator.configure_character_set(
        include_lowercase=True,
        include_uppercase=True,
        include_digits=True,
        include_symbols=False
    )
    password = generator.generate_password(14)
    print(f"Letters + digits only: {password}")
    
    # Custom characters
    generator.configure_character_set(
        include_lowercase=True,
        include_uppercase=False,
        include_digits=True,
        include_symbols=False,
        custom_chars="€£¥"
    )
    password = generator.generate_password(10)
    print(f"With custom characters: {password}")


def advanced_examples():
    """Advanced generator examples"""
    print("\n=== ADVANCED FEATURES ===")
    
    advanced_gen = AdvancedPasswordGenerator()
    
    # Memorable password
    memorable = advanced_gen.generate_memorable_password()
    print(f"Memorable password: {memorable}")
    
    # Pattern-based password
    pattern_pwd = advanced_gen.generate_pattern_password("lluudds")
    print(f"Pattern password: {pattern_pwd}")
    
    # Passphrase
    passphrase = advanced_gen.generate_passphrase(word_count=4)
    print(f"Passphrase: {passphrase}")


if __name__ == '__main__':
    basic_examples()
    custom_configuration()
    advanced_examples()