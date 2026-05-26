# Hệ thống kiểm duyệt nội dung sản phẩm Shopee
# Author: Hoang - HNKS25CNTT1

def process_product_data():
    shop_name = input("Nhập tên shop: ").strip()
    if not shop_name:
        print("Tên shop không được bỏ trống")
        return

    product_name = input("Nhập tên sản phẩm: ").strip().title()
    description = input("Nhập mô tả sản phẩm: ").strip()
    if not description:
        print("Mô tả sản phẩm không được rỗng")
        return

    category = input("Nhập danh mục sản phẩm: ").strip().lower()
    keywords = input("Nhập danh sách từ khóa (cách nhau bởi dấu phẩy): ").strip()
    keyword_list = [kw.strip() for kw in keywords.split(",") if kw.strip()]

    print("\n--- Báo cáo thống kê ---")
    print("Tên shop:", shop_name)
    print("Tên sản phẩm:", product_name)
    print("Mô tả:", description)
    print("Độ dài mô tả:", len(description))
    print("Danh mục:", category)
    print("Danh sách từ khóa:", keyword_list)
    print("Số lượng từ khóa:", len(keyword_list))
    print("Mô tả chữ thường:", description.lower())
    print("Mô tả chữ hoa:", description.upper())


def normalize_shop_name():
    shop_name = input("Nhập tên shop: ").strip()
    if not shop_name:
        print("Tên shop không được bỏ trống")
        return
    normalized = shop_name.lower().replace(" ", "-")
    if not normalized.startswith("shop-"):
        normalized = "shop-" + normalized
    print("Tên shop chuẩn hóa:", normalized)


def validate_discount_code():
    code = input("Nhập mã giảm giá: ").strip()
    if not code:
        print("Mã giảm giá không được rỗng")
        return
    if " " in code:
        print("Mã giảm giá không được chứa khoảng trắng")
        return
    if not (6 <= len(code) <= 12):
        print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
        return
    if not code.isalnum():
        print("Mã giảm giá chỉ được chứa chữ cái và số")
        return
    if not code.isupper():
        print("Mã giảm giá phải viết hoa toàn bộ")
        return
    if not code.startswith("SALE"):
        print("Mã giảm giá phải bắt đầu bằng SALE")
        return
    print("Mã giảm giá hợp lệ")


def replace_keyword_in_description():
    description = input("Nhập mô tả sản phẩm: ").strip()
    if not description:
        print("Mô tả sản phẩm không được rỗng")
        return
    find_kw = input("Nhập từ khóa cần tìm: ").strip()
    replace_kw = input("Nhập từ khóa thay thế: ").strip()
    count = description.count(find_kw)
    if count == 0:
        print("Không tìm thấy từ khóa trong mô tả")
    else:
        new_description = description.replace(find_kw, replace_kw)
        print("Số lần xuất hiện:", count)
        print("Mô tả sau khi thay thế:", new_description)


def main():
    while True:
        print("\n--- MENU ---")
        print("1. Nhập dữ liệu sản phẩm và xem báo cáo")
        print("2. Chuẩn hóa tên Shop")
        print("3. Kiểm tra mã giảm giá hợp lệ")
        print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
        print("5. Thoát chương trình")

        choice = input("Chọn chức năng (1-5): ").strip()
        if not choice.isdigit():
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5")
            continue

        choice = int(choice)
        if choice == 1:
            process_product_data()
        elif choice == 2:
            normalize_shop_name()
        elif choice == 3:
            validate_discount_code()
        elif choice == 4:
            replace_keyword_in_description()
        elif choice == 5:
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")


if __name__ == "__main__":
    main()
