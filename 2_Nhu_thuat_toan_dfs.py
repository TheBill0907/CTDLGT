# Phụ trách: Trần Thị Quỳnh Như - MSSV: 125000162
# Công việc: Cài đặt thuật toán tìm kiếm theo chiều sâu (giai_dfs) bằng đệ quy và quay lui

from importlib import import_module


hop_le = import_module("1_Hoang_tien_ich_me_cung").hop_le
HUONG = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# DFS dùng đệ quy
def giai_dfs(maze, bat_dau, ket_thuc):
    visited = set()
    path = []

    def dfs(x, y):
        visited.add((x, y))
        path.append((x, y))
        if (x, y) == ket_thuc:
            return True
        for dx, dy in HUONG:
            nx, ny = x + dx, y + dy
            if hop_le(maze, nx, ny) and (nx, ny) not in visited:
                if dfs(nx, ny):
                    return True
        path.pop()  # quay lui khi gặp ngõ cụt
        return False

    if dfs(bat_dau[0], bat_dau[1]):
        return path, len(visited)
    return None, len(visited)
