# Linux

### 使用pip命令查看环境中已经安装的python包

pip list 查看当前库

pip freeze 显示所有依赖

pip freeze  > requirement.txt  生成requirement.txt文件

pip install -r requirement.txt   根据requirement.txt生成相同的环境

pip -V 可以看与此pip对应的python解释器以及可以看到pip安装的包的存放目录

或者这种方法

![20180528173735592](/home/andy/Desktop/Notes/20180528173735592.png)

直接在IDE中直接打印模块名也可以显示路径

```python
import scrapy
print(scrapy)
<module 'scrapy' from '/home/andy/.local/lib/python3.6/site-packages/scrapy/__init__.py'>
```

### 新建新用户使用useradd和adduser

```shell
andy@mac-air:~$ sudo useradd -m moke
andy@mac-air:~$ sudo passwd moke
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
```

useradd -m --create-home             create the user's home directory



```shell
andy@mac-air:/etc$ sudo adduser mary
Adding user `mary' ...
Adding new group `mary' (1003) ...
Adding new user `mary' (1003) with group `mary' ...
Creating home directory `/home/mary' ...
Copying files from `/etc/skel' ...
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
Changing the user information for mary
Enter the new value, or press ENTER for the default
	Full Name []: 
	Room Number []: 
	Work Phone []: 
	Home Phone []: 
	Other []: 
