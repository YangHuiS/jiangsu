import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.graph_objects as go
from streamlit.elements.image import image_to_url
import numpy as np

#加载背景图（本地图片先转url，网页图片就直接给图片的链接）
img_url = image_to_url('back.png', width=-3, clamp=False,
                       channels='RGB', output_format='auto', image_id='',
                       allow_emoji=False)
# 通过markdown加载背景图（可以是动图、静图）
st.markdown('''
<style>
.css-fg4pbf {background-image: url(''' + img_url + ''');}</style>
''', unsafe_allow_html=True)

# st.markdown('# 教学评价系统')
st.markdown("<h1 style='text-align: center; color: white;'>教学评价系统</h1>", unsafe_allow_html=True)
# st.sidebar.markdown('# :house:首页')
# st.sidebar.markdown('# :book:课程信息')
# st.sidebar.markdown('''
# - 课程任务点
# - 章节学习
# - 教学预警
# ''')
# st.sidebar.markdown('# :book:课程报表')
# st.sidebar.markdown('''
# - 课堂活动
# - 课堂积分
# - 教师评价
# - 学生评价
# - 作业统计
# - 考试统计
# - 课程分析报表
# ''')
# st.sidebar.markdown('# :book:信息管理')

# st.markdown('## :heart:课堂分析报表')

# 五次任务
# tasks = ['林海股份经营目标和评价指标', '营业收入的可视化与评价', '成本费用的可视化与评价',
#          '偿债能力的可视化与评价', '营运能力的可视化与评价', '盈利能力的可视化与评价',
#          '发展能力的可视化与评价', ' 财务分析报告撰写']
def main():
    tasks = ['采购', '销售', '成本', '总账', '营运']
    # 学生名单
    students = '崔耀 郁磊 刘枫 张文莉 刘畅 王盈盈 王甜甜 高思雨 程梦 陈甜甜 王丹 丁亚男 许兰馨 刘星宇 王静怡 程玉珠 葛玚 王帅翔 陈熙贤 史喻航 陈杨 周圆圆 叶宇凡 葛文静'.split()

    scores = pd.DataFrame({
        '姓名': students,
        '团队': ['第1组', '第2组', '第3组', '第4组']*6,
        '得分': [np.random.randint(50, 70) for i in students]
    }).sort_values(['团队', '得分'], ascending=True)

    col1, col2 = st.columns(2)
    with col1:
        # 任务一
        fig = px.bar(scores,  # 带绘图数据
                     x="姓名",  # x轴
                     y="得分",  # y轴
                     color="团队",  # 颜色设置
                     barmode="group",  # 柱状图4种模式之一
                     title=f'任务：{tasks[0]}',
                     )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # 任务二
        df = scores.groupby('团队').tail(4)
        df['得分'] = [np.random.randint(60, 75) for i in range(df.shape[0])]
        df = df.sort_values(['团队', '得分'], ascending=True)
        fig = px.bar(df,  # 带绘图数据
                     x="姓名",  # x轴
                     y="得分",  # y轴
                     color="团队",  # 颜色设置
                     barmode="group",  # 柱状图4种模式之一
                     title=f'任务：{tasks[1]}',
                     )
        st.plotly_chart(fig, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        df2 = df.groupby('团队').tail(3)
        df2['得分'] = [np.random.randint(66, 80) for i in range(df2.shape[0])]
        df2 = df2.sort_values(['团队', '得分'], ascending=True)
        fig = px.bar(df2,  # 带绘图数据
                     x="姓名",  # x轴
                     y="得分",  # y轴
                     color="团队",  # 颜色设置
                     barmode="group",  # 柱状图4种模式之一
                     title=f'任务：{tasks[2]}',
                     )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        df3 = df2.groupby('团队').tail(2)
        df3['得分'] = [np.random.randint(70, 85) for i in range(df3.shape[0])]
        df3 = df3.sort_values(['团队', '得分'], ascending=True)
        fig = px.bar(df3,  # 带绘图数据
                     x="姓名",  # x轴
                     y="得分",  # y轴
                     color="团队",  # 颜色设置
                     barmode="group",  # 柱状图4种模式之一
                     title=f'任务：{tasks[3]}',
                     )
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        df4 = df3.groupby('团队').tail(1)
        df4['得分'] = [np.random.randint(80, 95) for i in range(df4.shape[0])]
        df4 = df4.sort_values(['团队', '得分'], ascending=True)
        fig = px.bar(df4,  # 带绘图数据
                     x="姓名",  # x轴
                     y="得分",  # y轴
                     color="团队",  # 颜色设置
                     barmode="group",  # 柱状图4种模式之一
                     title=f'任务：{tasks[4]}',
                     )
        st.plotly_chart(fig, use_container_width=True)



def run():
    state = State(__name__)
    # the above line is required if you want to save states across page switches.
    # you can provide your own namespace prefix to make keys unique across pages.
    # here we use __name__ for convenience.
    # st.header("房地产数据")

    main()
    # here's the "magic": state(name, default, ...) returns the namespace-prefixed
    # key name. if a previously saved state exist, the widget is set to it. if not,
    # the widget is set to default if it is specified.

    state.save()  # MUST CALL THIS TO SAVE THE STATE!

