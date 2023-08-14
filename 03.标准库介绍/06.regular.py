

# re模块
import re

result = re.match('itcast',"itca1st.com")
if result:
    print(result)
    info = result.group()
    print(info)

# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h","hello Python")
print(ret.group())

ret = re.match("[hH]ello Python","Hello Python")
print(ret.group())