Is the information correct? [Y/n] y
```

直接就帮你创建好了home目录,还叫你输入密码

### 临时增加环境变量

```shell
andy@mac-air:/etc$ PATH=/home/andy/Desktop:$PATH
andy@mac-air:/etc$ 14.py
start
```

在当前bash窗口添加环境变量,关闭窗口就失效.



### 直接运行.py文件

```python
test.py文件
#!/usr/bin/env python 
print('start')
```

```shell
andy@mac-air:~/Desktop$ chmod 764 test.py 
andy@mac-air:~/Desktop$ ll|grep test.py
-rwxrw-r--  1 andy andy       38 Aug  4 00:30 test.py*
andy@mac-air:~/Desktop$ PATH=$PATH:/home/andy/Desktop/
andy@mac-air:~/Desktop$ test.py
start
```



### linux误删/lib64如何解决

### vim查看行数,永久性显示行数

- 查看行数

  :set number 或者 :set nu

  然后回车

- 隐藏行数

  :set nonnumber 或者 :set nonu

  然后回车

- 永久显示行数

  /etc/vim/vimrc 是系统范围的初始化配置

  ~/.vimrc 个人的vim初始化配置

  - 具体操作

    直接在终端输入vim ~/.vimrc,然后在配置文件中输入set number 或者set nu就可以了.以后想去除的时候注释掉即可.

    

### linux查看外网IP方法

- curl ifconfig.me 响应时间稍长,直接返回外网ip地址
- curl members.3322.org/dyndns/getip 响应时间很快,直接返回ip地址
- curl cip.cc 响应时间很快,返回外网ip地址,地址以及运营商



### vim查找字符串

> 一、用/和？的区别： /后跟查找的字符串。vim会显示文本中第一个出现的字符串。 ?后跟查找的字符串。vim会显示文本中最后一个出现的字符串。
>
> 二、注意事项： 不管用/还是？查找到第一个字符串后，按回车，vim会高亮所有的匹配文  高亮所有的匹配后，按n键转到下一个匹配，按N键转到上一个匹配。

​    

### vim翻页快捷键

Ctrl-f	即PageDown翻页

Ctrl-b	即PageUp翻页



### Linux终端快捷键

Ctrl+Alt+t	打开新的标签页

Ctrl+Alt+w	关闭标签页

Ctrl+d	关闭终端

Ctrl+a	移到当前行的开头

Ctrl+e	移动到当前行的结尾

Ctrl+l	清屏

Ctrl+Alt+c	复制

Ctrl+Alt+v	粘贴

Ctrl+r	查找历史命令

Ctrl+k	删除此处至末尾的所有内容

Ctrl+u	删除此处至开始的所有内容



### Linux常用命令的缩写

/proc -- RROCess

sed -- Stream EDitor

wc -- Word Count

chgrp -- CHange GRouP

grep -- General Regular Expression Print

df -- Disk Free

du -- Disk Usage

ps -- Processes Status

tty -- TeleTYpe

grup -- GRand Unified Bootloader

vi -- VIsual

vim -- Vi IMproved

gtk -- Graphic user interface ToolKit

gnu GPL -- Gnu General Public License

BSD -- Berkeley Software Distribution license



### Linux中sources.list.d文件夹和sudoers.d文件夹后.d的含义

为了防止命名的时候重名，其中d代表的意思就是目录，directory.

```shell
~/$ touch a
~/$ mkdir a
mkdir: cannot create directory ‘a’: File exists
```



### 解决linux下sudo更改文件权限报错xxxis not in the sudoers file. This incident will be reported.

>Linux中普通用户用sudo执行命令时报”xxx is not in the sudoers file.This incident will be reported”错误，解决方法就是在/etc/sudoers文件里给该用户添加权限。如下：
>
>1.切换到root用户下 
>　　方法为直接在命令行输入：su，然后输入密码（即你的登录密码，且密码默认不可见）。
>
>2./etc/sudoers文件默认是只读的，对root来说也是，因此需先添加sudoers文件的写权限,命令是: 
>即执行操作：chmod u+w /etc/sudoers
>
>3.编辑sudoers文件 
>即执行：vi /etc/sudoers 
>找到这行 root ALL=(ALL) ALL,在他下面添加xxx ALL=(ALL) ALL (这里的xxx是你的用户名)
>
>ps:这里说下你可以sudoers添加下面四行中任意一条 
>youuser ALL=(ALL) ALL 
>%youuser ALL=(ALL) ALL 
>youuser ALL=(ALL) NOPASSWD: ALL 
>%youuser ALL=(ALL) NOPASSWD: ALL
>
>第一行:允许用户youuser执行sudo命令(需要输入密码). 
>第二行:允许用户组youuser里面的用户执行sudo命令(需要输入密码). 
>第三行:允许用户youuser执行sudo命令,并且在执行的时候不输入密码. 
>第四行:允许用户组youuser里面的用户执行sudo命令,并且在执行的时候不输入密码.
>
>4.撤销sudoers文件写权限,命令: 
>chmod u-w /etc/sudoers

Please consider adding local content in /etc/sudoers.d/ instead of directly modifying this file.

一般是不建议直接在sudoers文件里直接编辑的，想要增加用户，推荐在sudoers.d文件夹中编辑



Linux查询一个文件详细信息的命令

>linux下查看文件详细信息命令stat。
>
>![dc54564e9258d109b81f0807d758ccbf6d814d82](/home/andy/Desktop/Notes/dc54564e9258d109b81f0807d758ccbf6d814d82.jpg)
>
>说明：Access访问时间。Modify修改时间。Change状态改变时间。可以stat *查看这个目录所有文件的状态
>
>与文件相关的3个时间：
>
>1、访问时间，读一次这个文件的内容，这个时间就会更新。比如对这个文件使用more命令。ls、stat命令都不会修改文件的访问时间。
>
>2、修改时间，对文件内容修改一次，这个时间就会更新。比如：vi后保存文件。ls -l列出的时间就是这个时间。
>
>3、状态改变时间。通过chmod命令更改一次文件属性，这个时间就会更新。查看文件的详细的状态、准确的修改时间等，可以通过stat命令文件名。
>
>size: 427说明:文件的大小.
>
>Blocks: 8说明:这个文件占用了8个块,块的单位是512个字节,因为文件系统的块为4096个字节,除以512个字节，就是8个Blocks.也就是一个文件最小也要占用8个block.
>
>regular file
>
>说明:
>
>文件的状态是不是正常的,此处为完整文件(个人理解是这个意思,请高手指点)
>
>Device: fd00h/64768d
>
>说明:是指存放文件的设备 详细的不太理解 请高手赐教
>
>IO Block: 4096说明:IOBlock表示文件系统块的大小,ext3默认为4096,可以调整为2048等,但ext3最大也即是4096,可以通过tune2fs-l /dev/sda1来确认.
>
>Inode: 23724038
>
>说明:Inode就是I节点,这里说明的是23724038并不是系统已经用了这么多个inode,比如现在新建文件2,inode为23724039,这时新建文件3,inode为23724040,此时你删了文件2,再建文件4,它的inode还是23724039.最后要注意一个文件只有一个Inode,Inode指引我们找到文件的信息.
>
>Links: 1说明:只有这个文件名用了这个Inode.如果有两个文件名用了这个Inode,这里的数字将是2,例如一个硬链接。



### Linux彻底删除用户

创建用户账号时对/etc/passwd、/etc/shadow、/etc/group/、/etc/gshadow四个文件的修改，在文件中添加了该用户和组的相关信息

因为默认情况下创建一个用户账号，会创建一个家目录和一个用户邮箱（在/var/spool/mail目录以用户名命名）。我们可以使用find命令来查找所有与该用户相关的文件信息【find / -name "*xiaoluo*"】.



想要完全删除用户账号（也就是删除所有与该用户相关的文件），以下这两种方法个人觉得是最好的：

​    （1）使用 userdel -r xiaoluo命令删除。

​    （2）先使用userdel xiaoluo 删除账户和组的信息，在使用find查找所有与该用户的相关文件，在使用rm -rf 删除

第二种方法：先使用userdel xiaoluo 删除账户和组的信息，再使用【find / -name "*xiaoluo*"】查找所有于该用户的相关文件，在使用rm -rf 删除

**使用第二种方法的时候，一定要先执行userdel xiaoluo，直接使用 find / -name "*xiaoluo*" |xargs rm -rf只能删除相关目录和文件，不能删除账户信息和组。**



### 安装火狐浏览器

sudo apt install firefox



### ubuntu 源码编译,dpkg,apt 安装原理 及简单使用

> #### 1. 源码编译（源码安装通常安装比较麻烦，特别是解决依赖经常会出现问题，但是通常编译可以获得该软件的最新版本）
>
> - 源码：程序代码，写给人开的程序语言，但机器无法识别，所以无法执行；
> - 编译程序：将程序代码转译成为机器能看得懂的语言，相当与翻译器；
> - 可执行文件：经过编译程序变成二进制程序后机器可以识别的可执行二进制文件；
>
> 而在整个编译的过程，又需要设置软件安装路径，确定链接库位置，检测库依赖关系是否满足，判断目标系统上是否有合适的编译环境等复杂的过程。通常软件开发商都会写这样一个检测程序，来检测用户的操作环境，以及该操作环境是否满足开发商所需的其他功能，替我们完成上诉的复杂过程。检测完毕后，就会主动新建一个**Makefile**的规则文件，而这个检测程序的名字通常为**configure**（下载完软件源码会在源码文件中找到）。
>
> 获取源码文件，解压后，`cd`进入源码文件目录，找到`configure`程序，使用`./configure`建立**Makefile**文件（必须保证Makefile文件正确建立，如果建立不成功的话，查看错误，并依据错误提示，解决后再次建立Makefile文件，直到正确建立**Makefile**文件）
>
> 成功生成 **Makefile**后 我们只需要使用`sudo make`命令进行编译
>
> 编译成功后，使用`sudo make install`进行安装软件
>
> 不过源码安装的话，尽量将源码文件放在一个能找到的特定位置，一般的话**Makefile**也会提供**uninstall**，这样的话，当我们需要卸载软件时，可以到软件包中输入`sudo make uninstall`卸载软件。
> 也可以使用 `./configure --prefix='File Path'`命令，将软件安装在`File Path`位置，这样可以方便删除。关于`configure`的更多参数可以查看软件包中列如ReadMe文件或INSTALL文件，一般有参数设置说明。
>
> 正因为上诉源码安装时出现的各种麻烦，所以引入了软件包管理系统。（不过在使用linux 时需要进行源码编译，也是比较常见的！）
>
> #### 2. dpkg安装
>
> 为了解决上诉问题，很多厂商发布了针对各种 linxu distribution 编译好的软件。因为软件已经编译好了，所以我们只要像windows下一样安装就ok。
>
> linux 开发商在固定的硬件平台和操作系统平台上将需要安装的软件编译好，然后将这个软件所有的相关文件打包成一个特殊格式的文件，这个文件还包括了预先检测系统与依赖的脚本，并且提供记载该软件提供的所有文件信息。客户取得软件包后，只要通过特定的命令来安装，那么该软件就会按照内部的脚本来检测前驱软件的存在，若安装的环境符合满足需求，按么就会开始安装。安装完成后还会将该软件的信息写入软件管理机制中，以完成未来的升级，删除等操作。
>
> 下面是dpkg一些基础命令的简介：
>
> 1. **dpkg -i package-name** 安装软件包
> 2. **dpkg -r package-name** 删除软件包（保留配置信息）
> 3. **dpkg -P package-name** 删除软件包（包括配置信息）
> 4. **dpkg --configure package-name** 配置软件包，如果加上`-a`表示配置所有未配置的软件包
> 5. **dpkg --unpack package-name** 解开软件包到系统目录，但不进行配置
>
> 下面几个命令用于对软件包进行查询
>
> 1. **dpkg -I filename** 查看软件说明(直接使用`dpkg -l` 查询所有安装的软件包，filename可以使用正则，我通常用```dpkg -l | grep "filename"因为会存在软件名记不住的情况)
> 2. **dpkg -L filename** 查看package-name对应的软件包安装的文件及目录
> 3. **dpkg -s filename** 查看package-name对应的软件包信息
> 4. **dpkg -S filename-pattern** 从已经安装的软件包中查找包含filename的软件包名称
>
> dpkg软件包相关文件介绍
> **/etc/dpkg/dpkg.cfg** dpkg包管理软件的配置文件
> **/var/log/dpkg.log** dpkg包管理软件的日志文件
> **/var/lib/dpkg/available** 存放系统所有安装过的软件包信息
> **/var/lib/dpkg/status** 存放系统现在所有安装软件的状态信息
> **/var/lib/dpkg/info** 记安装软件包控制目录的控制信息文件
>
> #### 3. apt安装
>
> 虽然我们在使用**dpkg**时，已经解决掉了 软件安装过程中的大量问题，但是当依赖关系不满足时，仍然需要手动解决，而**apt**这个工具解决了这样的问题，linux distribution 先将软件放置到对应的服务器中，然后分析软件的依赖关系，并且记录下来，然后当客户端有安装软件需求时，通过清单列表与本地的dpkg以存在的软件数据相比较，就能从网络端获取所有需要的具有依赖属性的软件了。
>
> 下面是apt的一些基础命令简介：
>
> 1. **apt-get update** 更新源
> 2. **apt-ge dist-upgrade** 升级系统
> 3. **apt-get upgrade** 更新所有已经安装的软件包
> 4. **apt-get install package_name** 安装软件包(加上 --reinstall重新安装)
> 5. **apt-get remove** 移除软件包（保留配置信息）
> 6. **apt-get purge package_name** 移除软件包（删除配置信息）
> 7. **apt show pack_name** 获取包的相关信息
> 8. **apt search page_name** 搜索包的相关信息
> 9. **apt-cache depends package** 了解使用依赖
> 10. **apt-get check** 检查是否有损坏的依赖
>
> apt软件包相关文件介绍：
> **/etc/apt/sources.list** 记录软件源的地址
> **/var/cache/apt/archives** 已经下载到的软件包都放在这里



