# CTDLVGT: Ứng dụng giải mê cung bằng DFS và BFS

## Giới thiệu

Đây là chương trình minh họa việc áp dụng cấu trúc dữ liệu và thuật toán tìm kiếm
để giải một mê cung dạng ma trận 2 chiều. Chương trình xác định đường đi từ điểm
bắt đầu `S` đến điểm kết thúc `E`, sau đó hiển thị đường đi và số ô đã duyệt.

Dự án sử dụng hai thuật toán:

- **DFS (Depth-First Search - tìm kiếm theo chiều sâu):** đi sâu theo từng nhánh
  bằng đệ quy và quay lui khi gặp ngõ cụt.
- **BFS (Breadth-First Search - tìm kiếm theo chiều rộng):** duyệt mê cung theo
  từng lớp bằng hàng đợi, bảo đảm tìm được đường đi ngắn nhất khi mỗi bước có
  cùng chi phí.

## Mục tiêu

- Minh họa cách biểu diễn mê cung bằng ma trận 2 chiều.
- So sánh cách hoạt động của DFS và BFS.
- Hiển thị trực quan bản đồ, đường đi tìm được và số ô đã duyệt.
- Nhận xét sự khác nhau giữa hai thuật toán.

## Quy ước dữ liệu

Mỗi ô trong ma trận được biểu diễn bằng một số:

| Giá trị | Ý nghĩa | Ký hiệu hiển thị |
| ---: | --- | :---: |
| `0` | Đường đi | `.` |
| `1` | Tường | `#` |
| `2` | Điểm bắt đầu | `S` |
| `3` | Điểm kết thúc | `E` |

Khi một đường đi được tìm thấy, các ô trên đường đi được hiển thị bằng ký hiệu
`*`.

## Cấu trúc tệp

- [`1_Hoang_tien_ich_me_cung.py`](./1_Hoang_tien_ich_me_cung.py): khai báo các
  hằng số và hàm tiện ích như tìm vị trí, kiểm tra ô hợp lệ và in mê cung.
- [`2_Nhu_thuat_toan_dfs.py`](./2_Nhu_thuat_toan_dfs.py): cài đặt thuật toán DFS
  bằng đệ quy và quay lui.
- [`3_Truc_thuat_toan_bfs.py`](./3_Truc_thuat_toan_bfs.py): cài đặt thuật toán
  BFS bằng hàng đợi `deque` và truy vết ô cha.
- [`4_Hieu_menu_va_main.py`](./4_Hieu_menu_va_main.py): chương trình chính,
  menu lựa chọn, hiển thị kết quả và phần nhận xét.

## Cách chạy

Yêu cầu Python 3. Chạy tệp chương trình chính từ thư mục `CTDLGT`:

```bash
python 4_Hieu_menu_va_main.py
```

Sau khi chạy, chọn một chức năng trong menu:

1. Hiển thị bản đồ ban đầu.
2. Hiển thị kết quả tìm đường bằng DFS.
3. Hiển thị kết quả tìm đường bằng BFS.
4. So sánh kết quả của DFS và BFS.
0. Thoát chương trình.

## Kết quả minh họa

Với mê cung mẫu trong chương trình, BFS tìm được đường đi ngắn hơn DFS. Tuy
nhiên, DFS và BFS có thể duyệt số lượng ô khác nhau tùy theo cấu trúc mê cung và
thứ tự các hướng di chuyển.