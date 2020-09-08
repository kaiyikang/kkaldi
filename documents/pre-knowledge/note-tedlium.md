time: 2020-sep-04

## path.sh

~~~bash
[ "a"=="a" ]
echo $?
~~~

$? 获取上一个状态码


~~~bash
export KALDI=`pwd`/../../.._
[ -f $KALDI_ROOT/tools/env.sh ]
~~~
判断一个文件是否存在
