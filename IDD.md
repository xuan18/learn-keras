## 理解
> 任务分析

- 学习运用在AIphaGo上运用的工具



## 困难
> 任务预想主要困难点

- 未知AIphaGo运用哪些工具和知识



## 学习原则

> 问题出现，其一般处理原则

1. 首先参考课程：refer、提醒、problems
2. 官方文档、FAQ
3. 书籍教程
4. [提问的智慧](https://github.com/DebugUself/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)
5. 发布课程issue
6. 参考课程 issue、同学作业
7. 临近任务期限：6



## 方案
> 针对困难和目标功能的开发计划、问题分析

- [x] **d1 理解realpython中pygame例子的每一行代码** 60+32
- [x] **d2 理解snaky代码**
  - 思考：由于理解snaky代码难度太大了，要尝试先自己写下realpython的例子
  - from...import... 和 import 怎么使用？
    - [Python导入模块的几种姿势](https://codingpy.com/article/python-import-101/)
- [ ] **d3 寻找AIphaGo的资料 **
    - [ ] 目前最新版是 AlpahGo Zero
        - [ ] 要了解其用到的工具和知识点，必须从官方渠道知道
            - [ ] 提问的智慧
            - [ ] [DeepMind](https://deepmind.com)
            - [ ] 学习英语阅读
            - [ ] 刻意练习
- [ ] **d？ 学习Keras**
    - [ ] 参考：《 [当 AlphaGo 战胜李世石以后，我们来聊聊深度学习](https://www.infoq.cn/article/Lets-talk-about-deep-learning.) 》
    - [x] 安装ubuntu
    - [ ] relu函数是？
    - [x] 理解2.3.1
      - [x] x[i, j] 是什么？
        - [x] https://blog.csdn.net/xinjieyuan/article/details/81429048
          - [x] ​对于 numpy的dtype **x(array)**（例如 `x = numpy.arrary([1,2])`), i 和 j 表示 索引位置
      - [x] x.shape ?
        - [x] shape 表示形状(p25)
          - [x] x.shape[0],表示在第一维度的所有元素吗？ 但其输出的却为 <class 'tuple'> ，跟我理解不同，尝试理解
            - [x] x = np.array 数据类型为 `<class 'numpy.ndarray'>`
            - [x] 忽略了要把 range 和 x[i,j] 放在一起理解，作注释会容易理解点，i 是列，j 是行
        - [x] 轴(axis)
          - [x] 张量的维度通常叫做轴 p23
    - [x] [numpy.maximun](https://docs.scipy.org/doc/numpy/reference/generated/numpy.maximum.html)
      - [x] 0. 意思为 0.0
      - [x] np.maximum(x1, x2:array_like)
      - [x] numpy 默认的数据类型是？
    - [ ] Y[i, :] == y for i in range(0, 32) ?
         - [x] == ，此符号意思是？
              - [x] python 比较符号
         - [ ] y for i in range(0, 32) ？
- [ ] **具体作业追踪 Issue 模板建议**
- [ ] < 任务 >（< SHA >   t< 0时min >）
        - 思考
- [ ] 「具体作业追踪 Issue 模板建议」（md格式「+」替换为「-」）
### 收集箱

> 收集任务，想法和灵感


- [ ] 检查课程：功能、要求
- [ ] 补看直播
- [ ] 尝试课程：额外
- [ ] 往期 issue
- [ ] close issue
- [ ] 蟒周刊作业「PPS: How-To-Ask-Questions-The-Smart-Way」
- [ ] 阅读参考资料



## 状况

> 记录当日，工作和理解
>
> > 任务分析
>
> - 学习运用在AIphaGo上运用的工具
>
>
>
> ## 困难
> > 任务预想主要困难点
>
> - 未知AIphaGo运用哪些工具和知识
>
>
>
> ## 学习原则
>
> > 问题出现，其一般处理原则
>
> 1. 首先参考课程：refer、提醒、problems
> 2. 官方文档、FAQ
> 3. 书籍教程
> 4. [提问的智慧](https://github.com/DebugUself/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md)
> 5. 发布课程issue
> 6. 参考课程 issue、同学作业
> 7. 临近任务期限：6
>
>
>
> ## 方案
> > 针对困难和目标功能的开发计划、问题分析
>
> - [x] **d1 理解realpython中pygame例子的每一行代码** 60+32
> - [x] **d2 理解snaky代码**
>   - 思考：由于理解snaky代码难度太大了，要尝试先自己写下realpython的例子
>   - from...import... 和 import 怎么使用？
>     - [Python导入模块的几种姿势](https://codingpy.com/article/python-import-101/)
> - [ ] **d3 寻找AIphaGo的资料 **
>     - [ ] 目前最新版是 AlpahGo Zero
>         - [ ] 要了解其用到的工具和知识点，必须从官方渠道知道
>             - [ ] 提问的智慧
>             - [ ] [DeepMind](https://deepmind.com)
>             - [ ] 学习英语阅读
>             - [ ] 刻意练习
> - [ ] **d？ 学习Keras**
>     - [ ] 参考：《 [当 AlphaGo 战胜李世石以后，我们来聊聊深度学习](https://www.infoq.cn/article/Lets-talk-about-deep-learning.) 》
>     - [x] 安装ubuntu
>     - [ ] relu函数是？
>     - [ ] 理解2.3.1
>       - [ ] x[i, j] 是什么？
>         - [ ] https://blog.csdn.net/xinjieyuan/article/details/81429048
>       - [ ] x.shape ?
>         - [ ] 轴？
> - [ ] **具体作业追踪 Issue 模板建议**
> - [ ] < 任务 >（< SHA >   t< 用时min >）
>         - 思考
> - [ ] 「具体作业追踪 Issue 模板建议」（md格式「+」替换为「-」）
> ### 收集箱
>
> > 收集任务，想法和灵感
>
>
> - [ ] 检查课程：功能、要求
> - [ ] 补看直播
> - [ ] 尝试课程：额外
> - [ ] 往期 issue
> - [ ] close issue
> - [ ] 蟒周刊作业「PPS: How-To-Ask-Questions-The-Smart-Way」
> - [ ] 阅读参考资料
>
>
>
> ## 状况
>
> > 记录当日，工作和学习用时（min），身体状况（欠佳（0）；一般（01）；良好（1）），心情
>
> |      | 工作和学习用时 | 身体状况 | 心情                                                         |
> | ---- | -------------- | -------- | ------------------------------------------------------------ |
> | d1   |                |          |                                                              |
> | d2   |                |          |                                                              |
> | d3   |                |          |                                                              |
> | d4   |                |          |                                                              |
> | d5   |                |          |                                                              |
> | d6   |                |          |                                                              |
> | d7   |                |          | 学习用时（min），身体状况（欠佳（0）；一般（01）；良好（1）），心情 |

|      | 工作和学习用时 | 身体状况 | 心情 |
| ---- | -------------- | -------- | ---- |
| d1   |                |          |      |
| d2   |                |          |      |
| d3   |                |          |      |
| d4   |                |          |      |
| d5   |                |          |      |
| d6   |                |          |      |
| d7   |                |          |      |
