class Rectangle:
    """
    Клас для представлення прямокутника.
    """

    def __init__(self, init_width: float, init_height: float) -> None:
        """ Ініціалізує прямокутник із заданими шириною та висотою. """
        self.width = init_width
        self.height = init_height

    def area(self) -> float:
        """ Повертає площу прямокутника."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Повертає периметр прямокутника."""
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        """Перевіряє, чи є прямокутник квадратом."""
        return self.width == self.height

    def resize(self, init_new_width: float, init_new_height: float) -> float:
        """Змінює розміри прямокутника."""
        self.width = init_new_width
        self.height = init_new_height


width = float(input("Enter width of rectangle: "))
height = float(input("Enter height of rectangle: "))

# Створюємо об'єкт прямокутника
rect = Rectangle(width, height)

print(f"Width: {rect.width}, Height: {rect.height}")
print(f"Area: {rect.area()}")
print(f"Perimetr: {rect.perimeter()}")
print(f"Is square?: {'YES' if rect.is_square() else 'NO'}")

# Змінюємо розміри прямокутника
new_width = float(input("Enter new width rectangle: "))
new_height = float(input("Enter new_height rectangle: "))

rect.resize(new_width, new_height)

print("\nAfter changes:")
print(f"Width: {rect.width}, Height: {rect.height}")
print(f"Area: {rect.area()}")
print(f"Perimetr: {rect.perimeter()}")
print(f"Is square?:  {'YES' if rect.is_square() else 'NO'}")
