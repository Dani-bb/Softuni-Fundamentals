def closest_point_to_center(x1, y1, x2, y2):
    distance1 = x1**2 + y1**2  # Calculate distance of point 1 from the center
    distance2 = x2**2 + y2**2  # Calculate distance of point 2 from the center

    if distance1 <= distance2:  # Check if point 1 is closer or at the same distance as point 2
        print(f"({x1:3f}, {y1:0f})")  # Print point 1
    else:
        print(f"({x2:1f}, {y2:0f})")  # Print point 2

x1 = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())

closest_point_to_center(x1,x2,x3,x4)