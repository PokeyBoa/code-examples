# 用户 TUI 交互界面

重点介绍 Shell Script 中 `read` 与 `while true loops + case statements` 的结合使用，能够构建用户交互场景的 TUI 菜单选项卡

- 运行结果:
```shell
[admin@localhost ~]$ sh demo.sh
##################################################
Please enter ipaddr: 192.168.0.100
Please enter netmask: 255.255.255.0
Please enter gateway: 192.168.0.1

##################################################

[y] Confirm to continue | [n] Re-enter | [q] Quit
y

Result:
  ip: 192.168.0.100
  netmask: 255.255.255.0
  gateway: 192.168.0.1
```