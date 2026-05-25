# Password Strength Checker

A simple yet effective password strength checker tool that evaluates passwords based on multiple security criteria.

## Features

- **Length Validation**: Ensures passwords are at least 8 characters long
- **Character Variety**: Checks for:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special symbols
- **Repeated Character Detection**: Identifies sequences of 3+ identical characters
- **Strength Scoring**: Provides clear feedback on password strength (Weak, Medium, Strong)

## Usage

### Running the Script

```bash
python password_checker.py
```

### Interactive Mode

Once running, you'll be prompted to enter passwords. The tool will provide instant feedback on password strength:

```
🔐  Password Strength Checker
--------------------------------------------------
Enter your password (or 'quit' to exit): 
```

### Example Outputs

- **Strong Password**: `✅ STRONG — Excellent password!`
- **Medium Password**: `⚠️ MEDIUM — Add more variety to strengthen it.`
- **Weak Password**: `❌ WEAK — Missing uppercase, lowercase, numbers, or symbols.`
- **Repeated Characters**: `⚠️ MEDIUM — Avoid repeated characters in sequence.`

## Password Criteria

| Criteria | Requirement |
|----------|-------------|
| Minimum Length | 8 characters |
| Uppercase | At least 1 (A-Z) |
| Lowercase | At least 1 (a-z) |
| Digits | At least 1 (0-9) |
| Symbols | At least 1 special character |
| No Repeats | No 3+ identical characters in sequence |

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Author

Danish Gulzar

## License

This project is open source and available for educational purposes.
