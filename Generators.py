from itertools import chain


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


def flat_generator(ls: list):
    res = [elem for elem in chain(*ls)]
    for obj in res:
        yield obj


def main():
    for item in flat_generator(nested_list):
        print(item)

    flat_list = [item for item in flat_generator(nested_list)]
    print(flat_list)


if __name__ == "__main__":
    main()
