#爬取智慧树兴趣课：IT互联网分类，综合排序课程

import requests
import json

url = 'https://official-web-search.zhihuishu.com/indexPageSearch/interestCourse'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Referer' : 'https://www.zhihuishu.com/',
    'Cookie' : 'exitRecod_dlQB3J3D=2; Z_LOCALE=1; Hm_lvt_0a1b7151d8c580761c3aef32a3d501c6=1634049533,1634391921,1634914368,1635730544; CASTGC=TGT-9150466-Bl2aTZ6GdUtbTsE56bw7plBcI1emR5XsD9K3cZmsmGjUVnPoWt-passport.zhihuishu.com; CASLOGC=%7B%22realName%22%3A%22%E6%9D%8E%E6%A1%A6%E7%81%BF%22%2C%22myuniRole%22%3A0%2C%22myinstRole%22%3A0%2C%22userId%22%3A804207745%2C%22headPic%22%3A%22https%3A%2F%2Fimage.zhihuishu.com%2Fzhs%2Fablecommons%2Fdemo%2F201804%2F5c4ae8dc37bb40128aa91b8f233a357c_s3.jpg%22%2C%22uuid%22%3A%22dlQB3J3D%22%2C%22mycuRole%22%3A0%2C%22username%22%3A%2252ab96f5b47e47ddb16acdc69ea5c8ce%22%7D; o_session_id=B34F790C56019D92AEED8FC6480147D7; privateCloudSchoolInfo_804207745=",1,#032a49,https://image.zhihuishu.com/testzhs/myuni/home/201607/0581a20796274076ba3849d7d98cd1e3.png,https://image.zhihuishu.com/zhs/myuni/home/201712/92ddc087b6f74edb9a0f8162c8be2cb1.png,506,https://dzzy.zhihuishu.com/hrbeu,"; Hm_lpvt_0a1b7151d8c580761c3aef32a3d501c6=1635739461; acw_tc=2f624a0116357394663572818e2851544f5ff9bc623e5f575d3de99cbeef30; INGRESSCOOKIE=1635739467.364.50657.936226; SERVERID=03054949867e87ef0fcf62686aaa4bba|1635739466|1635739466'
}
params = {
    'interestLabelId': '1',
    'courseType': '-1',
    'orderRuler': '1',
    'pageNo': '0',
    'pageSize': '60',
    'uuid': 'dlQB3J3D',
    'dateFormate': '1635739472000',
}
r = requests.get(url, headers=headers, params=params)
content = r.content
string = content.decode('utf-8')
results = json.loads(string)
i = 1
for course in results["rt"]:
        print(i, ' ', course["courseName"], course["schoolName"]) # 课程名字与大学
        i+=1

'''
1   平面图像处理—PS高手 南华大学
2   国际税收网链上的舞者 吉林财经大学
3   Python程序设计 青岛职业技术学院
4   C语言程序设计（原版） 海南科技职业大学
5   大学计算机基础 广西师范大学
6   互联网与营销创新 华东师范大学
7   计算机应用基础 海南经贸职业技术学院
8   C程序设计 中国海洋大学
9   多媒体课件设计与制作 佳木斯大学
10   大学计算机 
11   计算机软件基础 北京工业大学
12   数据结构 南京邮电大学
13   网络信息安全 青岛职业技术学院
14   《C/C++程序设计》 兰州文理学院
15   大学计算机基础 河北科技大学
16   C语言程序设计 西安理工大学
17   大学计算机 济南大学
18   信息技术基础 河北师范大学
19   flash多媒体开发与制作 海南热带海洋学院
20   大学计算机 北华大学
21   C#基础程序设计 青岛酒店管理职业技术学院
22   Linux操作系统运维 海南软件职业技术学院
23   系统设计创新与机器人实践 
24   高级语言C程序程序设计 华侨大学
25   新媒体与社会性别 复旦大学
26   WLAN无线网络技术 青岛职业技术学院
27   大学计算机基础 山东农业大学
28   新媒体运营（西安欧亚学院） 西安欧亚学院
29   计算机应用基础 吉林交通职业技术学院
30   解码工业互联网平台 中国信息社会50人论坛
31   计算机应用基础 
32   计算机程序设计（C语言） 北华大学
33   数字图像处理 东华理工大学
34   服装电脑辅助设计 海南经贸职业技术学院
35   ASP.NET程序设计 青岛职业技术学院
36   大学计算机基础 西北农林科技大学
37   自动控制原理 
38   程序设计基础 海南大学
39   局域网组建 贵州电子商务职业技术学院
40   计算机通信网络 西北工业大学
41   信息技术基础 海南师范大学
42   影视编辑实战技巧 
43   Java 面向对象程序设计（新） 青岛职业技术学院
44   信息检索 同济大学
45   电视节目策划与制作 河南经贸职业学院
46   Java程序设计教程 内蒙古医科大学
47   网店客服 洛阳科技职业学院
48   计算思维与创新创业 陕西科技大学
49   攻防基础：漏洞利用及渗透测试 南开大学
50   8小时入门计算机绘图 鲁东大学
51   会计信息化 盘锦职业技术学院
52   面向对象分析与设计 华东师范大学
53   网站规划与开发技术 辽宁对外经贸学院
54   电子商务概论 海南经贸职业技术学院
55   网络综合布线 青岛职业技术学院
56   有限元基础与软件应用 北京工业大学
57   Linux开发环境及应用 北京邮电大学
58   软件测试 青岛职业技术学院
59   社会统计学及Satat应用 
60   大趋势 东西部高校联盟
'''