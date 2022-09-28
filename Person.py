import datetime


class Person:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        birth_date: str,
    ) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.birth_date: datetime.date = datetime.datetime.strptime(
            birth_date, "%Y-%m-%d"
        ).date()

    def print_info(self) -> None:
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age()} years")

    def age(self) -> int:
        today = datetime.date.today()
        return (
            today.year
            - self.birth_date.year
            - (
                (today.month, today.day)
                < (
                    self.birth_date.month,
                    self.birth_date.day,
                )
            )
        )

    def next_birthday(self):
        today = datetime.date.today()
        birthday = None
        if (today.month, today.day) > (
            self.birth_date.month,
            self.birth_date.day,
        ):
            birthday = datetime.date(
                today.year + 1, self.birth_date.month, self.birth_date.day
            )
        else:
            birthday = datetime.date(
                today.year, self.birth_date.month, self.birth_date.day
            )
        return (birthday - today).days


if __name__ == "__main__":
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    birth_date = input("Enter birthdate (yyyy-mm-dd): ")

    person = Person(first_name, last_name, birth_date)
    person.print_info()
    print(f"Days until next birthday: {person.next_birthday()}")
