# TXT_Dos2Unix
一个很简单的小工具，用来处理txt（或其他），将dos格式的换行符转换为unix格式。<br>解决在使用TXT文件时出现 `^M` 换行符导致的问题。
## 使用方法
* 进入Src目录
    - 打开 `TXT_Dos2Unix.py`
* 【可选】修改变量 `fileExtension`
    - 默认为 `.txt` ，可根据具体的文件需要进行修改
    - 修改内容应为 `字符串` 形式的文件扩展名（后缀），务必添加分隔符`.`
* 【可选】修改变量 `unProcessFolderPath `
    - 默认为 `Input` 文件夹
    - 修改内容应为 `字符串 String` 形式的待处理文件所在文件夹（目录）
* 【可选】修改变量`unProcessFolderPath `
    - 默认为 `Output` 文件夹
    - 修改内容应为 `字符串 String` 形式的输出文件所在文件夹（目录）
* 修改完成后务必保存

* 运行 `TXT_Dos2Unix.py` 
