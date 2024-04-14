def get_even_squares(num_list):
    return [num**2 for num in num_list if num % 2 == 0]

def get_odd_cubes(num_list):
    cubes = []
    for num in num_list:
        if num % 2 != 0:
            cubes.append(num**3)
    return cubes

def get_sliced_list(num_list):
    return num_list[4:]

def format_numbers(numbers):
    formatted_numbers = []
    for num in numbers:
        formatted_numbers.append(f"{num:>8}")
    return formatted_numbers

# 主程式
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 獲取偶數平方值列表、奇數立方值列表、切片子列表
even_squares = get_even_squares(num_list)
odd_cubes = get_odd_cubes(num_list)
sliced_list = get_sliced_list(num_list)

# 格式化數字列表
formatted_even_squares = format_numbers(even_squares)
formatted_odd_cubes = format_numbers(odd_cubes)
formatted_sliced_list = format_numbers(sliced_list)

# 顯示結果
print("偶數平方值列表:")
print(", ".join(formatted_even_squares))
print("\n奇數立方值列表:")
print(", ".join(formatted_odd_cubes))
print("\n切片子列表:")
print(", ".join(formatted_sliced_list))