length = float(input())
width = float(input())

wp_by_width = (width * 100 - 100) // 70
wp_by_length = (length * 100) // 120
overall_places = wp_by_length * wp_by_width - 3
print(int(overall_places))


