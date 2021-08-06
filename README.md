# it_project team kkpp

## [项目地址](https://github.com/bluegothic/it_project)

## Deployment steps

### 看要求文件(需要进入项目目录)

 `cat requirements.txt`

### 使用如下命令建立并切换环境

```sh
conda create -n kkpp python=3.7.5
conda activate kkpp
conda install django==2.1.5
conda install pillow
```

### Build db and contain some example data

下面的脚本用于清空现有数据库

 `./freshDb.sh`

可能需要下面的命令给予执行权限

 `chmod a+x xxx.sh`

run contain data script

 `python polls_dbitems.py`

## 需要满足的标准（搬运自4-ITECH-Project.pdf）

### 部署

#### 需求文件 3

Requirements file is included and contains the correct packages

#### 不包含 DB/migrations 文件 1

Database / migrations files not included

#### 填入样例文件的脚本 2

Population script works and contains useful example data

#### 可以部署 3

Application can be deployed on marker's own machine

### 功能

#### 设计中反映的主要功能已经实现 10

Main functionality has been implemented reflecting the design

#### 不报错 3

Application is bug-free / no error messages occur

#### Javascript/ JQuery/ AJAX 3

Application includes some Javascript / JQuery / AJAX

### 观感

#### 精美 不过时 3

Polished / refined interface, not clunky

#### 响应式CSS 2

Uses a responsive CSS framework

#### 尺寸变化 1

If browser window size changed, is the change handled neatly?

### 代码

#### helper函数/类 4

Code contains helper functions/classes (if required)

#### 可读 注释 4

Code is readable, clear and commented where appropriate

#### CSS Javascript 分开 4

CSS and Javascript kept separate from templates (i.e., not inline)

#### views 和 templates 里不重复 3

No repetition of code blocks in the views or templates

#### 单元测试 4

Unit tests are included – 4 unique unit tests 4
