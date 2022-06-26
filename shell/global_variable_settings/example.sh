#!/usr/bin/env bash
#written on xx/xx

set -o nounset                                  # set -u 引用了未定义的变量会报错
export LANG=en_US.UTF-8                         # 设定语序环境
stty erase '^h'                                 # 退格键操作
trap 'echo -e "  \nExit...\n"' EXIT             # SIGINT信号捕获
datesuf=`date +%Y%m%d`                          # 日期后缀
symbols=`perl -e "print '#' x 50;"`             # 分割线
curdir=`dirname $(readlink -f $0)`
basedir=`dirname $curdir`"/"


echo -e "${symbols}\n"
echo "当前脚本路径: ${curdir}"
echo "父级目录: ${basedir}"


# EOF
