


def set_input_date() -> list:
    surname = input()
    name = input()
    patronymic = input()
    day = int(input())
    month = int(input())
    year = int(input())
    data = [surname, name, patronymic, day, month, year]
    return data




def main():
    set_input_date()


if __name__ == '__main__':
    main()
