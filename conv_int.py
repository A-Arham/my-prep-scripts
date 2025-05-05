# Given the string representations of two integers, return the string representation of the sum of those integers.

# For example:

# sumStrings('1','2') // => '3'
# A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

# I have removed the use of BigInteger and BigDecimal in java

# Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.

def sum_strings(a, b):
    a = a.lstrip('0') or '0'
    b = b.lstrip('0') or '0'

    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    carry = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        digit_sum = int(a[i]) + int(b[i]) + carry
        carry = digit_sum // 10
        result.append(str(digit_sum % 10))

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1]).lstrip('0') or '0'



in1,in2="123", "456"
sum_strings(in1,in2)

