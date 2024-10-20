## Secure Password Generator

A Python-based secure password generator that creates cryptographically strong random passwords with customizable options.

### Features

- **Cryptographically Secure**: Uses Python's `secrets` module for true randomness
- **Customizable Length**: Generate passwords from 4 to any reasonable length
- **Character Set Control**: Choose which character types to include
- **Multiple Passwords**: Generate multiple passwords at once
- **Strength Profiles**: Predefined profiles for different security needs
- **Custom Character Sets**: Use predefined or custom character sets
- **Strength Estimation**: Analyze password strength

### Installation

No installation required! This script uses only Python standard library modules.

```bash
# Clone or download the files
# Ensure you have Python 3.6+ installed
```

### Basic Usage

#### Command Line

```bash
# Generate a default 16-character password
python password_generator.py

# Generate a 12-character password
python password_generator.py -l 12

# Generate 5 passwords
python password_generator.py -n 5

# Generate password without symbols
python password_generator.py --no-symbols

# Generate numeric PIN (6 digits)
python password_generator.py -l 6 --no-lowercase --no-uppercase --no-symbols
```

#### Python Code

```python
from password_generator import PasswordGenerator

# Create generator instance
generator = PasswordGenerator()

# Generate default password (16 chars, all character sets)
password = generator.generate_password()
print(password)

# Generate custom password
password = generator.generate_password(
    length=20,
    lowercase=True,
    uppercase=True,
    digits=True,
    symbols=False
)

# Generate multiple passwords
passwords = generator.generate_multiple_passwords(5, 12)
```

### Advanced Features

```python
from advanced_generator import AdvancedPasswordGenerator

advanced_gen = AdvancedPasswordGenerator()

# Use predefined strength profiles
password = advanced_gen.generate_with_profile('strong')

# Generate with custom character set
password = advanced_gen.generate_with_custom_charset(10, 'ABC123')

# Estimate password strength
strength = advanced_gen.estimate_strength("MyPassword123!")
print(strength)  # Output: "Medium"
```

### Files Overview

- `password_generator.py` - Main password generator class and CLI
- `config.py` - Configuration for custom character sets and profiles
- `advanced_generator.py` - Extended features and strength analysis
- `example_usage.py` - Demonstration of various use cases
- `requirements.txt` - Dependency list (empty - uses stdlib only)

### Security Notes

- Uses cryptographically secure random number generator (`secrets` module)
- Ensures at least one character from each selected character set
- Passwords are properly shuffled to avoid patterns
- No passwords are stored or logged

### Requirements

- Python 3.6 or higher
- No external dependencies

Run the examples to see the generator in action:
```bash
python example_usage.py
```