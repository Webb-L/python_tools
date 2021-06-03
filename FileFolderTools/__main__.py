from optparse import OptionParser
import os

from FileFolderTools.ReplaceName import ReplaceName
from FileFolderTools.SearchFilesAndFolders import SearchFilesAndFolders

if __name__ == '__main__':
    parser = OptionParser("使用:%prog -s <操作模式> -p <目标路径>")
    parser.add_option("-t", "--type", type="string", dest="TYPE", help="*目标路径操作模式。s=搜索，r=替换")
    parser.add_option("-p", "--path", type="string", dest="PATH", help="*目标路径")
    parser.add_option("-s", "--search", type="string", dest="SEARCH", help="搜索内容。提示：支持正则表达式。")
    parser.add_option("-r", "--replace", type="string", dest="REPLACE", help="要替换的文件名。格式：旧名称-新名称。提示：支持正则表达式。")
    options, args = parser.parse_args()
    '''
        判断用户参数是否传入正确。
    '''
    # 判断路径和类型参数是否传入值
    if not options.PATH or not options.TYPE:
        parser.print_help()
        exit()
        pass

    if not os.path.exists(options.PATH):
        print("文件路径错误！")
        exit()
        pass

    # 判断用户传入类型是否等于s
    if options.TYPE == 's':
        print("开始查找")
        dirs = SearchFilesAndFolders(options.PATH, options.SEARCH)
        print(f" 一共查找到有{len(dirs.searchResult)}条。\n  文件夹：{len(dirs.folders)}\n  文件：{len(dirs.files)}")
        for dir in dirs.searchResult:
            print(f"\t   {dir}")
        print("结束查找")
        exit()
        pass

    # 判断用户传入类型是否等于r
    if options.TYPE == 'r':
        print("开始替换")
        replace = options.REPLACE.split("-")
        dirs = SearchFilesAndFolders(options.PATH, replace[0])
        if len(dirs.searchResult) > 0:
            dirs.searchResult.reverse()
            ReplaceName(dirs.searchResult, replace[0], replace[1])
        else:
            print("\t找不到数据")
        print("结束替换")
        exit()
        pass

    # 用户传入类型错误
    if options.TYPE:
        parser.print_help()
        exit()
        pass
