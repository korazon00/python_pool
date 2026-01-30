
class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:

        self.name: str = name
        self._height: int = 0
        self._age: int = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, height: int) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self.get_height()}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self.get_age()} days [OK]\n")
        else:
            print(f"Invalid operation attempted: age {age}cm [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"Current plant: {self.name}", end=" ")
        print(f"({self.get_height()}cm, {self.get_age()} days)")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 0, 0)
    plant.get_info()


if __name__ == "__main__":
    ft_garden_security()
