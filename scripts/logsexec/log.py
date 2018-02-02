#!/opt/python/bin/python3
import IP,os
cnt = 11
f = open('/tmp/ip.txt','w+')
ipstr = os.popen("cat access.log |awk '{print $1,$7}' |sort |uniq -c |sort -rn |head -10")
f.write(ipstr.read())
f.close()
f1 = open('/tmp/ip.txt')
f2 = open('/tmp/nginx_ip.txt','w+')
for i in range(1,cnt):
    d = f1.readline()
    print("访问次数: %-4s  访问IP: %-18s  IP地址来源: %-4s   \t URL:%s" % (d.split()[0],d.split()[1],IP.find(d.split()[1]),d.split()[2]),file=f2)
f1.close()
f2.close()

