import multipage_streamlit as mt
import page1 as p1
import page2 as p2
import streamlit as st
from streamlit.elements.image import image_to_url
from streamlit.server.server import Server

st.set_page_config(
     page_title="教学评价系统",
     page_icon="🧊",
     layout="wide",    # 'wide' or 'centered'
     initial_sidebar_state="expanded",
 )

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
st.markdown("<h1 style='text-align: center; color: grey;'>教学评价系统</h1>", unsafe_allow_html=True)
st.sidebar.markdown('# :house:首页')
st.sidebar.markdown('# :book:课程信息')
st.sidebar.markdown('''
- 课程任务点
- 章节学习
- 教学预警
''')
st.sidebar.markdown('# :book:课程报表')
st.sidebar.markdown('''
- 课堂活动
- 课堂积分
- 教师评价
- 学生评价
- 作业统计
- 考试统计
- 课程分析报表
''')
st.sidebar.markdown('# :book:信息管理')

if 'first_visit' not in st.session_state:
    st.session_state.first_visit = True
else:
    st.session_state.first_visit = False

# app = mt.MultiPage()
# app.add("课程信息", p1.run)
# app.add("学生评价", p2.run)
# #app.run_radio('课程信息')
# app.run()
app.add_app("课程信息", p1.run)
app.add_app("学生评价", p2.run)
# app.run_radio('经济大数据')
app.run()

sessions = Server.get_current()._session_info_by_id
st.sidebar.info(f'当前在线人数：{len(sessions)}')
