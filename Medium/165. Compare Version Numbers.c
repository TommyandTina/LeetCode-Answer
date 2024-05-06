#include <stdio.h>
#include <stdlib.h>

int compareVersion(char * version1, char * version2){
    while(*version1 || *version2) {
        int v1 = 0;
        int v2 = 0;
        while(*version1 && *version1 != '.') {
            v1 = v1 * 10 + (*version1 - '0');
            version1++;
        }
        while(*version2 && *version2 != '.') {
            v2 = v2 * 10 + (*version2 - '0');
            version2++;
        }
        if(v1 > v2) return 1;
        if(v1 < v2) return -1;
        if(*version1) version1++;
        if(*version2) version2++;
    }
    return 0;
}

int main() {
    char version1[] = "1.01";
    char version2[] = "1.001";
    printf("Output: %d\n", compareVersion(version1, version2));
    return 0;
}

/*
Dưới đây là một ví dụ về cách mã của bạn hoạt động khi so sánh hai chuỗi phiên bản "1.01" và "1.001":

1. Khi bạn gọi hàm `compareVersion(version1, version2)`, nó bắt đầu vòng lặp `while(*version1 || *version2)`.

2. Trong mỗi lần lặp, nó khởi tạo hai biến `v1` và `v2` là 0. 

3. Sau đó, nó vào vòng lặp `while(*version1 && *version1 != '.')` để xử lý chuỗi `version1`. Nó sẽ chuyển đổi từng ký tự số thành số nguyên và thêm vào `v1` cho đến khi gặp ký tự '.' hoặc kết thúc chuỗi. Trong trường hợp này, `v1` sẽ trở thành 1 sau khi xử lý ký tự đầu tiên của `version1`.

4. Tương tự, nó vào vòng lặp `while(*version2 && *version2 != '.')` để xử lý chuỗi `version2`. `v2` cũng sẽ trở thành 1 sau khi xử lý ký tự đầu tiên của `version2`.

5. Sau đó, nó so sánh `v1` và `v2`. Nếu `v1` lớn hơn `v2`, nó trả về 1. Nếu `v1` nhỏ hơn `v2`, nó trả về -1. Trong trường hợp này, `v1` và `v2` đều bằng 1, nên nó không trả về gì cả.

6. Tiếp theo, nó kiểm tra xem `version1` và `version2` có phải là ký tự '.' hay không. Nếu có, nó tăng con trỏ `version1` và `version2` lên 1 để bỏ qua ký tự '.'.

7. Vòng lặp `while(*version1 || *version2)` tiếp tục cho đến khi cả hai chuỗi `version1` và `version2` đều được xử lý hết.

8. Cuối cùng, nếu cả hai chuỗi `version1` và `version2` đều được xử lý hết mà không có sự khác biệt nào được tìm thấy, hàm `compareVersion` sẽ trả về 0.

Với chuỗi `version1` là "1.01" và `version2` là "1.001", hàm `compareVersion` sẽ trả về 0, vì cả hai chuỗi này đều biểu diễn cho số 1.01 khi bỏ qua các số 0 dẫn đầu. Kết quả này được in ra bởi hàm `main`.
*/