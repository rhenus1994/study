

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
$ apt-get --purge remove packagename
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



### sftp

lls:查看当前的目录

ls:查看远程的目录

put 文件 

put -r 目录

get 文件 

get -r 目录



### vim $(which pip)可以直接调用结果



### CDN

CDN的全称是Content Delivery Network，即[内容分发网络](https://baike.baidu.com/item/%E5%86%85%E5%AE%B9%E5%88%86%E5%8F%91%E7%BD%91%E7%BB%9C/4034265)。其基本思路是尽可能避开互联网上有可能影响数据传输速度和稳定性的瓶颈和环节，使内容传输的更快、更稳定。通过在网络各处放置[节点服务器](https://baike.baidu.com/item/%E8%8A%82%E7%82%B9%E6%9C%8D%E5%8A%A1%E5%99%A8/4576219)所构成的在现有的互联网基础之上的一层智能[虚拟网络](https://baike.baidu.com/item/%E8%99%9A%E6%8B%9F%E7%BD%91%E7%BB%9C/855117)，CDN系统能够实时地根据[网络流量](https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E6%B5%81%E9%87%8F/7489548)和各节点的连接、负载状况以及到用户的距离和响应时间等综合信息将用户的请求重新导向离用户最近的服务节点上。其目的是使用户可就近取得所需内容，解决 Internet网络拥挤的状况，提高用户访问网站的响应速度。



### oneinstack



### linux安装java环境

sudo apt install default-jre



### 终端退出快捷键

ctrl+D 可以退出redis客户端，mysql客户端以及远程服务器客户端。



### 查看ubuntu版本

```shell
cat /etc/issue
```

openresty 非阻塞io

查看Linux核心(cat /etc/proc/cpuinfo)



### vim下复制
在普通模式下 按yy该行，表示复制了这一行，然后按p就复制了这一行的内容。如果想复制多行，可以按数字+yy，比如3yy,表示复制三行。



### vim下撤销操作

在普通模式下 按u撤销上次操作。



### epoll,IO多路复用。



### virtualenvwrapper

记得要在~/.bashrc文件末尾添加

```shell
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

这样设置完毕之后，每次开机后都可以直接WORKON 虚拟环境名直接进入虚拟环境了。

注意:不能直接将外部由virtualenv创建的虚拟环境直接移到~/.virtualenvwrapper中，就算移进去了也是不可用的。

### pip list 与 pip freeze的区别

```shell
(venv) andy@mac-air:~$ pip freeze
certifi==2018.8.13
chardet==3.0.4
idna==2.7
requests==2.19.1
urllib3==1.23

(venv) andy@mac-air:~$ pip list
Package    Version  
---------- ---------
certifi    2018.8.13
chardet    3.0.4    
idna       2.7      
pip        18.0     
requests   2.19.1   
setuptools 40.0.0   
urllib3    1.23     
wheel      0.31.1  
# pip freeze的格式更加明确，适合使用pip freeze > requirements.txt 而且没有创建虚拟环境就自带的库setuptools,wheel,pip。都是用户自己安装的库。
# pip list是表格型的，比较适合看我们的环境里到底有哪些库，而且包含所有的库，包括建虚拟环境就自带的pip库等。
```

pip freeze > requirements.txt中 > 指的是写入，即把pip freeze现实的结果写入requirements.txt中， >>表示追加。



### linux删除文件快键键(mac电脑下)

fn + delete 删除文件

delete 返回上一级



### Linux安装ab命令(Apache Bench)

```shell
sudo apt-get install apache2-utils
```

```bash
Usage: ab [options] [http[s]://]hostname[:port]/path

// 总的请求数
-n requests Number of requests to perform

// 一次同时并发的请求数 总的请求数(n)=次数*一次并发数(c)
-c concurrency Number of multiple requests to make
```

**运行 ab -n 100 -c 10 http://www.meetu.hk/ 对 http://www.meetu.hk/ 进行100次请求，10个并发请求压力测试结果。**

```bash
Server Software: lighttpd/1.4.20
Server Hostname: www.meetu.hk
Server Port: 80
 
Document Path: /
Document Length: 2095 bytes
 
Concurrency Level: 10
 
//整个测试持续的时间 
Time taken for tests: 3.303 seconds
 
//完成的请求数量 
Complete requests: 100
Failed requests: 0
Write errors: 0
Total transferred: 235200 bytes
HTML transferred: 209500 bytes
 
//平均每秒处理30个请求 
Requests per second: 30.27 [#/sec] (mean)
 
//平均每个请求处理时间为330毫秒 注:这里将一次10个并发请求看成一个整体 
Time per request: 330.335 [ms] (mean)
 
//平均每个并发请求处理 时间 为33毫秒 
Time per request: 33.034 [ms] (mean, across all concurrent requests)
Transfer rate: 69.53 [Kbytes/sec] received
 
Connection Times (ms)
min mean[+/-sd] median max
Connect: 51 170 35.9 178 230
Processing: 60 153 64.5 121 263
Waiting: 55 148 64.4 115 258
Total: 235 322 59.9 299 437
 
Percentage of the requests served within a certain time (ms)
 
//在这100个请求中有50%在299毫秒内完成 
50% 299
 
//在这100个请求中有66%在312毫秒内完成 
66% 312
75% 383
80% 412
90% 431
95% 432
98% 436
99% 437
100% 437 (longest request)
```



### Chrome扩展程序商店地址

https://chrome.google.com/webstore/category/extensions

JSONVIEW：一个可以在chrome浏览器上格式化查看json数据的插件，直接在chrome网上应用店搜索下载即可。



### ubuntu下载Postman工具

ubuntu16.04下postman安装方式:

基本步骤:

1):官网下载软件包:

<https://www.getpostman.com/apps>

2):解压安装:

```
sudo tar -xzf Postman-linux-x64-6.0.10.tar.gz   	
```

3):进入解压后的Postman文件夹打开终端,启动Postman 

```
./Postman/Postman
```

​    4):创建启动图标,便于快速启动

  建立软链接,创建解压后的Postman文件中的Postman到/usr/bin/目录下

```
sudo ln -s  /home/c/Downloads/Postman/Postman   /usr/bin/
```



### apt-get autoremove命令不要轻易使用

> ## apt-get autoremove 命令你敢不敢用？
>
> 用apt时看到有提示，说有些软件包已经不再被需要，可以使用
>
> autoremove
>
> 命令删除，我是一个希望保持系统简洁性的人，当然不希望系统有太多不需要而仍然存在东西，喜欢简洁性也是选择debian的一个原因嘛。看autoremove的命令，当然是自动给删除一些东西，呵呵，还真智能啊。
>
> 在使用的时候发现原来不是这么回事，有多次尴尬的经历，让人哭笑不得：
> 1，第一次使用autoremove，删除了我N多的软件，删除时就看到删除的软件包有gnome－theme，gnome－background，file－roller（当时有点纳闷）等，删除完再进系统，傻眼了。主题，背景，文件管理，网络管理工具等很多常用的工具没了，可是我之前却被告知“这些软件是什么什么自动安装的，已经不被需要了”，所以我才删除了。第一次产生这样的疑问：autoremove是通过什么判定这些软件不被需要了？
> 2：有第一次还有第二次，用完automove发现我的锐捷没办法认证了，原来是锐捷需要的libpcap0.8这个被告知“不被需要的工具”被autoremove了。我是每天都要用这个包包的……
> 3：这是最让人郁闷的一次（我觉得自己很笨，都被愚弄了两次，还要用第三次，大概是因为前两次后果不是很严重），就是今天，因为一些原因，切换的windows下几日。再次回到debian，因为用的是testing，有很多软件包没升级了，所以用apt升级软件包，顺便又看到一些软件包不被需要的提示，于是再次很潇洒的apt-get autoremove，这次又是删除了几个软件包。再次开机，debian警告什么守护进程无法启动，还有一些都没办法去描述的问题。这样说吧，在我自己看来我的debian系统在崩溃的边缘了，看来这次严重了。辛苦经营很久，终于让debian播放电影啊，上网阿，什么什么都弄好了，又出现这样的问题，郁闷死了。我只有打算重新安装debian了，这次安装stable的吧。刚刚硬盘安装也没成功，再试。
>
> 那么，autoremove这到底是怎么回事，为什么让我这么受伤害？



### Ubuntu系统自带Wi-Fi热点

**方法一:**

打开设置，Wi-Fi设置，打开Wi-Fi热点，就会自动生成网络名称和口令了。

**方法二:**

具体方法如下：使用ap-hotspot来创建WIFI热点，而不要用Ad hoc。终端里输入：

$ sudo add-apt-repository ppa:nilarimogard/webupd8

$ sudo apt-get update

$ sudo apt-get install ap-hotspot

$ sudo ap-hotspot configure  //这一步会检查ubuntu的网络和WIFI接口，确定后会提示你配置热点，输入ssid和密码之类的就行了

$ sudo ap-hotspot start

 

### scrapy startproject ab时报错解决

```shell
:0: UserWarning: You do not have a working installation of the service_identity module: 'cannot import name 'opentype''.  Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied.  Without the service_identity module, Twisted can perform only rudimentary TLS client hostname verification.  Many valid certificate/hostname mappings may be rejected.
New Scrapy project 'ab', using template directory '/usr/local/lib/python3.5/dist-packages/scrapy/templates/project', created in:
    /home/theeb/ab
```

根据提示，去下载和安装`service_identity`,地址为：<https://pypi.python.org/pypi/service_identity#downloads>，下载whl文件 

```shell
根据提示，去下载和安装service_identity,地址为：https://pypi.python.org/pypi/service_identity#downloads，下载whl文件 
```

```shell
C:\Users\lenovo>scrapy version
:0: UserWarning: You do not have a working installation of the service_identity module: ‘cannot import name ‘opentype‘‘.  Please install it from <https://pypi.python.org/pypi/service_identity> and make sure all of its dependencies are satisfied.  Without the service_identity module, Twisted can perform only rudimentary TLS client hostname verification.  Many valid certificate/hostname mappings may be rejected.
Scrapy 1.5.0
```

 　　可见，在scrapy安装时，其实还有点问题的。

　　其实这种情况下scrapy已经安装好了 可以使用 只是有部分功能 有影响就是其中提到的 service_identity模块。其实这个模块是已经安装了的。但是为什么还会报错呢。耗费了我两个小时 各种发帖 搜索。终于在一位大神那里找到了答案。
　　原因是不知道因为什么原因导致本机上的service_identity模块太老旧，而你通过install安装的时候 不会更新到最新版本。

 　　然后，再执行.

```shell
C:\Users\lenovo>pip install service_identity
C:\Users\lenovo>pip install service_identity --force --upgrade --user
```





### linux重命名文件和文件夹

linux下重命名文件或文件夹的命令mv既可以重命名，又可以移动文件或文件夹.

例子：将目录A重命名为B

mv A B

例子：将/a目录移动到/b下，并重命名为c

mv /a /b/c

 

### 查看在终端输入scrapy startproject ab时所产生的项目是使用的是哪个python解释器

```shell
andy@mac-air:~$ which scrapy
/home/andy/.local/bin/scrapy
andy@mac-air:~$ vim $(which scrapy)
```

出现如下脚本文件

```python
#!/usr/bin/python3
 
# -*- coding: utf-8 -*-
import re
import sys

from scrapy.cmdline import execute

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(execute())
```

正如首行所示，#/usr/bin/python3指定了操作系统执行这个脚本的时候，调用/usr/bin下的python3解释器。



### #!/usr/bin/python3 和 #!/usr/bin/env python3的区别

脚本语言的第一行，目的就是指出，你想要你的这个文件中的代码用什么可执行程序去运行它，就这么简单

\#!/usr/bin/python3是告诉操作系统执行这个脚本的时候，调用/usr/bin下的python3解释器；
\#!/usr/bin/env python3这种用法是为了防止操作系统用户没有将python3装在默认的/usr/bin路径里。当系统看到这一行的时候，首先会到env设置里查找python3的安装路径，再调用对应路径下的解释器程序完成操作。
\#!/usr/bin/python3相当于写死了python3路径;
\#!/usr/bin/env python3会去环境设置寻找python3目录,推荐这种写法

 

### 每个Py程序的最开始都有 #!/usr/bin/python , 这个到底是什么, 有什么作用?

这个符号（#!）的名称，叫做”Shebang”或者”Sha-bang”（还有其他一些名称，不过我一般就用这两个）。

这是脚本语言共同遵守的规则：当第一行为 #!/path/to/script/interpreter时，指定了用来执行本脚本的解释器。 

注意： 1、必须是文件的第一行 2、必须以#!开头，你丢了一个惊叹号 3、/path/to/script/interpreter是脚本解释器的全路径名。  例如： #!/bin/sh shell脚本 #!/usr/bin/perl perl脚本 #!/usr/bin/python python脚本 #!/usr/bin/python3 python3脚本 #!/usr/bin/python2 python2脚本  而有时不太清楚脚本解释器的具体全路径名；或者开发环境与运行环境的安装路径不同。为了保证兼容性，也可以写作： #!/usr/bin/env python3 这样运行时会自动搜索脚本解释器的绝对路径。 



### Linux删除文件时点ESC键可以选择是否



### ll某文件可以直接查看该文件的详细信息

```shell
andy@mac-air:~$ ll /usr/bin/python
lrwxrwxrwx 1 root root 10 Aug 16 20:38 /usr/bin/python -> python3.6m*
# 第一个字母l代表这个文件是个链接文件
```

ll查看文件夹详细信息

```python
andy@mac-air:~$ ll ~/c
total 16
drwxr-xr-x  4 andy andy 4096 Aug 23 22:19 ./
drwxr-xr-x 92 andy andy 4096 Aug 23 22:19 ../
drwxr-xr-x  2 andy andy 4096 Aug 23 22:19 d/
drwxr-xr-x  2 andy andy 4096 Aug 23 22:19 e/
```



### Linux命令中，grep是处理正则表达式的，基本语法为

```shell
grep [option] pattern [file]
```



### 为了将当前目录下所有.TXT文件打包并压缩归档到文件this.tar.gz 我们可以使用tar czvf this.tar.gz ./*.txt



### 创建用户并加入组

比如说创建xp用户并将用户加入到root组中

```shell
useradd -g root xp
```





### 删除当前目录及其子目录下名为'core'的文件

```shell
find . -name core -exec rm {} \
```



### 如何查看/etc所占的磁盘ko

```shell
sudo du -sh /etc # -s代表summary 总结 
# -h --human-readable print sizes in human readable format(e.g.,1K 234M 2G)
```




### 如何一次性创建text/1/2/3/4

```shell
 mkdir–p text/1/2/3/4 
```



###  Linux如何设置dns服务器地址

修改DNS

username@host:~$ vim /etc/resolv.conf

添加nameserver 8.8.8.8 

>8.8.8.8是GOOGLE公司提供的DNS，该地址是全球通用的，相对来说，更适合国外以及访问国外网站的用户使用。
>
>114.114.114.114是国内移动、电信和联通通用的DNS，手机和电脑端都可以使用，干净无广告，解析成功率相对来说更高，国内用户使用的比较多，而且速度相对快、稳定，是国内用户上网常用的DNS。

重新加载网络配置

这里说的重启网络服务，命令如下:

username@host:~$ sudo /etc/init.d/networking restart

注意：配置修改完成后必须重启网络服务后所做的修改才能生效。



### source help文档

```bash
andy@mac-air:~$ source --help
source: source filename [arguments]
    Execute commands from a file in the current shell.
    
    Read and execute commands from FILENAME in the current shell.  The
    entries in $PATH are used to find the directory containing FILENAME.
    If any ARGUMENTS are supplied, they become the positional parameters
    when FILENAME is executed.
    
    Exit Status:
    Returns the status of the last command executed in FILENAME; fails if
    FILENAME cannot be read.

```



### chmod +x ./test.sh使得test.sh文件对于所有用户都增加执行权限

```shell
andy@mac-air:~$ ll test.sh
-rw-r--r-- 1 andy andy 34 Aug 31 20:01 test.sh
andy@mac-air:~$ chmod +x ./test.sh 
andy@mac-air:~$ ll test.sh
-rwxr-xr-x 1 andy andy 34 Aug 31 20:01 test.sh*
```



### shell脚本

> Shell 是一个用 C 语言编写的程序，它是用户使用 Linux 的桥梁。Shell 既是一种命令语言，又是一种程序设计语言。
>
> Shell 是指一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务。
>
> Ken Thompson 的 sh 是第一种 Unix Shell，Windows Explorer 是一个典型的图形界面 Shell。
>
> [**Shell 在线工具**](http://www.runoob.com/try/showbash.php?filename=helloworld)
>
> ------
>
> ## Shell 脚本
>
> Shell 脚本（shell script），是一种为 shell 编写的脚本程序。
>
> 业界所说的 shell 通常都是指 shell 脚本，但读者朋友要知道，shell 和 shell script 是两个不同的概念。
>
> 由于习惯的原因，简洁起见，本文出现的 "shell编程" 都是指 shell 脚本编程，不是指开发 shell 自身。
>
> ------
>
> ## Shell 环境
>
> Shell 编程跟 java、php 编程一样，只要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器就可以了。
>
> Linux 的 Shell 种类众多，常见的有：
>
> - Bourne Shell（/usr/bin/sh或/bin/sh）
> - Bourne Again Shell（/bin/bash）
> - C Shell（/usr/bin/csh）
> - K Shell（/usr/bin/ksh）
> - Shell for Root（/sbin/sh）
> - ……
>
> 本教程关注的是 Bash，也就是 Bourne Again Shell，由于易用和免费，Bash 在日常工作中被广泛使用。同时，Bash 也是大多数Linux 系统默认的 Shell。
>
> 在一般情况下，人们并不区分 Bourne Shell 和 Bourne Again Shell，所以，像 **#!/bin/sh**，它同样也可以改为 **#!/bin/bash**。
>
> \#! 告诉系统其后路径所指定的程序即是解释此脚本文件的 Shell 程序。
>
> ------
>
> ## 第一个shell脚本
>
> 打开文本编辑器(可以使用 vi/vim 命令来创建文件)，新建一个文件 test.sh，扩展名为 sh（sh代表shell），扩展名并不影响脚本执行，见名知意就好，如果你用 php 写 shell 脚本，扩展名就用 php 好了。
>
> 输入一些代码，第一行一般是这样：
>
> ## 实例
>
> \#!/bin/bash
> echo "Hello World !"
>
>  
>
> 运行实例 »
>
> \#! 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 Shell。
>
> echo 命令用于向窗口输出文本。
>
> ### 运行 Shell 脚本有两种方法：
>
> **1、作为可执行程序**
>
> 将上面的代码保存为 test.sh，并 cd 到相应目录：
>
> ```
> chmod +x ./test.sh  #使脚本具有执行权限
> ./test.sh  #执行脚本
> ```
>
> 注意，一定要写成 ./test.sh，而不是 **test.sh**，运行其它二进制的程序也一样，直接写 test.sh，linux 系统会去 PATH 里寻找有没有叫 test.sh 的，而只有 /bin, /sbin, /usr/bin，/usr/sbin 等在 PATH 里，你的当前目录通常不在 PATH 里，所以写成 test.sh 是会找不到命令的，要用 ./test.sh 告诉系统说，就在当前目录找。
>
> **2、作为解释器参数**
>
> 这种运行方式是，直接运行解释器，其参数就是 shell 脚本的文件名，如：
>
> ```
> /bin/sh test.sh
> /bin/php test.php
> ```
>
> 这种方式运行的脚本，不需要在第一行指定解释器信息，写了也没用。



### 查看python安装路径以及pip安装的包

安装python2的pip

```shell
sudo apt-get install python-pip
```

查看pip安装了多少包

```shell
pip list
```

如果电脑有两个python,一个python2，一个python3，使用上面的命令查看的是python3中pip安装的包。要查看python2pip安装的包，如下：

```shell
python2 -m pip list 
```

同理要查看python3的pip安装的包，则如下:

```shell
python3 -m pip list
```



