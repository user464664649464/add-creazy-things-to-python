import sys
import os


def transformer(code: str = None, fileObj: str = None) -> str:
    """Summary

    Args:
            fileObj (str): The file path or file object to be processed.

    Returns:
            str: The processed code string.
    """
# Read the file
    code: str = fileObj.read() if fileObj else (code if code else "")
# Split the code into lines
    lines: list = code.split('\n')
    # Iterate over the lines list
    trans: list[tuple] = []
    for line in lines:
        # The syntax is:
        """
        define <name> <value: any>
                         ^ Tip: <value> can be the keyword
                """
        split: list = line.split(' ')
        if split[0] == 'define':
            trans.append((split[1], split[2]))

    lines = [
        l for l in lines
        if l.split(" ")[0] != "define"
    ]
    code = '\n'.join(lines)
    for k, v in trans:
        code = code.replace(k, v)
    return code


if len(sys.argv) < 2:
    print(f"""
整活：我在python中添加了define
使用方法：
在文件中：
e.g. 1.py
define fro for
fro i in range(10):
        print(i)

        翻译：
        python main.py 1.py
    转换后：
{transformer(code="""
define fro for
fro i in range(10):
        print(i)
""")}
        运行：
        python main.py 1.py
        运行结果：""")
    exec(transformer(code="""
define fro for
fro i in range(10):
        print(i)
""")
         )
    path = input("请输入路径")
    with open(path, 'r', encoding="utf-8") as f:
        code = transformer(fileObj=f)
    with open(f"{path.split('.')[0]}_replaced.py", 'w', encoding='utf-8') as f:
        f.write(code)
    os.system(f"python {path.split('.')[0]}_replaced.py")
else:
    with open(sys.argv[1], 'r', encoding="utf-8") as f:
        code = transformer(fileObj=f)
    with open(f"{sys.argv[1].split('.')[0]}_replaced.py", 'w', encoding='utf-8') as f:
        f.write(code)
    os.system(f"python {sys.argv[1].split('.')[0]}_replaced.py")
