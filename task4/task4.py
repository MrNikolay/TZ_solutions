import sys

def main(numbers):
    m = numbers[len(numbers) // 2]
    print(sum(abs(n - m) for n in numbers))


if __name__ == "__main__":
    assert len(sys.argv) >= 2, "Программа ожидает один обязательный аргумент!"

    with open(sys.argv[1], 'r') as file:
        numbers = sorted(map(int, file.readlines()))
    
    main(numbers)