### Linux命令find的使用方法

- 输入find -name *history，意思是查询当前目录及子目录下所有以history结尾的文件
- 输入find -name mysql*，意思是查询当前目录及子目录下所有以mysql开头的文件
- 输入find -name mysql* -o -name *history，中间加个-o表示或的意思，就是以mysql开头或history结尾的文件
- 上面是例子没有搜索目录，默认是当前目录下，可以加上目录位置来指定特地的目录下搜索 如find ./apps -name *history 在当前目录下的apps目录下查找以history结尾的文件
- 有时候经常会需要查询最近10分钟修改过的文件，则可以输入find -mmin -10命令来查询



### 2018公共DNS服务器地址评估—DNS推荐

1. 第一名（以平均值排名）

   DNSPod DNS：★★★★★

   DNSPod：相比于去年今年的DNSPod在解析速度上，比以往要快上许多，国内最快节点：上海延迟3ms，最慢节点：新疆哈密延迟73ms

   DNS 服务器 IP 地址：

   首选：119.29.29.29

   备选：182.254.116.116

2. 第二名（以平均值排名）

   114DNS：★★★★★

   114DNS：作为国内用户最多的DNS，自然有他的强大之处，国内最快节点：江苏扬州延迟2ms，最慢节点：辽宁沈阳延迟123ms

   DNS 服务器 IP 地址：

   首选：114.114.114.114

   备选：114.114.114.115

