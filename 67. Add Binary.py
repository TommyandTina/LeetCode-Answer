class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_int = int(a, 2)
        b_int = int(b, 2)
        return bin(a_int + b_int)[2:]

"""
Trong Python, `[2:]` là một cách để **cắt chuỗi**. Cụ thể, `bin(a_int + b_int)[2:]` sẽ trả về một chuỗi mới bắt đầu từ vị trí thứ 3 (đếm từ 0) của chuỗi ban đầu và kéo dài đến cuối chuỗi.

Hàm `bin()` trong Python chuyển đổi một số nguyên thành chuỗi nhị phân, nhưng chuỗi này bắt đầu bằng `'0b'` để chỉ ra rằng đó là một chuỗi nhị phân. Vì vậy, `[2:]` được sử dụng để loại bỏ hai ký tự đầu tiên (`'0b'`) và chỉ lấy phần nhị phân thực sự của chuỗi.

Ví dụ, nếu `a_int + b_int` là 3, thì `bin(a_int + b_int)` sẽ trả về chuỗi `'0b11'`. Khi bạn áp dụng `[2:]`, bạn sẽ chỉ lấy phần `'11'`, đó là phần nhị phân của số 3. 

Vì vậy, `bin(a_int + b_int)[2:]` trả về chuỗi nhị phân của tổng `a_int` và `b_int` mà không có phần tiền tố `'0b'`.
"""