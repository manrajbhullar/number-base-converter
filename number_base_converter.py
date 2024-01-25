LETTER_VALS = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}


def to_decimal(num: str, base: int) -> str:
    """Convert number of any base to decimal."""
    if base < 2 or base > 16:
        raise ValueError(f"Invalid Base Value: {base}. Must be between 2-16.")
    
    if int(num) == 0:
        return "0"
    
    num_digits = len(num)
    decimal = 0
    for i in range(num_digits):
        if num[i].isalpha():
            if num[i].upper() not in LETTER_VALS.keys():
                raise ValueError(f"Invalid Number Value: {num}. Includes digit that is not supported.")
            current_digit = int(LETTER_VALS[num[i].upper()])
        else:
            current_digit = int(num[i])

        if current_digit >= base:
            raise ValueError(f"Invalid Number Value: {num}. Includes digit too high for base {base}.")
        
        position = num_digits-1 - i
        decimal +=  current_digit * base**position

    return str(decimal)


def from_decimal(num: str, target_base: int) -> str:
    """Convert decimal number to any base."""
    if target_base < 2 or target_base > 16:
        raise ValueError(f"Invalid Target Base Value: {target_base}. Must be between 2-16.")
    if num.isnumeric() == 0:
        raise ValueError(f"Invalid Number Value: {num}. Must be base 10 decimal number.")
    
    if int(num) == 0:
        return "0"
    
    remainders = []
    current_floor = int(num)
    while current_floor > 0:
        remainder = current_floor % target_base
        if remainder > 9:
            letter_key_index = list(LETTER_VALS.values()).index(remainder)
            remainder = list(LETTER_VALS.keys())[letter_key_index]
        remainders.append(str(remainder))
        current_floor = current_floor // target_base
    
    remainders.reverse()

    return ''.join(remainders)


def main():
    """Execute main script."""
    num = input("Enter number you want to convert: ")
    base = int(input("Enter the current base: "))
    target_base = int(input("Enter target base: "))

    decimal = to_decimal(num, base)
    result = from_decimal(decimal, target_base)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()