import streamlit as st
import cv2
import numpy as np
from PIL import Image

# 1. Cấu hình giao diện Boutique
st.set_page_config(page_title="Tiệm Nơ Xinh AI", page_icon="🎀", layout="wide")

# CSS để làm đẹp giao diện (Boutique Style)
st.markdown("""
    <style>
    .main { background-color: #fffafb; }
    .stButton>button { background-color: #fb7185; color: white; border-radius: 20px; border: none; }
    .product-card { border: 1px solid #eee; padding: 20px; border-radius: 15px; background: white; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Điều hướng
menu = st.sidebar.selectbox("MENU CỬA HÀNG", ["🏠 Trang Chủ", "🛍️ Sản Phẩm", "🤖 AI Kiểm Kho"])

if menu == "🏠 Trang Chủ":
    st.title("🎀 Chào mừng đến với Tiệm Nơ Xinh")
    st.subheader("Nơi vẻ đẹp được chăm chút bằng công nghệ AI")
    st.image("http://googleusercontent.com/image_collection/image_retrieval/12933770790719936414", use_container_width=True)
    st.write("Chúng tôi tự hào mang đến những chiếc nơ thủ công tinh xảo nhất.")

elif menu == "🛍️ Sản Phẩm":
    st.header("✨ Bộ Sưu Tập Nổi Bật")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("http://googleusercontent.com/image_collection/image_retrieval/18034493506020806984", caption="Nơ Lụa Pastel - 45.000đ")
        if st.button("Thêm vào giỏ", key="b1"): st.balloons()
        
    with col2:
        st.image("http://googleusercontent.com/image_collection/image_retrieval/10342582903065759466", caption="Nơ Ren Cổ Điển - 55.000đ")
        if st.button("Thêm vào giỏ", key="b2"): st.balloons()

    with col3:
        st.image("http://googleusercontent.com/image_collection/image_retrieval/13208184143458702748", caption="Nơ Charm Kitty - 60.000đ")
        if st.button("Thêm vào giỏ", key="b3"): st.balloons()

elif menu == "🤖 AI Kiểm Kho":
    st.header("🤖 Trợ Lý AI Kiểm Kho Thông Minh")
    st.write("Tải ảnh chụp hàng tồn kho của bạn lên, AI sẽ đếm giúp bạn!")
    
    uploaded_file = st.file_uploader("Chọn ảnh kho hàng...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Chuyển ảnh sang OpenCV
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        
        # --- THUẬT TOÁN AI CỦA BẠN ---
        gray = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (7, 7), 0)
        _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Vẽ kết quả lên ảnh
        result_img = opencv_image.copy()
        count = 0
        for cnt in contours:
            if cv2.contourArea(cnt) > 500: # Lọc kích thước nơ
                cv2.drawContours(result_img, [cnt], -1, (0, 255, 0), 3)
                count += 1
        
        # Hiển thị kết quả
        c1, c2 = st.columns(2)
        with c1: st.image(opencv_image, caption="Ảnh gốc", channels="BGR")
        with c2: st.image(result_img, caption="AI đã nhận diện", channels="BGR")
        
        st.success(f"🎯 AI PHÁT HIỆN: {count} SẢN PHẨM TRONG KHO")  