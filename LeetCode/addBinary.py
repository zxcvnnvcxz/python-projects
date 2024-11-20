def addBinary(a: str, b: str) -> str:
    # Initialize pointers for both strings and the result
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    # Iterate through both strings from right to left
    while i >= 0 or j >= 0 or carry:
        # Get current digits (0 if out of bounds)
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0

        # Sum the digits and carry
        total = digit_a + digit_b + carry

        # Resulting bit is total % 2 (either 0 or 1)
        result.append(str(total % 2))

        # New carry is total // 2 (either 0 or 1)
        carry = total // 2

        # Move to the next digits
        i -= 1
        j -= 1

    # The result list will be in reverse order, so reverse it and join to form the final string
    return ''.join(result[::-1])


# Example usage
a = "1010"
b = "1011"
print(addBinary(a, b))  # Output: "10101"
