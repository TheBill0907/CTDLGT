# Phụ trách: Nguyễn Hồng Thanh Trúc - MSSV: 125000161
# Công việc: Cài đặt thuật toán tìm kiếm theo chiều rộng (giai_bfs) dùng hàng đợi deque và truy vết ô cha

from collections import deque
from importlib import import_module


hop_le = import_module("1_Hoang_tien_ich_me_cung").hop_le
HUONG = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# BFS dùng hàng đợi (queue)
def giai_bfs(maze, bat_dau, ket_thuc):
    queue = deque([bat_dau])
    cha = {bat_dau: None}  # lưu ô cha để truy vết đường đi

    while queue:
        x, y = queue.popleft()
        if (x, y) == ket_thuc:
            break
        for dx, dy in HUONG:
            nx, ny = x + dx, y + dy
            if hop_le(maze, nx, ny) and (nx, ny) not in cha:
                cha[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    if ket_thuc not in cha:
        return None, len(cha)

    path = []
    o = ket_thuc
    while o is not None:
        path.append(o)
        o = cha[o]
    path.reverse()
    return path, len(cha)
