# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Sửa lỗi lấy sai index: Mã sản phẩm nằm ở vị trí đầu tiên (index 0)
product_code = product_info[0]

# Sửa lỗi lấy sai index: Tên sản phẩm nằm ở vị trí thứ hai (index 1)
product_name = product_info[1]

# Sửa lỗi cú pháp: Dùng hàm len() để đếm số lượng thông tin trong tuple
product_length = len(product_info)

# Sửa lỗi logic sửa đổi trực tiếp: Tạo tuple mới bằng cách gom dữ liệu cũ và giá mới
product_info_updated = (product_info[0], product_info[1], product_info[2], 279000)

# Hiển thị kết quả ra Console theo đúng định dạng yêu cầu của Yody
print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info_updated)