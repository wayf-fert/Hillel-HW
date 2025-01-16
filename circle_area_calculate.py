import math


def calculate_circle_area(r: float) -> float:
    """
    Обчислює площу кола за його радіусом.

    Args:
        r (float): Радіус кола.

    Returns:
        float: Площа кола.
    """
    return math.pi * r ** 2


radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"CIRCLE AREA: {area:.2f}")
