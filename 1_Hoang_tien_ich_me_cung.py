# Phụ trách: Nguyễn Văn Hoàng
# Công việc: Khai báo hằng số cấu hình và các hàm tiện ích xử lý mê cung (tim_vi_tri, in_me_cung, hop_le)

# Đề tài 15: Ứng dụng giải mê cung (Maze Solver)
# Mê cung là ma trận 2D: 0 = đường đi, 1 = tường, 2 = điểm bắt đầu (S), 3 = điểm kết thúc (E)

DUONG = 0
TUONG = 1
BAT_DAU = 2
KET_THUC = 3
HUONG = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def tim_vi_tri(maze, gia_tri):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == gia_tri:
                return (i, j)
    return None


def in_me_cung(maze, path=None):
    tap_hop_path = set(path) if path else set()
    for i in range(len(maze)):
        dong = ""
        for j in range(len(maze[0])):
            if maze[i][j] == TUONG:
                dong += "# "
            elif maze[i][j] == BAT_DAU:
                dong += "S "
            elif maze[i][j] == KET_THUC:
                dong += "E "
            elif (i, j) in tap_hop_path:
                dong += "* "
            else:
                dong += ". "
        print(dong)


def hop_le(maze, x, y):
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
        return False
    return maze[x][y] != TUONG