3. 第三名（以平均值排名）

   百度 DNS：★★★★★

   百度DNS：作为互联网巨头，百度在DNS解析速度这一块也是不逞多让，国内最快节点：江苏扬州延迟2ms，最慢节点：辽宁沈阳延迟71ms

   DNS 服务器 IP 地址：

   首选：180.76.76.76

4. 第四名（以平均值排名）

   阿里 DNS：★★★★★

   阿里DNS：同为互联网巨头的阿里，这几年也十分重视DNS解析发展这一块，在解析速度上阿里也不逞多让，国内最快节点：浙江湖州延迟5ms，最慢节点：辽宁沈阳延迟159ms

   DNS 服务器 IP 地址：

   首选：223.5.5.5

   备选：223.6.6.6

5. 第五名（以平均值排名）

   CNNIC SDNS：★★★★★

   SDNS DNS：作为中国互联网络信息中心的DNS，解析网页速度也是很强势，SDNS DNS丝毫不弱于其他几家DNS解析商，国内最快节点：上海延迟6ms，最慢节点：辽宁沈阳延迟146ms

   DNS 服务器 IP 地址：

   首选：1.2.4.8

   备选：202.98.0.68

6. 第六名（以平均值排名）

   DNS派：★★★★★

   DNS派：作为DNS解析商的后起之秀，不得不说DNS派在解析速度上，已经处于一线水准，国内最快节点：上海延迟2ms，最慢节点：河北秦皇岛326ms

   DNS 服务器 IP 地址：

   首选：101.226.4.6

   备选：218.30.118.6

