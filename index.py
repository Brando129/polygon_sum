# Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).

def internal_angles_sum(sides):
    total = (sides - 2) * 180

    return f"The sum of the internal angles is {total}" + "°"

print(internal_angles_sum(6))