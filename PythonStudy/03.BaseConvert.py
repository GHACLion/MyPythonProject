# Author：程序员良哥
# DateTime: 2023/3/1 19:24

# chr代表 字符型 ，开头的 0b 代表后边是 二进制数，在ASCII码表中，二进制的 100111001011000 代表汉字 “乘”
print(chr(0b100111001011000))
# 反向处理，把汉字 “乘” 转化为ASCII码值，输出值为 20056，是十进制表示的 ASCII码值
print(ord('乘'))