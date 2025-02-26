def reverse_string(s):
    """Возвращает строку в обратном порядке."""
    return s[::-1]

def is_palindrome(s):
    """Проверяет, является ли строка палиндромом."""
    return s == s[::-1]

def extract_vowels(s):
    """Возвращает гласные из строки."""
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in s if char in vowels])

def remove_duplicates(s):
    """Удаляет повторяющиеся символы из строки."""
    return ''.join(sorted(set(s), key=s.index))

test_string = "level"

print(reverse_string(test_string))

print(is_palindrome(test_string))

sample_string = "Hello, World!"
print(extract_vowels(sample_string))

duplicate_string = "aabbccddeeff"
print(remove_duplicates(duplicate_string))

