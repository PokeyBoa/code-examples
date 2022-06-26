# 非交互自动化执行脚本

介绍 Shell Script 中利用 `expect` 工具进行非交互自动化脚本的作业，常被用于 `ssh/ftp` 等需要输入密码的任务中。


## 执行方式

+ 在 bash 中直接使用代码块
+ 构建独立的 expect 脚本


## 运行结果

```shell
[admin@localhost ~]$ chmod u+x ./demo.sh

[admin@localhost ~]$ ./demo.sh root 10.0.0.15 123456
spawn sftp -o port=22 root@10.0.0.15
Authorized uses only. All activity may be monitored and reported.
root@10.0.0.15's password: 
Connected to 10.0.0.15.
sftp> pwd
Remote working directory: /root
sftp> ls -l
-rwxr-xr-x    1 root     root     2018148352 Jun 22 11:52 Fedora-Live-x86_64-36-1.5.iso
-r-xr-xr-x    1 root     root      7235024 Jun  6 14:24 libpython2.6.so.1.0
sftp> put ./demo.sh
Uploading ./demo.sh to /root/demo.sh
./demo.sh                                                                                 100%  549     1.3MB/s   00:00    
sftp> bye
```

