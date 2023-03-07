# 0x01 概述：
 
- 本脚本用于BC导出来的手机号的信息收集（**省份、城市、区号、运营商**）。
- 可举一反三修改脚本、用于其他项目。

![image](/img/2.png)

-This script is used to collect information (**province, city, area code, operator**) of mobile phone numbers derived from gambling.
-You can draw inferences from one instance to modify the script and use it for other projects.

# 0x02 注意事项：

- xlrd高版本只支持解析xls不支持xlsx，会报错：

`AttributeError: ‘ElementTree‘ object has no attribute ‘getiterator‘`

- 故xlsx请另存为xls

# 0x02 开始使用：

```
python phoneInfoSearch.py phone.xls
```

![image](/img/1.png)

结果生成在根目录下New_Tel.xls

![image](/img/2.png)

