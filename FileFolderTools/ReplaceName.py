import re
import os


class ReplaceName:
    """
        参数：
            data : [list]
                字符串数组。\n
                *如：["C:\\Windows","C:\\Program Files","C:\\Program Files (x86)"]
            old_name : [string]
                旧的内容\n
                *如："作者：xxx"\n
                *提示：支持正则表达式。
            new_name : [string]
                新的内容。\n
                *如：""

        根据用户传入的data数组，进行遍历将data数组中的值把旧的内容替换成新的内容，然后重命名文件。
    """

    def __init__(self, data, old_name, new_name):
        self._data = data
        self._oldName = old_name
        self._newName = new_name
        # 调用替换函数
        self.replace(data)
        pass

    def replace(self, data):
        for item in data:
            newPath = re.sub(rf"{self._oldName[::-1]}", self._newName[::-1], item[::-1], 1)[::-1]
            os.rename(item, newPath)
            print(f"\t替换成功：{item}")
