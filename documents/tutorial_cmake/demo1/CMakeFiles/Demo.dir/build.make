# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/kang/Develop/kkaldi/tutorial-cmake/demo1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/kang/Develop/kkaldi/tutorial-cmake/demo1

# Include any dependencies generated for this target.
include CMakeFiles/Demo.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Demo.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Demo.dir/flags.make

CMakeFiles/Demo.dir/main.cc.o: CMakeFiles/Demo.dir/flags.make
CMakeFiles/Demo.dir/main.cc.o: main.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/kang/Develop/kkaldi/tutorial-cmake/demo1/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Demo.dir/main.cc.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Demo.dir/main.cc.o -c /home/kang/Develop/kkaldi/tutorial-cmake/demo1/main.cc

CMakeFiles/Demo.dir/main.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Demo.dir/main.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/kang/Develop/kkaldi/tutorial-cmake/demo1/main.cc > CMakeFiles/Demo.dir/main.cc.i

CMakeFiles/Demo.dir/main.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Demo.dir/main.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/kang/Develop/kkaldi/tutorial-cmake/demo1/main.cc -o CMakeFiles/Demo.dir/main.cc.s

# Object files for target Demo
Demo_OBJECTS = \
"CMakeFiles/Demo.dir/main.cc.o"

# External object files for target Demo
Demo_EXTERNAL_OBJECTS =

Demo: CMakeFiles/Demo.dir/main.cc.o
Demo: CMakeFiles/Demo.dir/build.make
Demo: CMakeFiles/Demo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/kang/Develop/kkaldi/tutorial-cmake/demo1/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Demo"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Demo.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Demo.dir/build: Demo

.PHONY : CMakeFiles/Demo.dir/build

CMakeFiles/Demo.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Demo.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Demo.dir/clean

CMakeFiles/Demo.dir/depend:
	cd /home/kang/Develop/kkaldi/tutorial-cmake/demo1 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/kang/Develop/kkaldi/tutorial-cmake/demo1 /home/kang/Develop/kkaldi/tutorial-cmake/demo1 /home/kang/Develop/kkaldi/tutorial-cmake/demo1 /home/kang/Develop/kkaldi/tutorial-cmake/demo1 /home/kang/Develop/kkaldi/tutorial-cmake/demo1/CMakeFiles/Demo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Demo.dir/depend

