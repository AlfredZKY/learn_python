from pathlib import Path

def main():
    # 设置当前路径
    p = Path('.')
    print(p)

    # 列出当前路径中的文件夹
    l_list = [x for x in p.iterdir() if x.is_dir()]
    print(l_list)

    print("---------------------------------")
    # 列出当前路径所有文件夹下的.py文件
    print(list(p.glob('**/*.py')))



if __name__ == '__main__':
    main()
        