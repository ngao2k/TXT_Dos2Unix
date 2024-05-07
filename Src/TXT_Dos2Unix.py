import os

# 定义待处理文件夹路径
unProcessFolderPath = "Input"

# 定义输出结果文件夹路径
ç = "Output"

# 定义待处理文件扩展名
fileExtension = ".txt"

"""
    构造指定文件夹下所有文件路径的数组
    @param folderPath 需要遍历的文件夹路径
    @return 返回包含所有符合条件文件路径的列表
"""
def DefineAllFilePaths(folderPath):
    paths = []
    for root, dirs, files in os.walk(folderPath):  # 遍历文件夹
        for file in files:  # 遍历文件
            # 检查文件扩展名是否为 .txt
            if file.endswith(fileExtension):
                # 构造完整的文件路径
                file_path = os.path.join(root, file)
                paths.append(file_path)
    return paths

"""
    处理单个文件
    @param filePath 需要处理的文件路径
    @param outputFolderPath 处理结果输出的文件夹路径
"""
def ProcessFile(filePath, outputFolderPath):
    # 读取文件内容
    with open(filePath, 'r', newline='\n') as file:
        content = file.read()

    # 替换不寻常的换行符为正常换行符
    content = content.replace('\r\n', '\n')

    # 获取文件名
    fileName = os.path.basename(filePath)

    # 确保输出目录存在
    os.makedirs(outputFolderPath, exist_ok=True)

    # 构造输出文件路径
    outputFilePath = os.path.join(outputFolderPath, fileName)

    # 写入处理后的内容到输出文件
    with open(outputFilePath, 'w') as file:
        file.write(content)

def main():
    # 获取待处理文件路径数组
    filePaths = DefineAllFilePaths(unProcessFolderPath)

    # 遍历文件路径数组，处理每个文件
    for filePath in filePaths:
        ProcessFile(filePath, outputFolderPath)

if __name__ == '__main__':
    main()