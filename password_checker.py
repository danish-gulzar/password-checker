import string

def check_password_strength(password):
    
    if len(password) < 8:
        return "❌ WEAK — Password must be at least 8 characters long."

    has_upper  = any(char.isupper()                   for char in password)
    has_lower  = any(char.islower()                   for char in password)
    has_digit  = any(char.isdigit()                   for char in password)
    has_symbol = any(char in string.punctuation       for char in password)

    # Check for repeated characters (3+ in a row)
    has_repeated = any(password[i] == password[i+1] == password[i+2] for i in range(len(password) - 2))

    score = 0
    if has_upper:  score += 1
    if has_lower:  score += 1
    if has_digit:  score += 1
    if has_symbol: score += 1

    if has_repeated:
        return "⚠️ MEDIUM — Avoid repeated characters in sequence."

    if score == 4:
        return "✅ STRONG — Excellent password!"
    elif score == 3:
        return "⚠️ MEDIUM — Add more variety to strengthen it."
    else:
        return "❌ WEAK — Missing uppercase, lowercase, numbers, or symbols."

if __name__ == "__main__":
    print("🔐  Password Strength Checker")
    print("-" * 50)
    
    while True:
        password = input("Enter your password (or 'quit' to exit): ").strip()
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not password:
            print("\n❌ Error: Password cannot be empty.\n")
            continue
        
        result = check_password_strength(password)
        print("\nResult:", result)
        print()