"""
Command Line Interface for Password Generator
"""

import argparse
import sys
from typing import List
from password_generator import PasswordGenerator

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Secure Password Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli_interface.py -l 20
  python cli_interface.py -l 16 -c lowercase uppercase digits symbols
  python cli_interface.py -l 12 -n 3 --custom "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
        """
    )
    
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=16,
        help='Password length (default: 16)'
    )
    
    parser.add_argument(
        '-c', '--char-types',
        nargs='+',
        choices=['lowercase', 'uppercase', 'digits', 'symbols', 'hex', 'alphanumeric'],
        default=['lowercase', 'uppercase', 'digits', 'symbols'],
        help='Character types to include'
    )
    
    parser.add_argument(
        '--custom',
        type=str,
        help='Custom character set'
    )
    
    parser.add_argument(
        '-n', '--count',
        type=int,
        default=1,
        help='Number of passwords to generate (default: 1)'
    )
    
    parser.add_argument(
        '--no-strength-check',
        action='store_true',
        help='Skip password strength analysis'
    )
    
    return parser.parse_args()

def main():
    """Main CLI function"""
    args = parse_arguments()
    
    try:
        generator = PasswordGenerator()
        
        # Set character set
        if args.custom:
            generator.set_custom_character_set(args.custom)
            print(f"Using custom character set: {args.custom}")
        else:
            generator.set_character_set(args.char_types)
            print(f"Using character types: {', '.join(args.char_types)}")
        
        # Generate passwords
        if args.count == 1:
            password = generator.generate_password(args.length)
            print(f"\nGenerated Password: {password}")
            
            if not args.no_strength_check:
                strength = generator.get_password_strength(password)
                print("\nPassword Strength Analysis:")
                print(f"  Length: {len(password)} characters")
                print(f"  Contains lowercase: {'✓' if strength['has_lowercase'] else '✗'}")
                print(f"  Contains uppercase: {'✓' if strength['has_uppercase'] else '✗'}")
                print(f"  Contains digits: {'✓' if strength['has_digits'] else '✗'}")
                print(f"  Contains symbols: {'✓' if strength['has_symbols'] else '✗'}")
                print(f"  Overall strength: {'STRONG' if strength['is_strong'] else 'WEAK'}")
        
        else:
            passwords = generator.generate_multiple_passwords(args.length, args.count)
            print(f"\nGenerated {args.count} passwords:")
            for i, password in enumerate(passwords, 1):
                print(f"{i:2d}. {password}")
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)

if __name__ == "__main__":
    main()