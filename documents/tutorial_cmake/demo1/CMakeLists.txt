# Cmake 最低的版本号要求
cmake_minimum_required(VERSION 2.8)

# 项目信息
project(Demo1)
# 参数表示该项目的名称是Demo1

# 生成指定目标
add_executable(Demo main.cc)
# 将main.cc的源文件编译成一个名称为Demo的可执行文件
