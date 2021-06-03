# 文件介绍
## __main__功能启动文件
+ 说明：
  + 该文件是用于启动当前目录下的功能。
+ 使用：
```bash
python __main__.py --help
Usage: 使用:__main__.py -s <操作模式> -p <目标路径>

Options:
  -h, --help            show this help message and exit
  -t TYPE, --type=TYPE  *目标路径操作模式。s=搜索，r=替换
  -p PATH, --path=PATH  *目标路径
  -s SEARCH, --search=SEARCH
                        搜索内容。提示：支持正则表达式。
  -r REPLACE, --replace=REPLACE
                        要替换的文件名。格式：旧名称-新名称。提示：支持正则表达式。
 ```

## SearchFilesAndFolders文件和文件夹搜索
+ 说明：
  + 根据用户传入的目录进行搜索，再根据用户传入的内容进行筛选。
+ 使用：
    + 可以在__main__传参方式使用。
    + 按照__main__文件中的方式调用SearchFilesAndFolders文件。
    
## ReplaceName替换文件和文件夹名称
+ 说明：
  + 根据用户传入的数组，进行遍历将数组中的值把旧的内容替换成新的内容。
+ 使用：
    + 可以在__main__传参方式使用。
    + 按照__main__文件中的方式调用ReplaceName文件。