"""
Configuration file for password generator.
Predefined character sets and password patterns.
"""

# Custom character sets
CUSTOM_CHARACTER_SETS = {
    'hexadecimal': '0123456789ABCDEF',
    'alphanumeric': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
    'letters_only': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'easy_symbols': '!@#$%&*+-=?',
    'no_similar': 'abcdefghjkmnpqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789!@#$%&*'
}

# Password strength profiles
PASSWORD_PROFILES = {
    'weak': {
        'length': 8,
        'lowercase': True,
        'uppercase': False,
        'digits': True,
        'symbols': False
    },
    'medium': {
        'length': 12,
        'lowercase': True,
        'uppercase': True,
        'digits': True,
        'symbols': False
    },
    'strong': {
        'length': 16,
        'lowercase': True,
        'uppercase': True,
        'digits': True,
        'symbols': True
    },
    'very_strong': {
        'length': 20,
        'lowercase': True,
        'uppercase': True,
        'digits': True,
        'symbols': True
    }
}