# Tổ chức quy hoạch mạng viễn thông

Học kì 20182

Đại học Bách khoa Hà Nội

Giảng viên: TS. Trần Thị Ngọc Lan

Nhóm sinh viên:

Nguyễn Xuân Lưu 20152346

Nguyễn Phương Nam 20152577

Bùi Thị Ngọc Ánh 20150211


## Đề Tài: 
Đề 1: Cho mạng gồm 100 nút. Khoảng cách giữa các nút được tính bằng khoảng cách đề các. Biết các nút được đặt một cách ngẫu nhiên trên mặt phẳng kích thước 1200x1200.
1. Sử dụng giải thuật MENTOR để tìm nút backbone và các nút truy nhập tương ứng với nút Backbone. Biết W=2, R=0,35. dung lượng liên kết C=12. Biết lưu lượng giữa nút i và i+3 là 1, Lưu lượng giữa nút i và i+4 là 3. Lưu lượng giữa nút i và i +6 bằng 2, Lưu lượng giữa nút 10 và nút 34 là 10. Lưu lượng giữa nút 35 và 67 là 14, lưu lượng giữa nút 48 và 70 là 14, lưu lượng giữa nút 18 và 76 là 10,
lưu lượng giữa nút 25 và 73 là 14

2. Sử dụng giải thuật E-W để tính cây truy nhập. Với giả sử rằng W=8, W8xi =2 với i=1..10 còn w khác =1. Đưa kết quả ra màn hình.

3. Hiệu chỉnh kết quả cho trường hợp giới hạn số nút trên cây truy nhập là 5

## Môi trường phát triển

Ngôn ngữ chương trình Python 3

IDE sử dụng: PyCharm 3.1

Ngày hoàn thành 7, tháng 5, 2019

##Hướng dẫn sử dụng

## Chỉnh sửa thông số hệ thống.

### Chỉnh sửa các tham số thực hiện tại file Main.py

```
MAX = 1200 # MAX là thông số độ dài cạnh của mặt phẳng hình vuông kích thước MAX*MAX, nơi các nút được đặt lên.
NumNode = 100 # Số lượng nút trong mạng
RadiusRatio = 0.35 # Tỉ lệ dùng để tính bán kính quét mạng truy nhập của thuật toán MENTOR
C = 12 # Dung lượng 1 liên kết
w = 2  # Trọng số lưu lượng chuẩn hóa dùng để xét nút backbone của thuật toán MENTOR
w_ew = 8 # Trọng số ngưỡng của các nhóm trong cây truy nhập của thuật toán Esau Williams


ListPosition = InitialTopo.Global_Init_Topo_Fix_Position(MAX,NumNode,False)
# False/ True: Nếu chọn True, toàn bộ các bước trong tạo topology mạng sẽ được giám sát và hiển thị
# Nếu muốn các nút tạo ra ở vị trí ngẫu nhiên, tiến hành đỗi hàm Global_Init_Topo_Fix_Position thành hàm Global_Init_Topo, giữ nguyên tham số

ListMentor = MENTOR.MenTor(ListPosition,MAX,C,w,RadiusRatio,5,False)
# 5: Là số giới hạn nút đầu cuối của thuật toán MENTOR. Khi một nút Backbone tìm thấy số lượng nút đầu cuối đạt tới giới hạn. Nó ngừng việc quét tìm nút đầu cuối. Nếu cài đặt giá trị này bằng 0 thì xem như không có giới hạn số lượng nút đầu cuối.
# False/ True: Bật tắt giám sát thuật toán

ListFinish = EsauWilliam.Esau_William(ListMentor,w_ew,MAX,False)
# False/ True: Bật tắt giám sát thuật toán
```

### Chỉnh sửa dung lượng liên kết thực hiện tại file InitialTopo.py
```
###


###    Cấu hình mạng


###
    
    #Cài đặt để các nút thứ i và i+3 có dung lượng liên kết bằng 1, giữa i và i+4 bằng 3, giữa i và i+6 bằng 2
    
    for i in range(NumNode):
        if i + 3 < NumNode:
            set_traffic0(i, i + 3, 1)
        if i + 4 < NumNode:
            set_traffic0(i, i + 4, 3)
        if i + 6 < NumNode:
            set_traffic0(i, i + 6, 2)
    
    #Cài đặt để liên kết (10,34) dung lượng bằng 10; (35,67) bằng 14; (48,70) bằng 14; (18,76) bằng 10; (25,73) bằng 14
    set_traffic(10, 34, 10)
    set_traffic(35, 67, 14)
    set_traffic(48, 70, 14)
    set_traffic(18, 76, 10)
    set_traffic(25, 73, 14)

###

###    Kết Thúc Cấu hình mạng

###

```

