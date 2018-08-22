# Django

### Django使用HttpResponse返回图片并显示

做了一个关于Django的小案例，想要在网页中显示图片，直接在img标签的src属性写图片的路径是不能显示的，查询资料发现在Django中使用图片这类的资源相当繁琐需要进行一定D的配置，摸索了一会没有整明白，想到了写Java时使用文件流返回图片，于是想到使用该种方式来显示图片。使用实例如下：

```python
views.py
def my_image(request,news_id):
    d = path.dirname(__file__)
    #parent_path = path.dirname(d)
    print("d="+str(d))
    imagepath = path.join(d,"static/show/wordimage/"+str(news_id)+".png")
    print("imagepath="+str(imagepath))
    image_data = open(imagepath,"rb").read()
    return HttpResponse(image_data,content_type="image/png") #注意旧版的资料使用mimetype,现在已经改为content_type
```



```python
urls.py
urlpatterns = [
    url(r'^index/$', views.index,name="index"),
    url(r'^search/$', views.search,name="search"),
    url(r'^science/(?P<news_id>.+)/$', views.science,name="science"),
    url(r'^image/(?P<news_id>.+)/$',views.my_image,name="image"),
]
```

```python
template:
<img src="{% url 'show:image' param.id %}" alt="{{param.id}}"/>
```

如果把content_type设置为'image/png',直接访问图片的路由，浏览器会直接进行下载图片的操作。但是如果把content_type设置为''，则当访问图片路由的时候会预览图片。



### 让其他电脑浏览自己的django应用

在项目目录的settings中

ALLOWED_HOSTS = ['*'] *表示通配符

或ALLOWED_HOST = ['172.20.10.2']括号里填你的局域网IP，如果有唯一公网IP，也可以填公网IP。

然后在终端中，输入一下命令

```shell
项目目录$ python3 manage.py runserver 0.0.0.0:8000
```

这样，就可以用你的移动端浏览你的应用了，但是如果用的是局域网IP，要在同一个局域网内才能访问。



### debug=False时如何加载静态文件

```python
settings.py
DEBUG = False
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR,'static')
# ] DEBUG为False时用不到,可以注释掉
```

```python
urls.py
urlpatterns = [
    ...
    url(r'^static/(?P<path>.*)$',serve,{"document_root":settings.STATIC_ROOT})
] # 在urlpatterns中加入了一个静态文件的url匹配
```



### 谷歌开发者工具

- Sources中会显示各应用所使用的静态文件以应用为一级目录,比如app，static，user应用。应用下的路由使用二级目录，比如app/home。静态文件包括html文件，css文件，js文件以及图片。
- Application下有个Frames里的top文件夹放的是当前页面所使用到的静态文件，包括Fonts，Images，Scripts，Stylesheets以及Html页面。



### DEBUG=False的时候一定要设置ALLOWED_HOSTS

不设置的话会报错

```shell
CommandError: You must set settings.ALLOWED_HOSTS if DEBUG is False.
```



### 打印json数据时显示中文字符

```python
>>> import json
>>> d1 = dict(name='张三',age=14)
>>> d1
{'name': '张三', 'age': 14}
>>> print(json.dumps(d1))
{"name": "\u5f20\u4e09", "age": 14} # 中文字符无法正常显示
>>> print(json.dumps(d1,ensure_ascii=False))
{"name": "张三", "age": 14}
```

将ensure_ascii=False就可以正常显示中文字符了。



### http-equiv是什么意思

> http-equiv 属性为名称/值对提供了名称。并指示服务器在发送实际的文档之前先在要传送给浏览器的 MIME 文档头部包含名称/值对。 当服务器向浏览器发送文档时，会先发送许多名称/值对。虽然有些服务器会发送许多这种名称/值对，但是所有服务器都至少要发送一个：content-type:text/html。这将告诉浏览器准备接受一个 HTML 文档。  content-type表示内容类型 如 text/html  text/css 等等等等 charset表示编码 expires表示过期时间 set-cookie说明是否存cookie Refresh表示重定向(也可以当刷新用) 这时的content分两部分 如"1;about:blank" 表示1秒后重定向到about:blank 如果后一部分为空 则默认为刷新.
>
>   name 属性提供了名称/值对中的名称。HTML 和 XHTML 标签都没有指定任何预先定义的 <meta> 名称。通常情况下，您可以自由使用对自己和源文档的读者来说富有意义的名称。  这几个用name标识 便于搜索引擎抓取  description表示网站描述 keywords表示关键字 author表示作者 revised表示版权信息 generator表示网页生成信息 others其他



### label标签

```html
<form>
  <label for="male">Male</label>
  <input type="radio" name="sex" id="male" />
  <br />
  <label for="female">Female</label>
  <input type="radio" name="sex" id="female" />
</form>
```
<label> 标签为 input 元素定义标注（标记）。
label 元素不会向用户呈现任何特殊效果。不过，它为鼠标用户改进了可用性。如果您在 label 元素内点击文本，就会触发此控件。就是说，当用户选择该标签时，浏览器就会自动将焦点转到和标签相关的表单控件上。
**<label> 标签的 for 属性应当与相关元素的 id 属性相同。**



### django在指定文件夹创建app

cd 到指定目录，使用django-admin startapp user.



### django模板里路由不能使用相对路径

### pycharm可以compare with文件



### OAUTH2



### HTTP1.1和1.0版本

主要区别是1.1版本允许多个HTTP请求服用一个TCP连接，以加快传输速度。