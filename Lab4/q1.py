def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("WRONG TYPE")
    if len(s) == 0:
        return True
    left_pointer = 0
    right_pointer = len(s) - 1
    while left_pointer < right_pointer:
        temp_left = s[left_pointer]
        temp_right = s[right_pointer]
        if temp_right != temp_left:
            return False
        right_pointer -= 1
        left_pointer += 1
    return True

print(is_palindrome("TasaT")) # True
print(is_palindrome("Task")) # False
print(is_palindrome([1,2,3,4])) # Raise Type Error