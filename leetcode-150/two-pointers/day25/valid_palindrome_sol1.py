def is_palindrome(s: str) -> bool:
    # Normalize the string
    normalized = ''.join(char.lower() for char in s if char.isalnum())
    # Check palindrome using slicing
    return normalized == normalized[::-1]