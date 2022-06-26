#!/bin/bash

# Command line parameter processing
help_info="
Usage: sh ${0} [OPTION]...
The iDRAC management remote initialization tool of the Dell Server.

Mandatory arguments to short options.
  -i                with an ipv4 address.
  -h                display this help and exit.

For example:
  $ sh ${0} -i 192.168.1.100
"
err_info="Try '${0} -h' for more information."

if [[ ${#} -eq 0 ]]; then
    echo -e "${err_info}\n"
    exit 99
fi

while getopts 'i:h' args
do
    case $args in
        i)
            ip=${OPTARG}
        ;;
        h)
            echo "${help_info}"
            exit 0
        ;;
        *)
            echo -e "${err_info}\n"
            exit 99
    esac
done

#EOF