7. 谷歌dns

   现在国内对google屏蔽的很厉害，现在这两个dns很不稳定，建议用其他的开放dns服务器

   首选:8.8.8.8

   备选:8.8.4.4




### Linux建立软链接

- 如果是源文件和目标文件在同一目录下，可以直接ln -s 源文件 目标文件

  ```shell
  andy@mac-air:~/Desktop/Notes$ ln -s Linux.md a.md
  ```

  这样就直接创建了一个Linux.md的软链接 a.md

- 如果是两个文件在不同的目录下，那么需要用ln -s 源文件绝对路径 目标文件绝对路径

  ```shell
  andy@mac-air:~$ ln -s ~/Desktop/Notes/Linux.md ~/Desktop/Linux.md
  ```

  **注意：两边必须要使用绝对路径，不然创建出来的软链接会显示The link "Linux.md" is broken.Move it to trash?**

  

### sudo 出现unable to resolve host 解决方法

> Ubuntu环境, 假设这台机器名字叫abc(机器的hostname), 每次执行sudo 就出现这个警告讯息:
>
> sudo: unable to resolve host abc 
>
> 虽然sudo 还是可以正常执行, 但是警告讯息每次都出来,而这只是机器在反解上的问题, 所以就直接从/etc/hosts 设定, 让abc(hostname) 可以解回127.0.0.1 的IP 即可.
>
>  
>
> /etc/hosts 原始内容
>
> ​          127.0.0.1       localhost
>
> ​          # The following lines are desirable for IPv6 capable hosts 
>
> ​          ::1     localhost ip6-localhost ip6-loopback ip6-loopback
>
> ​         fe00::0 ip6-localnet 
>
> ​         ff00::0 ip6-mcastprefix 
>
> ​         ff02::1 ip6-allnodes
>
> ​         ff02::2 ip6-allrouters 
>
> ​         ff02::3 ip6-allhosts  
>
> ​         在127.0.0.1 localhost 后面加上主机名称(hostname) 即可, /etc/hosts 内容修改成如下:
>
> ```shell
> 127.0.0.1       localhost abc  #要保证这个名字与 /etc/hostname中的主机名一致才有效
> # 或改成下面这两行 
> #127.0.0.1       localhost 
> #127.0.0.1       abc
> 这样设完后, 使用sudo 就不会再有那个提示信息了。
> ```

  

### 无法获得锁 /var/lib/dpkg/lock...解决方法

```bash
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
```

如果还报错，可以执行

```shell
sudo rm /var/lib/apt/lists/lock
sudo rm /var/lib/dpkg/lock
```



### linux下将pycharm添加到系统的"应用程序"菜单里

