# it_project team kkpp

https://github.com/bluegothic/it_project

## 环境

```
conda create -n rango python=3.7.5
conda activate rango
conda install django==2.1.5
conda install pillow
```

## 数据库配置

1 运行

`./freshDb.sh`

用于清空现有数据库（可能需要chmod）

2 运行

`python polls_dbitems.py`

填入数据

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
