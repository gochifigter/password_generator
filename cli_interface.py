"""
Command-line interface for the password generator
"""

import argparse
import sys
from typing import List
from password_generator import PasswordGenerator, create_default_generator


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Secure Password Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Generate one 16-character password
  %(prog)s -l 20                    # Generate one 20-character password
  %(prog)s -n 5 -l 12               # Generate five 12-character passwords
  %(prog)s --no-symbols             # Generate password without symbols
  %(prog)s --custom "€£¥"           # Include custom characters
        """
    )
    
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=16,
        help='Password length (default: 16, min: 8, max: 128)'
    )
    
    parser.add_argument(
        '-n', '--number',
        type=int,
        default=1,
        help='Number of passwords to generate (default: 1)'
    )
    
    # Character set options
    char_group = parser.add_argument_group('Character Set Options')
    char_group.add_argument(
        '--no-lowercase',
        action='store_false',
        dest='include_lowercase',
        default=True,
        help='Exclude lowercase letters'
    )
    
    char_group.add_argument(
        '--no-uppercase',
        action='store_false',
        dest='include_uppercase',
        default=True,
        help='Exclude uppercase letters'
    )
    
    char_group.add_argument(
        '--no-digits',
        action='store_false',
        dest='include_digits',
        default=True,
        help='Exclude digits'
    )
    
    char_group.add_argument(
        '--no-symbols',
        action='store_false',
        dest='include_symbols',
        default=True,
        help='Exclude symbols'
    )
    
    char_group.add_argument(
        '--custom',
        type=str,
        default='',
        help='Additional custom characters to include'
    )
    
    # Output options
    output_group = parser.add_argument_group('Output Options')
    output_group.add_argument(
        '--no-strength',
        action='store_true',
        help='Do not show password strength analysis'
    )
    
    output_group.add_argument(
        '--copy',
        action='store_true',
        help='Copy first password to clipboard (requires pyperclip)'
    )
    
    return parser.parse_args()


def display_passwords(passwords: List[str], show_strength: bool = True) -> None:
    """Display generated passwords with optional strength analysis"""
    generator = create_default_generator()
    
    print("\n" + "="*50)
    print("GENERATED PASSWORDS")
    print("="*50)
    
    for i, password in enumerate(passwords, 1):
        print(f"\n{i:2d}. {password}")
        
        if show_strength:
            strength = generator.get_password_strength(password)
            print("    Strength Analysis:")
            print(f"    - Length: {len(password)} characters")
            print(f"    - Lowercase: {'✓' if strength['has_lowercase'] else '✗'}")
            print(f"    - Uppercase: {'✓' if strength['has_uppercase'] else '✗'}")
            print(f"    - Digits: {'✓' if strength['has_digits'] else '✗'}")
            print(f"    - Symbols: {'✓' if strength['has_symbols'] else '✗'}")
            print(f"    - Overall: {'STRONG' if strength['is_strong'] else 'WEAK'}")


def copy_to_clipboard(text: str) -> bool:
    """Attempt to copy text to clipboard"""
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except ImportError:
        return False


def main():
    """Main CLI function"""
    args = parse_arguments()
    
    try:
        # Create and configure generator
        generator = PasswordGenerator()
        generator.configure_character_set(
            include_lowercase=args.include_lowercase,
            include_uppercase=args.include_uppercase,
            include_digits=args.include_digits,
            include_symbols=args.include_symbols,
            custom_chars=args.custom
        )
        
        # Generate passwords
        if args.number == 1:
            passwords = [generator.generate_password(args.length)]
        else:
            passwords = generator.generate_multiple_passwords(args.number, args.length)
        
        # Display results
        display_passwords(passwords, not args.no_strength)
        
        # Copy to clipboard if requested
        if args.copy and passwords:
            if copy_to_clipboard(passwords[0]):
                print(f"\n✓ First password copied to clipboard!")
            else:
                print(f"\n⚠ Could not copy to clipboard. Install pyperclip: pip install pyperclip")
        
        print("\n" + "="*50)
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)


if __name__ == '__main__':
    main()