#!/usr/bin/env bash
#written on xx/xx

set -o nounset
export LANG=en_US.UTF-8
stty erase '^h'
trap 'echo -e "  \nExit...\n"' EXIT
datesuf=`date +%Y%m%d`
symbols=`perl -e "print '#' x 50;"`
curdir=`dirname $(readlink -f $0)`
basedir=`dirname $curdir`"/"


echo -e "${symbols}\n"
echo "当前脚本路径: ${curdir}"
echo "父级目录: ${basedir}"


# EOF
