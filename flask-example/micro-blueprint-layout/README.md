Here is a simple example of a standard blueprint.

```shell
建议这两个名字保持一致：
工程名：micro-blueprint-layout
项目名：micro-blueprint-layout


[admin@localhost /micro-blueprint-layout]$ tree 
.
|-- manage.py                                   # 主启动文件
`-- micro-blueprint-layout
    |-- __init__.py                             # 注册蓝图
    |-- static
    |-- templates
    `-- views                                   # 各个蓝图的业务逻辑
        |-- bp1.py
        `-- bp2.py

4 directories, 4 files
```
