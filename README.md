# Bài tập lớn môn Xử lý ngôn ngữ tự nhiên
## 1. Giới thiệu
Bài tập về phát triển hỏi đáp trên cơ sở dữ liệu về thời gian, địa điểm đi về giữa các chuyến xe.
## 2. Các thành phần trong project
Phân cấp của project như sau:
    |- main.py
    |- models/   
                |- utils.py
                |- dictionary.py
    |- input/    
                |- database.txt
                |- input.txt
    |- output/
                |- output_a.txt
                |- output_b.txt
                |- output_c.txt
                |- output_d.txt
trong đó main.py là entrypoint thực thi chương trình; models chứa các model, function cần thiết, dictionary cần thiết; input chưa database và input cho chương trình; output chứa các file kết quả của chương trình.

## 3. Cách chạy
Các câu input vào dược thêm vào input/input.txt.
Chương trình sẽ thực thi và trả lời tất cả câu hỏi trong file input. Kết quả in ra trong các file output là sentences - kết quả.
Ví dụ
```
                                             Sentences                                              
xe bus nào đi từ đà nẵng đến thành phố hồ chí minh ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~result~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{'B1', 'B2'}
####################################################################################################
                                             Sentences                                              
Xe bus nào đến lúc 20:00hr ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~result~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{'B3'}
####################################################################################################
```
    
Chưng trình chạy trên nền python 3.5.6:
Cách thực thi chương trình:
`python3 main.py`
                