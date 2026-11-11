# Phụ trách: Đinh Trung Hiếu - MSSV: 125000193
# Công việc: Hiển thị menu, hiển thị kết quả, phân tích nhận xét và điều phối chương trình chính (main)

from importlib import import_module
from pathlib import Path
import sys


sys.path.insert(0, str(Path(__file__).resolve().parent))

_tien_ich = import_module("1_Hoang_tien_ich_me_cung")
_dfs = import_module("2_Nhu_thuat_toan_dfs")
_bfs = import_module("3_Truc_thuat_toan_bfs")

BAT_DAU = _tien_ich.BAT_DAU
KET_THUC = _tien_ich.KET_THUC
tim_vi_tri = _tien_ich.tim_vi_tri
in_me_cung = _tien_ich.in_me_cung
giai_dfs = _dfs.giai_dfs
giai_bfs = _bfs.giai_bfs


def hien_thi_menu():
    print("\n========== MENU GIẢI MÊ CUNG ==========")
    print("1. Hiển thị bản đồ")
    print("2. Hiển thị kết quả DFS")
    print("3. Hiển thị kết quả BFS")
    print("4. Nhận xét")
    print("0. Thoát")


def hien_thi_ket_qua(ten_thuat_toan, maze, path, so_o_da_duyet):
    print(f"\nKẾT QUẢ {ten_thuat_toan}")
    print("(* là đường đi, # là tường, S là bắt đầu, E là kết thúc)")
    if path:
        in_me_cung(maze, path)
        print("Độ dài đường đi =", len(path) - 1, "bước")
    else:
        print("Không tìm thấy đường đi.")
    print("Số ô đã duyệt =", so_o_da_duyet)


if __name__ == "__main__":
    maze = [
        [2, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 3]
    ]

    bat_dau = tim_vi_tri(maze, BAT_DAU)
    ket_thuc = tim_vi_tri(maze, KET_THUC)
    path_dfs, duyet_dfs = giai_dfs(maze, bat_dau, ket_thuc)
    path_bfs, duyet_bfs = giai_bfs(maze, bat_dau, ket_thuc)

    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn: ").strip()

        if lua_chon == "0":
            print("Đã thoát chương trình.")
            break
        elif lua_chon == "1":
            print("\nBẢN ĐỒ BAN ĐẦU")
            print("(. là đường đi, # là tường, S là bắt đầu, E là kết thúc)")
            in_me_cung(maze)
        elif lua_chon == "2":
            hien_thi_ket_qua("DFS", maze, path_dfs, duyet_dfs)
        elif lua_chon == "3":
            hien_thi_ket_qua("BFS", maze, path_bfs, duyet_bfs)
        elif lua_chon == "4":
            print("\nNHẬN XÉT")
            if path_dfs and path_bfs:
                print("DFS: độ dài đường đi =", len(path_dfs) - 1,
                      "bước, số ô đã duyệt =", duyet_dfs)
                print("BFS: độ dài đường đi =", len(path_bfs) - 1,
                      "bước, số ô đã duyệt =", duyet_bfs)
                print("- BFS cho đường đi ngắn nhất vì duyệt theo từng lớp.")
                print("- DFS đi sâu một hướng nên đường đi có thể dài hơn.")
            else:
                print("Không tìm thấy đường đi bằng một trong hai thuật toán.")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 0 đến 4.")
