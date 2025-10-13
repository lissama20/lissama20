def minimum_path_sum(triangle):

    if not triangle:
        return 0
    
    
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            
            triangle[row][col] += min(
                triangle[row + 1][col], 
                triangle[row + 1][col + 1]
            )
    
    return triangle[0][0]

def get_minimum_path(triangle):

    if not triangle:
        return [], 0
    
   
    dp = [row[:] for row in triangle]
    path = []
    
    
    for row in range(len(dp) - 2, -1, -1):
        for col in range(len(dp[row])):
            dp[row][col] += min(dp[row + 1][col], dp[row + 1][col + 1])
    
   
    col = 0
    for row in range(len(dp)):
        path.append(triangle[row][col])
        if row < len(dp) - 1:
            
            if dp[row + 1][col] < dp[row + 1][col + 1]:
                col = col  
            else:
                col = col + 1  
    
    return path, dp[0][0]


if __name__ == "__main__":
    # Первый пример
    triangle1 = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    path1, sum1 = get_minimum_path(triangle1)
    print(f"Треугольник 1: {triangle1}")
    print(f"Минимальный путь: {' → '.join(map(str, path1))}")
    print(f"Результат: {sum1}")
    print()
    
    # Второй пример
    triangle2 = [[-1], [2, 3], [1, -1, -3], [4, 2, 1, 3]]
    path2, sum2 = get_minimum_path(triangle2)
    print(f"Треугольник 2: {triangle2}")
    print(f"Минимальный путь: {' → '.join(map(str, path2))}")
    print(f"Результат: {sum2}")