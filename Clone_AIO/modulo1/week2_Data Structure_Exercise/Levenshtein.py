# Viết chương trình tính khoảng cách chỉnh sửa tối thiểu Levenshtein. Khoảng cách Levenshtein thể
# hiện khoảng cách khác biệt giữa 2 chuỗi ký tự. Khoảng cách Levenshtein giữa chuỗi S và chuỗi T
# là số bước ít nhất biến chuỗi S thành chuỗi T thông qua 3 phép biến đổi là:
# Xoá một ký tự
# Thêm một ký tự
# Thay thế ký tự này bằng ký tự khác

def levenstein_distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    dp = [[0 for _ in range(len_str2 + 1)]
          for _ in range(len_str1 + 1)]  # tao ma tran 2D

    for i in range(len_str1 + 1):
        dp[i][0] = i  # khoi tao gia tri cho hang dau tien
    for j in range(len_str2 + 1):
        dp[0][j] = j  # khoi tao gia tri cho cot dau tien

    for i in range(1, len_str1 + 1):  # duyet theo hang
        for j in range(1, len_str2 + 1):  # duyet theo cot
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
    return dp[len_str1][len_str2]


print(levenstein_distance('kitten', 'sitting'))
print(levenstein_distance('sunday', 'saturday'))
print(levenstein_distance('yu','you'))
