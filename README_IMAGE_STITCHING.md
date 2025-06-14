
# 🧵 Image Stitching (Ghép ảnh toàn cảnh)

## 📌 Giới thiệu
Image Stitching là quá trình kết hợp nhiều ảnh có vùng chồng lặp để tạo thành một ảnh toàn cảnh duy nhất (panorama). Các ảnh này thường được chụp từ cùng một điểm với góc nhìn khác nhau.

---

## ⚙️ Quy trình các bước chính

### 🔹 Bước 1–2: Phát hiện & mô tả đặc trưng
- Dùng thuật toán như **SIFT** để phát hiện các keypoints.
- Mỗi keypoint được mô tả bằng descriptor (vector đặc trưng 128 chiều).

---

### 🔹 Bước 3: Feature Matching (So khớp đặc trưng)
- So khớp descriptor giữa 2 ảnh bằng khoảng cách Euclidean.
- Áp dụng **Lowe’s Ratio Test**:
  ```
  Giữ match nếu: D1 < 0.75 × D2
  ```
  - D1: khoảng cách đến match gần nhất
  - D2: khoảng cách đến match gần nhì

✅ Kết quả: Danh sách các cặp keypoints tương ứng giữa 2 ảnh.

---

### 🔹 Bước 4: Estimate Homography (Tính ma trận biến đổi)
- Tính ma trận Homography 3x3 để ánh xạ điểm từ ảnh 2 về ảnh 1:
  ```
  [x', y', 1]^T ≈ H × [x, y, 1]^T
  ```
- Dùng **RANSAC** để loại bỏ outliers (match sai).
- Cần ít nhất 4 cặp điểm để tính H.

---

### 🔹 Bước 5: Warp Image
- Áp dụng H để biến đổi ảnh 2 về hệ tọa độ của ảnh 1 bằng `cv2.warpPerspective`.
- Đảm bảo các điểm khớp nằm đúng vị trí.

---

### 🔹 Bước 6: Blend & Stitch
- Dán ảnh 1 và ảnh 2 đã warp vào cùng một canvas.
- Sử dụng blend như:
  - **Feather blending** (alpha mờ dần)
  - **Multi-band blending** (nâng cao)
- Mục tiêu: vùng chồng phải mượt, không rõ đường nối.

📌 Ví dụ:
Nếu ảnh chồng nhau 100px:
- Biên trái: ảnh 1 chiếm ưu thế
- Biên phải: ảnh 2 chiếm ưu thế
- Giữa là vùng hòa trộn

---

## 🧪 Kết quả kỳ vọng
- Ảnh panorama hoàn chỉnh, tự nhiên
- Không bị rách hình, bóng mờ hay lệch cấu trúc

---

## 📦 Ứng dụng thực tế
- Ghép ảnh điện thoại
- Dựng bản đồ địa lý (GIS)
- Ảnh toàn cảnh trong robot, VR, surveillance

