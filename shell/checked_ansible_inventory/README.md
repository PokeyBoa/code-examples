# 检测校准主机列表

功能：若 Ansible Inventory 列表中存在`UNREACHABLE`主机通讯不可达的条目, 将该行信息进行注释。


## 运行结果

```shell
[admin@localhost ~]$ chmod u+x ./check_hosts.sh

[admin@localhost ~]$ ./check_hosts.sh /etc/ansible/hosts
```
