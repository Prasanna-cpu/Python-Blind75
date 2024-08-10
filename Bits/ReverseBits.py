


def reverseBits(n):
    binary_str=bin(n)[2:].zfill(32)[::-1]

    rev_int=int(binary_str,2)

    return rev_int


print(reverseBits(8))

