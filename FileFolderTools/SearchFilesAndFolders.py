import re
import os


class SearchFilesAndFolders:
    """
        参数：
            path : [string]
                搜索目标路径。\n
                *如："C:/\test"
            name : [string]
                根据path参数提供的目录下的文件进行匹配，如果匹配成功将添加到searchResult中。\n
                *如："作者：xxx"\n
                *提示：支持正则表达式。

        根据用户传入的目录进行搜索，再根据用户传入的内容进行筛选。
    """

    def __init__(self, path, name):
        self._name = name
        self.files = []
        self.folders = []
        self.searchResult = []
        # 调用搜索函数
        self.search(path)

    '''
        根据用户传入的path变量进行递归查询符合要求的文件和文件夹
    '''

    def search(self, path):
        dirs = os.listdir(path)
        for dir in dirs:
            result = re.search(fr"{self._name}", dir)
            resultPath = f"{path}\\{dir}"
            if result:
                self.searchResult.append(resultPath)
                if os.path.isdir(resultPath):
                    self.folders.append(resultPath)
                else:
                    self.files.append(resultPath)

            if os.path.isdir(resultPath):
                self.search(resultPath)
