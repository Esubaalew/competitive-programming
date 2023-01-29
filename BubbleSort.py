
def CountSwaps(numbers: str):
    count: int = 0
    n = numbers[0]

    numbers = numbers[1:].strip().split()

    for i in range(len(numbers)):

        for j in range(0, len(numbers) - i - 1):

            if numbers[j] > numbers[j + 1]:

                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
                count += 1

    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {numbers[0]}')
    print(f'Last Element: {numbers[-1]}')
