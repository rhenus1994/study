

git init 建立仓库

git add . 将本目录加到暂存区

或git add 爬虫.md 将爬虫.md文件加到暂存区

git commit -m 'first commit' 将暂存区的文件提交到本地库

git remote add origin https://github.com/用户名/仓库名.git 本地库关联到guthub远程库

git push --set-upstream origin master

或git push -u origin master这样下次开始直接git push就好了

如果远程库里有本地库没有的文件，比如README.md

那么需要输入git pull --rebase origin master

然后再git push -u origin master即可