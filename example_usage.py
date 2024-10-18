"""
Example usage of the password generator.
"""

from password_generator import PasswordGenerator
from advanced_generator import AdvancedPasswordGenerator

def basic_examples():
    """Basic usage examples."""
    print("=== Basic Password Generator Examples ===")
    
    generator = PasswordGenerator()
    
    # Generate a default password (16 chars, all character sets)
    password1 = generator.generate_password()
    print(f"Default password: {password1}")
    
    # Generate a shorter numeric PIN
    pin = generator.generate_password(6, lowercase=False, uppercase=False, symbols=False, digits=True)
    print(f"6-digit PIN: {pin}")
    
    # Generate multiple passwords
    passwords = generator.generate_multiple_passwords(3, 12)
    print("3 passwords (12 chars each):")
    for i, pwd in enumerate(passwords, 1):
        print(f"  {i}. {pwd}")

def advanced_examples():
    """Advanced usage examples."""
    print("\n=== Advanced Password Generator Examples ===")
    
    advanced_gen = AdvancedPasswordGenerator()
    
    # Generate using profiles
    strong_password = advanced_gen.generate_with_profile('strong')
    strength = advanced_gen.estimate_strength(strong_password)
    print(f"Strong profile: {strong_password} [{strength}]")
    
    # Generate with custom character set
    hex_password = advanced_gen.generate_with_custom_charset(8, '0123456789ABCDEF')
    print(f"Hexadecimal password: {hex_password}")
    
    # Test password strength estimation
    test_passwords = [
        "abc",
        "password123",
        "Password123",
        "P@ssw0rd!2024",
        "V3ry$tr0ngP@ssw0rdW1thSp3c1@lCh@r5!"
    ]
    
    print("\n=== Password Strength Analysis ===")
    for pwd in test_passwords:
        strength = advanced_gen.estimate_strength(pwd)
        print(f"'{pwd}' -> {strength}")

if __name__ == "__main__":
    basic_examples()
    advanced_examples()