#!/bin/bash
#===============================================================================
#
#          FILE:  test.sh
# 
#         USAGE:  ./test.sh 
# 
#   DESCRIPTION:  just for testing
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  ---
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:  kang, yikai.kang@tum.de
#       COMPANY:  TUM
#       VERSION:  1.0
#       CREATED:  09/04/2020 11:39:26 AM CEST
#      REVISION:  ---
#===============================================================================

a=`pwd`/test.sh
[ -f a ]
echo $?
echo ${a}
