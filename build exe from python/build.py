import subprocess

def run_pyinstaller(input_path):
    # Xây dựng lệnh pyinstaller
    command = ["C:/Users/long.trinh-tien/AppData/Roaming/Python/Python39/Scripts/pyinstaller.exe", "--onefile", "-w", input_path]

    # Thực thi lệnh
    try:
        subprocess.run(command, check=True)
        print("Chạy pyinstaller thành công!")
    except subprocess.CalledProcessError as e:
        print(f"Lỗi: {e}")

def main():
    # Nhập đường dẫn của file từ người dùng
    input_path = input("Nhập đường dẫn của file: ")

    # Chạy pyinstaller với đường dẫn đã nhập
    run_pyinstaller(input_path)

if __name__ == "__main__":
    main()
