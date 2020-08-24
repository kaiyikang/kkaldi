- 有关Makefile 
https://zhuanlan.zhihu.com/p/47390641

- makefile 中的 = 和 :=
= 是最基本的赋值
:= 是覆盖之前的值

例如：
“:=”表示变量的值决定于它在makefile中的位置，而不是整个makefile展开后的最终值。

x := foo
y := $(x) bar
x := xyz
在上例中，y的值将会是 foo bar ，而不是 xyz bar 了。
