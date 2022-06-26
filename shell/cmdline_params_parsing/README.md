# 命令行参数解析

重点介绍 Shell Script 中 `getopts` 命令行参数解析工具的用法，以 IPv4 解析为脚本示例

- 运行结果:
```shell
[admin@localhost ~]$ chmod u+x ./ip-helper.sh

[admin@localhost ~]$ ./ip-helper.sh 

Try './ip-helper.sh -h' for more information.

[admin@localhost ~]$ ./ip-helper.sh -h

Usage: sh ./ip-helper.sh [OPTION]...
The iDRAC management remote initialization tool of the Dell Server.

Mandatory arguments to short options.
  -i                with an ipv4 address.
  -h                display this help and exit.

For example:
  $ sh ./ip-helper.sh -i 192.168.1.100

[admin@localhost ~]$ ./ip-helper.sh -i 10.0.0.1
```
