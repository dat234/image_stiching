import cv2
import matplotlib.pyplot as plt

# Load ảnh cần ghép
img1 = cv2.imread("D:\\download\\cd6ee5eb-0dc5-4cdc-bd32-8921cb3c2358.jpg")
img2 = cv2.imread("D:\\download\\9d3cf877-86c0-48a4-adfd-7abd63999647.jpg")

# Dùng thư viện Stitcher của OpenCV (tự động phát hiện, ghép, blend)
stitcher = cv2.Stitcher_create()
status, stitched = stitcher.stitch([img1, img2])

# Kiểm tra kết quả
if status == cv2.Stitcher_OK:
    print("✅ Ghép ảnh thành công!")
    # Hiển thị kết quả
    plt.imshow(cv2.cvtColor(stitched, cv2.COLOR_BGR2RGB))
    plt.title("Stitched Panorama")
    plt.axis("off")
    plt.show()
else:
    print("❌ Lỗi ghép ảnh. Mã lỗi:", status)
