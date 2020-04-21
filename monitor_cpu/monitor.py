#psutil 模块 用于监控：
#安装 pip install psutil
import psutil

#监控cpu信息：
def cpu ():
#	cpu = psutil.cpu_count(False) cpu核数 默认逻辑cpu核数，False查看真实cpu核数；
	cpu_per = int(psutil.cpu_percent(1)) #每秒cpu使用率，（1，True） 每一核cpu的每秒使用率；
#	print(cpu_per)
	return cpu_per
#监控内存信息：
def mem ():
#	mem = psutil.virtual_memory()   查看内存信息；
	mem_total = int(psutil.virtual_memory()[0]/1024/1024)
	mem_used = int(psutil.virtual_memory()[3] / 1024 / 1024)
	mem_per = int(psutil.virtual_memory()[2])
	mem_info = {
		'mem_total' : mem_total,
		'mem_used' : mem_used,
		'mem_per' : mem_per
	}
	return mem_info
#监控硬盘使用率：
def disk ():
	c_per = int(psutil.disk_usage('C:')[3]) #查看c盘的使用信息：总空间，已用，剩余，占用比；
	d_per = int(psutil.disk_usage('d:')[3])
	e_per = int(psutil.disk_usage('e:')[3])
	f_per = int(psutil.disk_usage('f:')[3])
	# print(c_per,d_per,e_per,f_per)
	disk_info = {
		'c_per' : c_per,
		'd_per' : d_per,
		'e_per' : e_per,
		'f_per' : f_per
	}
	return disk_info
#监控网络流量：
def network ():
#	network = psutil.net_io_counters() #查看网络流量的信息；
	network_sent = int(psutil.net_io_counters()[0]/8/1024)  #每秒接受的kb
	network_recv = int(psutil.net_io_counters()[1]/8/1024)
	network_info = {
		'network_sent' : network_sent,
		'network_recv' : network_recv
	}
	return network_info
#发邮件：

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.header import Header

def send_email (info):
	sender = '912111980@qq.com'
	receiver = '912111980@qq.com'
	subject = '报警'
	username = '912111980@qq.com'
	password = 'ZKY19920218'
	msg = MIMEText(info, 'plain', 'utf-8')
	msg['Subject'] = Header(subject, 'utf-8')
	msg['From'] = sender
	msg['To'] = receiver
	smtp = smtplib.SMTP()
	smtp.connect('smtp.qq.com')
	smtp.login(username, password)
	smtp.sendmail(sender, receiver, msg.as_string())
	smtp.quit()

#主函数，调用其他函数；
def main ():
	cpu_info = cpu()
	mem_info = mem()
	disk_info = disk()
	network_info = network()
	info = '''
				监控信息
		=========================
		cpu使用率： : %s,
		=========================
		内存总大小（MB） : %s,
		内存使用大小（MB） : %s,
		内存使用率 : %s,
		=========================
		C盘使用率: %s,
		D盘使用率: %s,
		E盘使用率: %s,
		F盘使用率: %s,
		=========================
		网络流量接收的量（MB） : %s,
		网络流量发送的量（MB）: %s
	''' % (cpu_info, mem_info['mem_total'],mem_info['mem_used'],mem_info['mem_per'],disk_info['c_per'],disk_info['d_per'],disk_info['e_per'],disk_info['f_per'],network_info['network_sent'],network_info['network_recv'])
	send_email(info)
	print(info)

if __name__ == '__main__':
    main()
