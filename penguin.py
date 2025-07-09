import tkinter as tk
from PIL import Image, ImageTk
import itertools
import random
import threading
import time

class PenguinDesktop:
    def __init__(self):
        # Tạo cửa sổ chính
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # Không có viền cửa sổ
        self.root.wm_attributes("-topmost", True)  # Luôn ở trên cùng
        self.root.wm_attributes("-transparentcolor", "white")  # Màu trắng trong suốt
        self.root.attributes("-alpha", 0.9)  # Độ trong suốt nhẹ
        
        # Kích thước nhân vật
        self.sprite_size = 64
        self.canvas = tk.Canvas(
            self.root, 
            width=self.sprite_size, 
            height=self.sprite_size, 
            bg='white', 
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Load tất cả frame ảnh
        self.frames = []
        for i in range(1, 9):  # Load từ frame_1.png đến frame_8.png
            try:
                img = Image.open(f"frame_{i}.png")
                # Resize về kích thước 64x64
                img = img.resize((self.sprite_size, self.sprite_size), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.frames.append(photo)
            except Exception as e:
                print(f"Không thể load frame_{i}.png: {e}")
        
        if not self.frames:
            print("Không tìm thấy frame nào! Vui lòng kiểm tra các file frame_*.png")
            return
        
        # Tạo cycle cho animation
        self.frame_cycle = itertools.cycle(self.frames)
        self.current_frame = next(self.frame_cycle)
        
        # Tạo sprite trên canvas
        self.sprite = self.canvas.create_image(
            self.sprite_size//2, 
            self.sprite_size//2, 
            image=self.current_frame
        )
        
        # Vị trí cố định ở góc màn hình (góc phải dưới)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.x = screen_width - self.sprite_size - 20  # Cách lề phải 20px
        self.y = screen_height - self.sprite_size - 20  # Cách lề dưới 20px
        
        # Cập nhật vị trí cửa sổ
        self.root.geometry(f"+{self.x}+{self.y}")
        
        # Biến điều khiển
        self.running = True
        self.animation_speed = 300  # ms giữa các frame (chậm hơn nữa)
        
        # Bind events
        self.root.bind("<Double-Button-1>", self.close_app)  # Double click chuột trái
        self.root.bind("<Button-2>", self.close_app)  # Click chuột giữa (scroll wheel)
        
        # Bind drag & drop events
        self.root.bind("<Button-1>", self.start_drag)  # Click chuột trái để bắt đầu kéo
        self.root.bind("<B1-Motion>", self.drag)       # Kéo chuột
        self.root.bind("<ButtonRelease-1>", self.stop_drag)  # Thả chuột
        
        # Biến cho drag & drop
        self.dragging = False
        self.drag_x = 0
        self.drag_y = 0
        
        # Tạo menu context (chuột phải)
        self.create_context_menu()
        
        # Bắt đầu animation
        self.animate()
        
    def animate(self):
        """Cập nhật frame animation"""
        if self.running:
            self.current_frame = next(self.frame_cycle)
            self.canvas.itemconfig(self.sprite, image=self.current_frame)
            self.root.after(self.animation_speed, self.animate)
    

    
    def start_drag(self, event):
        """Bắt đầu kéo thả"""
        self.dragging = True
        self.drag_x = event.x_root - self.x
        self.drag_y = event.y_root - self.y
    
    def drag(self, event):
        """Kéo thả nhân vật"""
        if self.dragging:
            new_x = event.x_root - self.drag_x
            new_y = event.y_root - self.drag_y
            
            # Giới hạn trong màn hình
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            
            if new_x < 0:
                new_x = 0
            elif new_x > screen_width - self.sprite_size:
                new_x = screen_width - self.sprite_size
                
            if new_y < 0:
                new_y = 0
            elif new_y > screen_height - self.sprite_size:
                new_y = screen_height - self.sprite_size
            
            self.x = new_x
            self.y = new_y
            self.root.geometry(f"+{self.x}+{self.y}")
    
    def stop_drag(self, event):
        """Dừng kéo thả"""
        self.dragging = False
    
    def create_context_menu(self):
        """Tạo menu context khi click chuột phải"""
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Di chuyển", command=self.toggle_draggable)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="Đóng", command=self.close_app)
        
        # Bind chuột phải để hiển thị menu
        self.root.bind("<Button-3>", self.show_context_menu)
        
        # Biến để bật/tắt drag
        self.draggable = True
    
    def show_context_menu(self, event):
        """Hiển thị menu context"""
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def toggle_draggable(self):
        """Bật/tắt khả năng kéo thả"""
        self.draggable = not self.draggable
        if self.draggable:
            print("Đã bật kéo thả")
        else:
            print("Đã tắt kéo thả")
    
    def start_drag(self, event):
        """Bắt đầu kéo thả"""
        if not self.draggable:
            return
        self.dragging = True
        self.drag_x = event.x_root - self.x
        self.drag_y = event.y_root - self.y
    
    def close_app(self, event=None):
        """Đóng ứng dụng"""
        print("Đang đóng Penguin Desktop...")
        self.running = False
        self.root.quit()
        self.root.destroy()
    
    def run(self):
        """Chạy ứng dụng"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.close_app()

if __name__ == "__main__":
    print("Khởi động Penguin Desktop...")
    print("Hướng dẫn:")
    print("- Click chuột trái và kéo để di chuyển nhân vật")
    print("- Click chuột phải để mở menu (Di chuyển/Đóng)")
    print("- Double click chuột trái để đóng")
    print("- Click chuột giữa (scroll wheel) để đóng")
    print("- Trong menu: có thể bật/tắt khả năng kéo thả")
    
    app = PenguinDesktop()
    app.run()
