# -*- coding: utf-8 -*-
def big_camel_to_underline(big_camel_string):
        """大驼峰命名转下划线命名"""
        string_list = []
        for i, char in enumerate(big_camel_string):
            if char.isupper():
                if i != 0 and big_camel_string[i - 1].islower():
                    string_list.append('_' + char.lower())
                    continue
                if i != len(big_camel_string) - 2 \
                        and big_camel_string[i + 1].isupper() \
                        and big_camel_string[i + 2].islower():
                    string_list.append(char.lower() + '_')
                    continue
                string_list.append(char.lower())
            else:
                string_list.append(char)
        return ''.join(string_list)

print(big_camel_to_underline('ABCD'))
    