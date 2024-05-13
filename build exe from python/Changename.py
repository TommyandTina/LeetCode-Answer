import os

def rename_files_with_dash(current_directory):
    # Lấy đường dẫn của thư mục hiện tại
    # current_directory = 'C:/Users/long.trinh-tien/Documents/LeetCode'

    # Lặp qua tất cả các tệp trong thư mục hiện tại
    for filename in os.listdir(current_directory):
        if filename.endswith(".py"):
            # Kiểm tra xem tên tệp có chứa ký tự "-" không
            if "-" in filename:
                new_filename = filename.replace("-", " ")
                # Tạo đường dẫn mới cho tệp
                new_filepath = os.path.join(current_directory, new_filename)
                # Đổi tên tệp
                os.rename(os.path.join(current_directory, filename), new_filepath)
                print(f"Đã đổi tên tệp {filename} thành {new_filename}")
            
            # Chuyển tất cả các từ thành chữ hoa
            new_filename = filename.title()
            # Tách phần đuôi của tên file
            file_name, file_extension = os.path.splitext(new_filename)
            # Chuyển phần đuôi thành chữ thường
            new_file_extension = file_extension.lower()
            #Thêm khoảng trắng nếu có số ngay đầu: VD 210.Name.py -> 210. Name.py
            if "." in file_name and not ". " in file_name:
                file_name = file_name.replace(".", ". ")
            # Tạo tên mới cho tệp
            new_filename = f"{file_name}{new_file_extension}"
            # Tạo đường dẫn mới cho tệp
            new_filepath = os.path.join(current_directory, new_filename)
            # Đổi tên tệp
            os.rename(os.path.join(current_directory, filename), new_filepath)
            print(f"Đã đổi tên tệp {filename} thành {new_filename}")

# Gọi hàm để thực hiện thay đổi tên tệp
rename_files_with_dash('C:/Users/long.trinh-tien/Documents/LeetCode')
