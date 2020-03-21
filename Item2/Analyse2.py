import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Sctot(item):
    # 我们可以在图中清楚地看到，人们传播的信息中，有62%属于真正的谣言!是无中生有，
    # 并且歪曲事实，给群众们带来了一定的恐慌，而还有12%的人，可能是某些公众号、和
    # 医生散播出来的伪科学，比如 ‘买回家的蔬菜必须用75%的酒精消毒’，‘在口罩中间垫
    # 上餐巾纸可以有效阻断新冠病毒’等等十分有争议性但又贴近生活的例子，正是这些贴近
    # 我们的例子才使#得许多社会上的人士、以及老一辈的家长们失去了理性的判断力，从而
    # 一次又一次的转发着这些“博眼球、博热度”的谣言。

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    labels = item["explain"].value_counts().index.tolist()  # 每个文本
    sizes = item["explain"].value_counts().values.tolist()  # 筛选出每个文本所对应的出现次数
    colors = ['lightgreen', 'gold', 'lightskyblue', 'lightcoral']
    plt.figure(figsize=(18, 10))
    plt.pie(sizes, labels=labels,
            colors=None, autopct='%1.1f%%', shadow=True, explode=(0.1, 0.1, 0, 0, 0, 0, 0, 0, 0, 0),
            textprops={'fontsize': 15, 'color': 'black'})  # shadow=True 表示阴影
    plt.axis('equal')  # 设置为正的圆形
    plt.legend(loc='upper right', ncol=2)
    plt.show()



def Broken_line():
    # 可以看到在2020年2月26日、3月8日、3月10日谣言出现了最大值，查看日历后发现2月26日应该是
    # 疫情的爆发期，那为什么在这一天谣言会出现这么多条呢？我想可能是大家都在家中，并且在当时各
    # 地都已经出现了疫情，而这时候正是返工时间，因此对于各大微信群、公众号、微博等就更加关注，
    # 茶余饭后这些消息被以各种交谈的方式散播出去，从而一传十，十传百越传越多。在3月8日和3月10日
    # 左右每天的谣言数目又增加起来，可能是因为我国已经基本控制住了疫情的增长，而外国的疫情却越来
    # 越严重，尤其是欧洲等国。人们可能因此觉得疫情的发源地并不一定是在中国，而很可能是在国外。之
    # 后谣言的数量又逐渐减小了，可能是大家都开始投入到工作和学习中，忙碌起来了，也就不那么关注谣言了。

    data = pd.read_csv('Data_Db.csv')

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    x = data["date"].tolist()  # 可以理解为每个文本
    y = data["explain"].tolist()  # 可以理解为筛选出每个文本所对应的出现次数

    plt.figure(figsize=(20, 20))
    plt.plot(x, y)
    plt.xlabel('日期')  # 设置X轴标签
    plt.ylabel('谣言数')  # 设置Y轴标签
    for x1, y1 in zip(x, y):
        plt.text(x1, y1 + 0.01, '%.0f' % y1, ha='center', va='bottom', fontsize=10.5)
    plt.title('每日的谣言数')  # 设置标题
    plt.xticks(rotation=45)  # 设置刻度和标签
    plt.tick_params(axis='both', labelsize=10)
    plt.show()



def Date_explain(item):
    # 从图中可以看出谣言、伪科学、尚无定论、有失实在这些消息中的占比非常大，我觉得这可能和
    # 这个特殊的时间段有关，因为面对未知的事物我们肯定会恐慌，这时我们的认知能力就会下降，
    # 往往会相信一些未经证实的消息，从而造成谣言、伪科学等消息四处扩散。
    fig, ax = plt.subplots()
    ax.scatter(item['date'], item['explain'])
    ax.set_xlabel('date')                        # 设置x轴名称
    ax.set_ylabel('explain')                     # 设置y轴名称
    plt.title('date & explain')
    plt.xticks(rotation=90)                      # 设置刻度和标签
    plt.show()



def Scanner(item):
    # 从图中可以看出多数都是直接关于疫情以及肺炎传播的，而‘武汉，新型冠状病毒’出现的次数最多，这可能
    # 是因为武汉处于疫情的爆发区，是这场抗击疫情的主战场。因此，所有人的目光都汇聚在这里，它的一举一
    # 动都牵动着人们的心。第二高是‘新型冠状病毒接触传播’、‘新型冠状病毒，NBA’、‘意大利，新型冠状病毒’
    # 、‘新型冠状病毒，韩国’、‘C罗，新型冠状病毒’。这是因为疫情在国外又爆发了，感染人数迅速增加，尤其
    # 是在意大利、韩国和美国，而篮球和足球是受欢迎度最高的两项运动，因此对于它们的关注度非常高，同时也
    # 说明这次疫情的传播能力非常强。
    item1 = item.head(50)
    plt.rcParams['font.sans-serif'] = ['simhei']  # 设置默认字体
    plt.rcParams['axes.unicode_minus'] = False    # 解决保存图象四负号'-'显示为方块的问题
    size = item1['tag'].rank()
    n = 20

    label = item1["tag"].value_counts().index.tolist()  # 每个文本
    size = item1["tag"].value_counts().values.tolist()
    sValue = 40
    color = {0: 'red', 1: 'blue', 2: 'orange'}
    plt.scatter(size, label, c=np.random.rand(43), s=sValue * 10, alpha=0.6)
    plt.xticks(rotation=90)                             # 设置刻度和标签
    plt.show()


def main():
    item = pd.read_csv('新冠肺炎数据.csv', encoding='utf-8')

    Sctot(item)

    Broken_line()

    Date_explain(item)

    Scanner(item)

main()

# 通过分析看以看出在此次疫情期间有大量的谣言、伪科学等被散播出来，我认为大多数的谣言是人们在无意中传播出来的，
# 但也不能排除有人故意为之。总之，现在疫情在世界上正处于爆发期，我们应该积极做好防护工作，不信谣，不传谣，坚
# 守自己的岗位，不为国家添麻烦。