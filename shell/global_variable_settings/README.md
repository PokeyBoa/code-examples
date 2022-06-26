# 全局变量环境定义

列出 bash 脚本中 global variable 常见的全局定义
| 命令 | 说明 |
| --- | --- |
| `set -u` 或 `set -o nounset` | 引用了未定义的变量会报错 |
| `export LANG=en_US.UTF-8` | 设定语序环境 |
| `stty erase '^h'` | 退格键操作 |
| `trap 'echo -e "  \nExit...\n"' EXIT` | SIGINT信号捕获 |
| ``datesuf=`date +%Y%m%d` `` | 日期后缀，常用作日志备份文件命名 |
| `` symbols=`perl -e "print '#' x 50;"` `` | 打印输出的分割线 |
| ``curdir=`dirname $(readlink -f $0)` `` | 脚本所在的当前路径，与执行路径无关 |
| ``basedir=`dirname $curdir`"/" `` | 脚本所在的父级目录 |

