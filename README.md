# Cattle

用于在宿主机抓取虚拟机数据包，对虚拟机数据包进行分析，对虚拟机流量监控

通过pcap抓取虚拟机到HOST的port的数据

分析抓取的数据包，获取源地址、端口，目的地址、端口，协议

基于地址、端口、协议统计数据包

将统计的流量数据交给监控系统

## 存在问题

分析虚拟机数据包时可能需要大量计算资源

需要做性能评估
