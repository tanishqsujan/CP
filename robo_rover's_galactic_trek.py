def count_paths(C, R1, R2):
    grid = [list(R1), list(R2)]
    visited = [[False for _ in range(C)] for _ in range(2)]
    paths = set()

    def backtrack(x, y, current_path):
        if len(current_path) == 2 * C:
            paths.add(''.join(current_path))
            return
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 0 <= ny < C and not visited[nx][ny]:
                visited[nx][ny] = True
                backtrack(nx, ny, current_path + [grid[nx][ny]])
                visited[nx][ny] = False

    for i in range(2):
        for j in range(C):
            visited[i][j] = True
            backtrack(i, j, [grid[i][j]])
            visited[i][j] = False

    return len(paths)

def main():
    T = int(input("Enter sectors (T): "))
    for _ in range(T):
        C = int(input("Enter number of columns (C): "))
        R1 = input("Enter first row (R1): ").strip()
        R2 = input("Enter second row (R2): ").strip()
        if len(R1) != C or len(R2) != C:
            print("Error: Row length does not match the number of columns.")
            continue
        print(f"Number of distinct paths: {count_paths(C, R1, R2)}")

if __name__ == "__main__":
    main()