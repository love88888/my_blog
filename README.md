创建虚拟环境             mkvirtualenv    项目名称
查看安装的所有虚拟环境     workon
进入虚拟环境              workon  项目名称
退出虚拟环境              deactivate     


创建app                  python3  manage.py startapp  项目名称   
                         django-admin.py startproject 项目名称 .

迁移数据库               makemigrations
                        migrate


运行                   python3   manage.py  runserver 


pip install
Django==1.11.7
mysqlclient


1. 在自己分支cs上提交代码：

git checkout cs

git add .

git commit -m "add files"

 

2. 切换到master分支上，从远程服务器上拉下最新代码：

git checkout master

git pull

 

3. 切换到cs分支上，检查是否与master分支有冲突：

git checkout cs

git rebase master

 

4. 若有冲突，先解决冲突

git add .

git rebase --continue（继续解决冲突）

反复执行这两步，直到所有冲突解决完成

 

5. 将本地代码推送到远程分支上：

git push origin cs:master
