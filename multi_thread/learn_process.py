import multiprocessing


def process(index):
    print(f'Process:{index}')


if __name__ == '__main__':
    for i in range(5):
        # 注意这里 args必须是一个元组，如果只有一个参数，那也要在元组第一个元素后面加上一个逗号，如果没有逗号则和单个元素本身没有区别，无法构成元组。导致参数传递出现问题。
        p = multiprocessing.Process(target=process,args=[i,])
        p.start()