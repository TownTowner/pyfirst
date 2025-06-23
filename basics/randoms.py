import random


def generate_random_number() -> int:
    return random.randint(1, 100)


def generate_random() -> int:
    return random.randrange(1, 100)


def main() -> None:
    random_number = generate_random_number()
    print(f"生成的随机数是: {random_number}")


if __name__ == "__main__":
    main()