方法一：

​	Pycharm第一运行的时候，会问你要不要建立快捷方式 当然要建立。

方法2：

>如果你刚开始没有建立快捷方式
>自己建立一个快捷方式，方法如下
>
>终端输入：sudo gedit /usr/share/applications/Pycharm.desktop
>粘贴模板：
>[Desktop Entry]
>Type=Application
>Name=Pycharm
>GenericName=Pycharm3
>Comment=Pycharm3:The Python IDE
>Exec=sh /opt/pycharm/bin/pycharm.sh （下划线部分是你存放的地址）
>Icon=/opt/pycharm/bin/pycharm.png （下划线部分是Pycharm内部的图片，比较一下上下） 
>Terminal=pycharm
>Categories=Pycharm;



### Linux中查找文件并删除

```shell
find taobao # 在当前目录下寻找以taobao为名称的文件和目录 一旦找到目录名为taobao的,会连带把所有taobao目录下的文件和文件夹全显示出来,例如下图
taobao
taobao/.idea
taobao/.idea/misc.xml
taobao/.idea/inspectionProfiles
taobao/.idea/inspectionProfiles/profiles_settings.xml
taobao/.idea/workspace.xml
taobao/.idea/taobao.iml
taobao/.idea/modules.xml
taobao/taobao
taobao/taobao/pipelines.py
taobao/taobao/items.py
taobao/taobao/__init__.py
taobao/taobao/settings.py
taobao/taobao/spiders
taobao/taobao/spiders/__init__.py
taobao/taobao/spiders/__pycache__
taobao/taobao/__pycache__
taobao/taobao/middlewares.py
taobao/scrapy.cfg
```

```shell
find -name taobao # -name表示只查找文件不找目录,并且是递归查找,会找到当前目录及其子目录下所有以taobao为名字的文件
```

查找所有以conf为扩展的文件:

```shell
find / -name "*.conf"
# 建议正则查找时,都加上引号.这里/代表根目录,即查找所有文件.
```

查找文件并删除

```shell
# 以查找和删除mp3为扩展的文件为例：
find / -name "*.mp3" |xargs rm -rf
# 会删除所有以mp3为扩展的文件。操作的时候先：
find / -name "*.mp3"
# 会打印出匹配的文件，如果觉得正是想删除这些文件，再执行：
find / -name "*.mp3" |xargs rm -rf
```



### 虚拟机桥接模式

虚拟机桥接模式相当于虚拟机在宿主机所属的局域网内，所以如果在虚拟机内开启服务，不止宿主机可以访问该服务，同一个局域网内的机子也可以访问该服务。

但是如果虚拟机开启的是NAT模式，那么只有宿主机和虚拟机在同一局域网内（相当于宿主机为虚拟机开辟了一个局域网），所以只有宿主机可以访问虚拟机上的服务。



### 内核态(Kernal Mode)与用户态(User Mode)

> **内核态:** CPU可以访问内存所有数据, 包括外围设备, 例如硬盘, 网卡. CPU也可以将自己从一个程序切换到另一个程序
>
> **用户态:** 只能受限的访问内存, 且不允许访问外围设备. 占用CPU的能力被剥夺, CPU资源可以被其他程序获取
>
> ### 为什么要有用户态和内核态
>
> 由于需要限制不同的程序之间的访问能力, 防止他们获取别的程序的内存数据, 或者获取外围设备的数据, 并发送到网络, CPU划分出两个权限等级 -- **用户态** 和 **内核态**
>
> ### **用户态与内核态的切换**
>
> 所有用户程序都是运行在用户态的, 但是有时候程序确实需要做一些内核态的事情, 例如从硬盘读取数据, 或者从键盘获取输入等. 而唯一可以做这些事情的就是操作系统, 所以此时程序就需要先操作系统请求以程序的名义来执行这些操作.
>
> 这时需要一个这样的机制: 用户态程序切换到内核态, 但是不能控制在内核态中执行的指令
>
> 这种机制叫**系统调用**, 在CPU中的实现称之为**陷阱指令**(Trap Instruction)
>
> 他们的工作流程如下:
>
> 1. 用户态程序将一些数据值放在寄存器中, 或者使用参数创建一个堆栈(stack frame), 以此表明需要操作系统提供的服务.
> 2. 用户态程序执行陷阱指令
> 3. CPU切换到内核态, 并跳到位于内存指定位置的指令, 这些指令是操作系统的一部分, 他们具有内存保护, 不可被用户态程序访问
> 4. 这些指令称之为陷阱(trap)或者系统调用处理器(system call handler). 他们会读取程序放入内存的数据参数, 并执行程序请求的服务
> 5. 系统调用完成后, 操作系统会重置CPU为用户态并返回系统调用的结果



