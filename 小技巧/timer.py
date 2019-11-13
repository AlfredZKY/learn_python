import schedule
import time

def job():
    print("I'm working")

def set_time_work():
    schedule.every(10).minutes.do(job)

    # 每分钟的第十七秒执行一次任务
    # schedule.every().minute.at(":17").do(job)

    # 每天的固定时间段执行一次任务
    schedule.every().day.at("17:11").do(job)
    
    # 每小时执行一次任务
    schedule.every().hour.do(job)

    # 每周一执行一次任务
    schedule.every().monday.do(job)

    # 每周二固定的时间段执行一次任务
    schedule.every().wednesday.at("17:16").do(job)

    schedule.every().thursday.at("13:15").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    set_time_work()