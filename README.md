# 🐧 Penguin Desktop Pet

Một ứng dụng desktop pet dễ thương với nhân vật chim cánh cụt pixel có thể di chuyển và tương tác trên màn hình Windows.

## ✨ Tính năng

- **Animation mượt mà**: 8 frame hoạt hình liên tục
- **Kéo thả**: Click và kéo để di chuyển nhân vật đến vị trí mong muốn
- **Menu context**: Click chuột phải để mở menu với các tùy chọn
- **Cửa sổ trong suốt**: Không viền, luôn ở trên cùng
- **Nhiều cách đóng**: Click chuột phải, double click, hoặc click chuột giữa

## 🚀 Cách sử dụng

### Chạy từ source code:
```bash
# Cài đặt dependencies
py -m pip install -r requirements.txt

# Chạy chương trình
py penguin.py
```

### Chạy file .exe:
Tải file `PenguinDesktop.exe` từ thư mục `dist/` và chạy trực tiếp.

## 🎮 Điều khiển

| Hành động | Mô tả |
|-----------|-------|
| **Click chuột trái + kéo** | Di chuyển nhân vật |
| **Click chuột phải** | Mở menu context |
| **Double click chuột trái** | Đóng chương trình |
| **Click chuột giữa** | Đóng chương trình |

### Menu Context:
- **Di chuyển**: Bật/tắt khả năng kéo thả nhân vật
- **Đóng**: Đóng chương trình

## 📁 Cấu trúc project

```
penguin-desktop/
├── penguin.py          # Chương trình chính
├── frame_1.png         # Frame animation 1
├── frame_2.png         # Frame animation 2
├── frame_3.png         # Frame animation 3
├── frame_4.png         # Frame animation 4
├── frame_5.png         # Frame animation 5
├── frame_6.png         # Frame animation 6
├── frame_7.png         # Frame animation 7
├── frame_8.png         # Frame animation 8
├── requirements.txt    # Dependencies
├── README.md          # File này
└── dist/
    └── PenguinDesktop.exe  # File thực thi
```

## 🛠️ Công nghệ sử dụng

- **Python 3.12+**
- **Tkinter**: GUI framework
- **Pillow (PIL)**: Xử lý ảnh
- **PyInstaller**: Đóng gói thành .exe

## 📦 Đóng gói

Để tạo file .exe mới:
```bash
py -m PyInstaller --onefile --windowed --name "PenguinDesktop" penguin.py
```

## 🎨 Tùy chỉnh

### Thay đổi vị trí mặc định:
Sửa dòng này trong `penguin.py`:
```python
self.x = screen_width - self.sprite_size - 20  # Vị trí X
self.y = screen_height - self.sprite_size - 20  # Vị trí Y
```

### Thay đổi tốc độ animation:
```python
self.animation_speed = 300  # ms giữa các frame
```

### Thay đổi kích thước nhân vật:
```python
self.sprite_size = 64  # Kích thước pixel
```

## 🐛 Troubleshooting

### Lỗi "No module named 'PIL'":
```bash
py -m pip install Pillow
```

### Lỗi khi chạy .exe:
- Đảm bảo các file frame_*.png có trong cùng thư mục với .exe
- Chạy với quyền admin nếu cần

## 📝 License

MIT License - Tự do sử dụng và chỉnh sửa.

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo issue hoặc pull request.

---

**Lưu ý**: Đây là một desktop pet đơn giản, hoàn hảo để trang trí màn hình và thư giãn! 🐧✨