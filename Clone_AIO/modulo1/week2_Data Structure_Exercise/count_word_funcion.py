# Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
# với key là từ và value là số lần từ đó xuất hiện.
# Input: Đường dẫn đến file txt
# Output: dictionary đếm số lần các từ xuất hiện
# Note: Giả sử các từ trong file txt đều có các chữ cái thuộc [a-z] hoặc [A-Z]
# Không cần các thao tác xử lý string phức tạp nhưng cần xử lý các từ đều là viết thường

file_path = 'D:\Machine-Learning\Clone_AIO\modulo1\week2_Data Structure_Exercise\P1_data.txt'

def count_words(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
        words = data.split()
        words_dic = {}
    for word in words:
        if word in words_dic:
            words_dic[word] += 1
        else:
            words_dic[word] = 1
    return words_dic
print(count_words(file_path))