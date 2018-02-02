#用于日志统计，获取访问量较高的接、IP及IP归属地。
#使用模块：
#https://pypi.python.org/pypi/17MonIP
pip install 17monip
import IP,os
#使用方法：
./log.py
cat /tmp/nginx_ip.txt
#日志格式
'$remote_addr - $remote_user [$time_local] "$request" '
'$status $body_bytes_sent  $user_id $request_body  "$http_referer" '
'"$http_user_agent" $http_x_forwarded_for $http_cdn_src_ip $http_x_imsi $http_x_phoneModel  $http_x_mac $http_x_idfa $http_x_HWUserToken'

172.246.236.138 - - [30/Dec/2017:00:04:01 +0800] "GET /search.php?formhash=33575971&mod=forum&searchsubmit=true&source=hotsearch&srchtxt=%E6%B4%BB%E5%8A%A8 HTTP/1.1" 200 44  - http://www.baidu.com Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1) --HWUserToken request_time_0.014
#生成格式
访问次数: 688   访问IP: 10.64.162.37        IP地址来源: 局域网  局域网           URL: /
访问次数: 428   访问IP: 10.64.162.37        IP地址来源: 局域网  局域网           URL: /
访问次数: 428   访问IP: 10.64.162.37        IP地址来源: 局域网  局域网           URL: /
访问次数: 373   访问IP: 10.64.162.37        IP地址来源: 局域网  局域网           URL: /
访问次数: 314   访问IP: 10.64.162.37        IP地址来源: 局域网  局域网           URL: /
访问次数: 313   访问IP: 10.64.162.37        IP地址来源: 局域网  局域网           URL: /
访问次数: 312   访问IP: 10.64.162.37        IP地址来源: 局域网  局域网           URL: /
访问次数: 243   访问IP: 60.195.254.33       IP地址来源: 中国    北京    北京     URL: /
访问次数: 235   访问IP: 10.64.162.37        IP地址来源: 局域网  局域网           URL: /
访问次数: 182   访问IP: 60.195.254.33       IP地址来源: 中国    北京    北京     URL: /



