# Folder

+ judge.py: 核心

+ timelimit.py: 控制运行时间的装饰器

+ settings.json: 配置项

+ data\\...: 测试数据

+ *.cpp: 源码

# Judger

1.  `__init__(self, cfg, src, binary = "std.exe", maxTime = 1000)`

    + cfg: json 配置对象
    + src: 源码文件名
    + binary: 编译生成目标文件名
    + maxTime: 运行时间

2. `compile(self)`

    编译源文件。

3. `getOutput(self)`

    使用源代码和测试数据生成输出数据。

4. `check(self, output, res)`

    对比原始输出数据和 res 中的结果是否一致。

5. `running(self, input)`

    输入 input 中的数据进行测试，返回输出数据和运行时间。

6. `run(self, input, res)`

    输入 input 测试数据进行测试，返回运行结果。

    返回 True 表示正确，或返回其他错误信息。

7. `test(self)`

    测试所有数据返回运行结果。
