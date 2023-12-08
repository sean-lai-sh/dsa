def reverse_vowels(input_str):
    # use list constructor
    # use join string method [ a, b, c] => [b, a ,c]
    left_pointer = 0
    right_pointer = len(input_str) - 1
    list_str = list(input_str)
    vowels = "aeiou"
    while left_pointer < right_pointer:
        temp_left = list_str[left_pointer]
        temp_right = list_str[right_pointer]
        if temp_left in vowels and temp_right in vowels:
            list_str[left_pointer], list_str[right_pointer] = (
                list_str[right_pointer],
                list_str[left_pointer],
            )
            left_pointer += 1
            right_pointer -= 1
        if temp_left not in vowels:
            left_pointer += 1
        if temp_right not in vowels:
            right_pointer -= 1
    return "".join(list_str)


print(reverse_vowels("Tandon"))
