# 0907
- configuration VIM 
ViM can help us to edit and compaile code for ssh remote case.
The code below is the configuration of vim which is saved in path ~/.vimrc

More details please check 'config-vim' 

- make and make install kaldi

First we need to check the volume of disk due to the large size of Tedlium dataset. By using command 'df -h', we know that there are two mount locations "/" and "/data". The mount "/" is SSD drive with high speed but little volume. On the contrary, the mount "/data" uses hard drive.

For this case, we use the following strategy: Kaldi will install and compile in '~' location. Dataset is downloaded in "/data" and linked to '~' path.

The size and structure of disk:

Filesystem      Size  Used Avail Use% Mounted on
udev            7,9G     0  7,9G   0% /dev
tmpfs           1,6G  9,7M  1,6G   1% /run
/dev/sda5       172G  101G   63G  62% /
tmpfs           7,9G  192K  7,9G   1% /dev/shm
tmpfs           5,0M  4,0K  5,0M   1% /run/lock
tmpfs           7,9G     0  7,9G   0% /sys/fs/cgroup
/dev/sdb1       367G   51G  298G  15% /data
tmpfs           1,6G   12K  1,6G   1% /run/user/5011
tmpfs           1,6G   20K  1,6G   1% /run/user/108

Next start to clone the source code:
~~~bash
git clone https://github.com/kaldi-asr/kaldi.git kaldi --origin upstream
cd kaldi
~~~
Check dependencies:
~~~
kang@tueimmk-dan5:~/asr/kaldi/tools$ . ./extras/check_dependencies.sh 
~~~
Result:
1.
-bash: subversion is not installed
-bash: Intel MKL is not installed. Run extras/install_mkl.sh to install it.
 ... You can also use other matrix algebra libraries. For information, see:
  ...   http://kaldi-asr.org/doc/matrixwrap.html
  -bash: Some prerequisites are missing; install them using the command:
    sudo apt-get install subversion
2. 
-bash: Intel MKL is not installed. Run extras/install_mkl.sh to install it.
 ... You can also use other matrix algebra libraries. For information, see:
  ...   http://kaldi-asr.org/doc/matrixwrap.html

When I want to install MKL and the issue occurs:
~~~BASH
W: GPG error: http://dl.google.com/linux/chrome/deb stable InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 78BD65473CB3BD13
~~~
solution
for google
~~~
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 6494C6D6997C215E
~~~
for nividia:
~~~BASH
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
~~~

This issue is still happens:
~~~
E: The repository 'http://ppa.launchpad.net/jonathonf/ffmpeg-3/ubuntu xenial Release' does not have a Release file.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.
~~~

I tried this solution:
~~~BASH
cd /etc/apt/sources.list.d
sudo mv jonathonf-ubuntu-ffmpeg-3-xenial.list.save jonathonf-ubuntu-ffmpeg-3-xenial.list.save.bak
sudo mv jonathonf-ubuntu-ffmpeg-3-xenial.list jonathonf-ubuntu-ffmpeg-3-xenial.list.bak
sudo apt update
~~~

This issue is close.

After we solve this problem, we can enter "./extras/install_mkl.sh" and check dependencies again.Then success.

In tools directory, we can compile the tools
~~~BASH
make j -4
~~~
success.

Issue:
when I want to compile and install kaldi, the process of compile is fail due to version incompatibilities of CUDA.
Here has a similar issue:https://github.com/kaldi-asr/kaldi/issues/1744

solution:
configure "./configure --shared --use-cuda=no"


