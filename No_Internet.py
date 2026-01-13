import csv
import os

students = []
# --- CHỨC NĂNG 1: THÊM SINH VIÊN MỚI ---
def add_new_student():
    print("--- THÊM SINH VIÊN MỚI ---")
    while True:
        student_id = input("Nhập ID sinh viên (VD:2502xxxx): ").strip()
        if not student_id:
            print("Đang trở lại menu chính...")
            return
        
        # Kiểm tra ID trùng
        if any(student['id'].upper() == student_id.upper() for student in students):
            print(f"Lỗi: ID '{student_id}' đã tồn tại.")
            k = input("Thử lại (1) | Thoát ra menu (0): ")
            if k == '1':
                continue
            else:
                return
        break
    
    name = input("Nhập tên sinh viên: ").strip()
    
    # Nhập điểm
    while True:
        print("Nhập danh sách điểm (Cách nhau bởi dấu cách. VD: 8 9.5 10)")
        score_input=input("Nhập điểm (0-10): ").strip()
        score_input=score_input.replace(',',' ')
        score_part=score_input.split()
        score=[]
        error=False
        for i in score_part:
            try:
                s=float(i)
                if 0<=s<=10:
                    score.append(s)
                else:
                    print(f"Lỗi: Điểm '{s}' không nằm trong khoảng 0-10.")
                    error=True
                    break
            except ValueError:
                print(f"Lỗi: '{i}' không phải là số hợp lệ")
                error=True
                break
        if not error:
            if len(score)>0:
                break
            else:
                print("Lưu ý: Bạn chưa nhập điểm nào (Danh sách điểm trống).")
                k=input("Bạn có chắc chăn không? (c/k): ").lower()
                if k=='c':
                    break
    new_student = {
        'id': student_id,
        'name': name,
        'score': score  # QUAN TRỌNG: Lưu điểm dưới dạng LIST
    }
    students.append(new_student)
    print(f"\nĐã thêm sinh viên '{name}' (ID: {student_id}) thành công.")

# --- CHỨC NĂNG 2: TÌM KIẾM SINH VIÊN ---
def search_by_student_id():
    print("--- TÌM KIẾM SINH VIÊN THEO ID ---")
    search_id = input("Nhập ID sinh viên cần tìm: ").strip().upper()
    found = False
    
    for student in students:
        if student['id'].upper() == search_id:
            print("\n*HỒ SƠ SINH VIÊN ĐƯỢC TÌM THẤY*")
            print(f"ID:   {student['id']}")
            print(f"Tên:  {student['name']}")
            print(f"Điểm: {student['score']}") # In ra danh sách điểm
            found = True
            break
            
    if not found:
        print(f"Không tìm thấy sinh viên với ID '{search_id}'")
        k = input(f"Bạn có muốn thêm sinh viên ID '{search_id}' không? (1: CÓ | 0: KHÔNG): ")
        if k == '1':
            name = input("Nhập tên sinh viên: ").strip()
            try:
                score_input = float(input("Nhập điểm số: ").strip())
            except ValueError:
                print("Điểm không hợp lệ, lưu mặc định là 0.")
                score_input = 0.0
                
            new_student = {
                'id': search_id,
                'name': name,
                'score': [score_input] # Lưu dạng LIST
            }
            students.append(new_student)
            print(f"\nĐã thêm sinh viên '{name}' thành công.")
        else:
            print("Đang trở lại menu chính...")

# --- CHỨC NĂNG 3: HIỂN THỊ DANH SÁCH ---
def display_all_scores():
    print("\n--- DANH SÁCH TẤT CẢ SINH VIÊN ---")
    if not students:
        print("Danh sách hiện đang trống.")
        return
    
    # Sắp xếp theo tên
    sorted_students = sorted(students, key=lambda x: x['name'])
    #Tính toán khoảng cách chia bảng
    max_name_len=max((len(s['name'])for s in students), default=20)
    w_name=max(max_name_len,20)
    #In tiêu đề (:<12 là dành 12 khoảng trắng và căn lề trái)
    header=f"{'ID':<12}  {'HỌ VÀ TÊN':<{w_name}}  {'ĐIỂM TB':<10}  {'CHI TIẾT ĐIỂM'}"
    print(header)
    print("-"*len(header))
    #In dữ liệu
    for s in sorted_students:
        if s['score']:
            avg=sum(s['score'])/len(s['score'])
            avg_str=f"{avg:.2f}" 
            scores_str=", ".join(map(str,s['score']))
        else:
            avg_str="0.00"
            scores_str="(Chưa có điểm)"
    #In dòng dữ liệu
        print(f"{s['id']:<12}  {s['name']:<{w_name}}  {avg_str:10}  {scores_str}")

# --- CHỨC NĂNG 4: THÊM ĐIỂM ---
def add_score_to_student():
    print("--- THÊM ĐIỂM CHO SINH VIÊN ---")
    student_id = input("Nhập ID sinh viên: ").strip().upper()
    
    found = False
    for student in students:
        if student['id'].upper() == student_id:
            found = True
            try:
                new_score = float(input(f"Nhập điểm thêm cho {student['name']}: ").strip())
                if 0 <= new_score <= 10:
                    student['score'].append(new_score) # Hoạt động tốt vì score giờ là list
                    print("Đã cập nhật điểm thành công.")
                else:
                    print("Điểm không hợp lệ (0-10).")
            except ValueError:
                print("Lỗi: Vui lòng nhập số.")
            break
            
    if not found:
        print("Không tìm thấy ID sinh viên này.")

# --- MENU CHÍNH ---
def main_menu():
    while True:
        print("\n==================================")
        print("  QUẢN LÝ DỮ LIỆU LỚP HỌC (DEMO)")
        print("==================================")
        print("1. Thêm sinh viên mới")
        print("2. Tìm kiếm bằng ID sinh viên")
        print("3. Hiển thị danh sách kèm điểm số")
        print("4. Thêm điểm cho sinh viên")
        print("5. Thoát chương trình") 
        
        choice = input("Nhập lựa chọn của bạn (1-6): ").strip()
        
        if choice == '1':
            add_new_student()
        elif choice == '2':
            search_by_student_id()
        elif choice == '3':
            display_all_scores()
        elif choice == '4':
            add_score_to_student()
        elif choice == '5':
            print("==========")
            print("Tạm biệt")
            print("==========")
            break
        else:
            print("Lựa chọn không hợp lệ!")
main_menu()