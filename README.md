# Get-IP-location-from-Excel
从Excel文件批量获取IP地理位置。
## 使用方法（Windows 环境）
### 一、Python 环境配置
安装`qqwry`、`openpyxl`：
```
pip install qqwry
pip install openpyxl
```
### 二、Excel 文件准备
准备含有IP地址的`.xlsx`文件，IP地址应置于**A列**。
例如：
|     | A  | B  |
|  ----  | ----  | ----  |
| **1**  | 192.168.0.1 |   |
| **2**  | 8.8.8.8 |   |
### 三、下载纯真IP库文件
https://www.cz88.net/soft/setup.zip

若无法访问，请自行搜索“纯真IP”。

安装后在**安装目录**找到`qqwry.dat`，复制到与Excel文件相同的文件夹。
### 四、Python 文件修改
将 `lookup.py` 下载到本地，与Excel文件置于同一文件夹，修改第3~5行：
```python
num = 100 #查询的总行数
file = 'ip.xlsx' #文件名，需要在同一目录下
key = 0 #0=只显示地区（如广东省深圳市），1=只显示详细地址（如某某网吧）
```
### 五、运行
打开`命令提示符`或`PowerShell`，切换到Python文件、Excel文件、`qqwry.dat`文件所在的同一文件夹：
```
D:
cd D:\code\IP_Look_up\
```
运行文件：
```
python lookup.py
```
祝君好运。