### POSIX(Portable Operating System Interface of UNIX)

> [POSIX](https://baike.baidu.com/item/POSIX)表示[可移植操作系统接口](https://baike.baidu.com/item/%E5%8F%AF%E7%A7%BB%E6%A4%8D%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E6%8E%A5%E5%8F%A3/12718298)（Portable Operating System Interface of UNIX，缩写为 POSIX ），POSIX标准定义了操作系统应该为应用程序提供的接口标准，是[IEEE](https://baike.baidu.com/item/IEEE)为要在各种UNIX操作系统上运行的软件而定义的一系列API标准的总称，其正式称呼为IEEE 1003，而国际标准名称为ISO/IEC 9945。
>
> POSIX标准意在期望获得[源代码](https://baike.baidu.com/item/%E6%BA%90%E4%BB%A3%E7%A0%81/3969)级别的[软件可移植性](https://baike.baidu.com/item/%E8%BD%AF%E4%BB%B6%E5%8F%AF%E7%A7%BB%E6%A4%8D%E6%80%A7/8320795)。换句话说，为一个POSIX兼容的操作系统编写的程序，应该可以在任何其它的POSIX操作系统（即使是来自另一个厂商）上编译执行。
>
> POSIX 并不局限于 UNIX。许多其它的操作系统，例如 DEC OpenVMS 支持 POSIX 标准，尤其是 IEEE Std. 1003.1-1990（1995 年修订）或 POSIX.1，POSIX.1 提供了源代码级别的 C 语言应用编程接口（API）给操作系统的服务程序，例如读写文件。POSIX.1 已经被国际标准化组织（International Standards Organization，ISO）所接受，被命名为 ISO/IEC 9945-1:1990 标准。



### 安装python3对应的pip3

```shell
sudo apt install python3-pip
```



### Flask安装

```shell
pip3 install Flask-SQLAlchemy==2.0
pip3 install flask==0.10.1
```



### 加源的时候如果没有加钥匙会报错

加源的时候如果没有加钥匙，即没有apt-key add那么可能在apt update的时候会报错 http://archive.canonical.com lucid InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 40976EAF437D05B5



### 在安装一个包发现好多依赖包没装时

```shell
Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).
```

可以使用

```shell
sudo apt --fix-broken命令
```

sudo apt-get install -f = sudo apt-get --fix-broken

- -f参数的主要作用是是修复依赖关系（depends），假如用户的系统上有某个package不满足依赖条件，这个命令就会自动修复，重新安装正确版本的。
- -f 是 参数放在 install 前面跟后面是一样的效果。即： " sudo apt-get -f install " equals to " sudo apt-get install -f"

### apt删除软件

```shell
# 卸载一个已安装的软件包（保留配置文件）：
$ apt-get remove packagename
# 卸载一个已安装的软件包（删除配置文件）：
$ apt-get –purge remove packagename
```



### apt-get autoclean clean autoremove的区别

#### apt-get autoclean：

​    如果你的硬盘空间不大的话，可以定期运行这个程序，将已经删除了的软件包的.deb安装文件从硬盘中删除掉。如果你仍然需要硬盘空间的话，可以试试`**apt-get clean**`，这会把你已安装的软件包的安装包也删除掉，当然多数情况下这些包没什么用了，因此这是个为硬盘腾地方的好办法。

#### apt-get clean:

​    类似上面的命令，但它删除包缓存中的**所有**包。这是个很好的做法，因为多数情况下这些包没有用了。但如果你是拨号上网的话，就得重新考虑了。

#### apt-get autoremove:

​    删除为了满足其他软件包的依赖而安装的，但现在不再需要的软件包。



### apt和apt-get不一样



### 在pycharm中，fn+回车键会变成类似于bash的那种光标。Typora中也会出现这种情况

Windows中使用ins键效果一样。



### 互斥锁