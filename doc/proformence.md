# 性能验证

## 容量规划

每台服务器*30台vm*

每台vm*1块网卡*

每块网卡高峰速率*100MB/s*

流量分析以数据包为单位，，每个数据包*1000位*

30\*100\*1024\*1024\*8/1000 = *24\*1024\*1024*

测试执行*24\*1024\*1024*次任务需要的时间

## python

代码在tools/performance

```bash
[Running] python -u "d:\three\src\github.com\skdong\cattle\tools\performance.py"
         25165828 function calls in 10.969 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.454    0.454   10.969   10.969 <string>:1(<module>)
        1    6.717    6.717   10.515   10.515 performance.py:3(task_while)
        1    0.000    0.000   10.969   10.969 {built-in method builtins.exec}
 25165824    3.798    0.000    3.798    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



[Done] exited with code=0 in 11.139 seconds

[Running] python -u "d:\three\src\github.com\skdong\cattle\tools\performance.py"
         25165828 function calls in 13.150 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.496    0.496   13.150   13.150 <string>:1(<module>)
        1    8.327    8.327   12.654   12.654 performance.py:3(task_while)
        1    0.000    0.000   13.150   13.150 {built-in method builtins.exec}
 25165824    4.327    0.000    4.327    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



[Done] exited with code=0 in 13.307 seconds

```

## go

```bash
Running tool: C:\Go\bin\go.exe test -benchmem -run=^$ github.com/skdong/cattle/tools -bench ^(BenchmarkTasks)$

goos: windows
goarch: amd64
pkg: github.com/skdong/cattle/tools
BenchmarkTasks-4   1000000000         0.140 ns/op       0 B/op       0 allocs/op
PASS
ok   github.com/skdong/cattle/tools 1.935s
Success: Benchmarks passed.
```
