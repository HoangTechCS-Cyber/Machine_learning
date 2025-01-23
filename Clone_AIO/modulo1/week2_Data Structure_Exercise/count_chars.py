# Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái và value là số lần xuất hiện
# Input: một từ
# Output: dictionary đếm số lần các chữ xuất hiện
# Note: Giả sử các từ nhập vào đều có các chữ cái thuộc [a-z] hoặc [A-Z]

def count_chars(string):
    chars_dic = {}
    for chars in string:
        if chars in chars_dic:
            chars_dic[chars] +=1
        else:
            chars_dic[chars] = 1
    return chars_dic
string = input('string =')
print(count_chars(string))