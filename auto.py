# import time
#
# start_time = time.time()
# print(10)
# num = 10
# sentinel = 1
# while True:
#     if time.time() - start_time == sentinel:
#         if num - sentinel == 0:
#             print('bomb')
#             break
#         print(num - sentinel)
#         sentinel += 1
#
# from urllib.parse import quote
# from urllib.parse import urlencode
#
# base_url = 'https://s.taobao.com/search?'
# data = {
#     'q': '我爱我家'
# }
# if __name__ == '__main__':
#
#     # print('https://s.taobao.com/search?q='+quote('ipad'))
#     # print(base_url+urlencode(data))
#     print('q=' + quote('我爱我家'))
#     print(urlencode(data))
#
# """
# quote 和 urlencode 的区别 urlencode 需要用字典
# 单个字符就用quote就行了，因为quote只需要字符串就行了
# https://s.taobao.com/search?ipad
# https://s.taobao.com/search?q=ipad
# """
import os
print(type(os.environ))
import eigen_config