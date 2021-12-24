#!/bin/bash 
echo "helloword"
echo $1 $2 $3 
echo "文件名 "$0
echo "参数变量 "$#
echo "all "$*
echo "return "$?
a=10
b=20
echo `expr $a + $b `
echo `expr $a - $b `
echo `expr $a \* $b `
echo `expr $a / $b `
echo `expr $a % $b `

if [ $a == $b ]
then
echo "equl"
else
echo "not equl"
fi
ps aux | awk '{print }' | grep /Applications/
