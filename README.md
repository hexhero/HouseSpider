# HouseSpider 中国房产交易信息爬虫

------
HouseSpider 爬取 **链家网** 全国各地的房产交易记录.

-----
## 如何运行项目
安装python3, 运行`HouseSpider.py`即可.
需要安装 `BeautifulSoup`,`requests` 组件

### 1. 目前可爬取的信息包括

- [x] 小区名称
- [x] 面积
- [x] 成交日期
- [x] 挂牌价
- [x] 单价 (元/平米)
- [x] 成交周期
- [ ] 房屋朝向
- [ ] 建成时间
- [ ] 产权 

### 2. 数据查看
当程序运行完成,可在程序目录下寻找 house.db 文件中存储了爬取的数据
| 小区名称   | 面积   | 成交日期  |成交价|挂牌价|单价 (元/平米)|成交周期|
| 万家花城一期  | 118.63 |2018-06-28|5650000|5850000|47628|236|