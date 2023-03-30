import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Himanshu Agarwal", page_icon="🚀", layout="wide")
config = {'displayModeBar': False} 

img = Image.open('streamlit/resources/images/Profile.png')
NAME = "Himanshu Agarwal"
DESCRIPTION = """Data Scientist | Web Developer | Blockchain Enthusiast"""
EMAIL = ":e-mail: himanshuaaagarwal20022gmail.com"

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(img,width=400)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write(EMAIL)

st.text("")
st.markdown("<h5 style='text-align: center;'>I'm a passionate Software Developer from India.</h5>", unsafe_allow_html=True)
st.markdown(
    '''
    <div align="center">

    [![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=200&color=F70000&center=true&vCenter=true&width=470&lines=Hey!+It's+Himanshu+Agarwal;I'm+a+Software+Developer.;%E2%9D%A4%EF%B8%8F+Data+Analyst+%7C+Python+Developer;I+%E2%9D%A4%EF%B8%8F+DSA.)](https://git.io/typing-svg)
    </div>
    '''
,unsafe_allow_html=True)
st.text("\n")
st.markdown("<h3 style='color:#DE1F1F'>🙋‍♂️ About me</h3>",unsafe_allow_html=True)

st.markdown("Hello! I'm Himanshu, a third-year Computer Science student, a data analyst who loves to explore and contribute to the world.I usually work on **Data Analysing**, **Web Development**, and **UI/UX Designs**.<br><br>I believe in public learning, and consider myself a proactive, responsible and result-oriented professional. ",unsafe_allow_html=True)
st.markdown(
    '''
        - 2x [Kaggle](https://www.kaggle.com/) Expert. See here: **[Kaggle Expert](https://www.kaggle.com/hiimanshuagarwal)**
        - Secretariat at [GDSC-TCET](https://www.gdsctcet.tech/)
    '''
)
st.text("")
st.markdown("<h3 style='color:#DE1F1F'>👨‍💻 Experience</h3>",unsafe_allow_html=True)
st.markdown(
    '''
        - **[Data Science Intern](https://drive.google.com/file/d/1xnRnI0V5B_hLzi1nXBbrkv-TshLG-sqo/view?usp=share_link)** at **[CodeClause](https://internship.codeclause.com/)**. See the [project](https://github.com/himanshu-03/CC-NOV-DATA_SCIENCE)
        - **[Data Science and Business Analytics Intern](https://drive.google.com/file/d/1nFCMda1bdLjNZUE_Wc7gBtDdwtULj-i8/view?usp=sharing)** at **[The Sparks Foundation](https://www.thesparksfoundationsingapore.org/)**. See the [project](https://github.com/himanshu-03/Exploratory-Data-Analysis-IPL)
        - **[Data Science Intern](https://drive.google.com/file/d/1PWHhJqs_bZ05yxPs4qEnbiSw2OMWQUzy/view?usp=share_link)** at **[LetsGrowMore](https://letsgrowmore.in/)**. See the [project](https://github.com/himanshu-03/LGMVIP-DataScience)
        - **[Data Science Intern](https://www.linkedin.com/posts/agarwal-himanshu_opportunity-datascience-internship-activity-7034145319512621056-gyDP?utm_source=share&utm_medium=member_desktop)** at **[Innomatics Research Labs](https://www.innomatics.in/)**
    '''
)
st.text("")
st.markdown("<h3 style='color:#DE1F1F'>🔗Connect with me</h3>",unsafe_allow_html=True)
st.markdown(
    '''
        </h3> 
        <a href="https://www.github.com/himanshu-03" target="_blank"><img alt="Github" width="40px" src="https://cdn-icons-png.flaticon.com/512/733/733553.png"></a> &nbsp&nbsp&nbsp
        <a href="https://www.linkedin.com/in/agarwal-himanshu" target="_blank"><img alt="LinkedIn" width="40px" src="https://cdn-icons-png.flaticon.com/512/3536/3536505.png"></a> &nbsp&nbsp&nbsp
        <a href="https://www.kaggle.com/hiimanshuagarwal" target="_blank"><img alt="Kaggle" width="40px" src="https://img.icons8.com/external-tal-revivo-color-tal-revivo/512/external-kaggle-an-online-community-of-data-scientists-and-machine-learners-owned-by-google-logo-color-tal-revivo.png"></a> &nbsp&nbsp&nbsp
        <a href="https://www.instagram.com/_._hiimanshu_._" target="_blank"><img alt="Instagram" width="40px" src="https://cdn-icons-png.flaticon.com/512/1384/1384063.png"></a> &nbsp&nbsp&nbsp
        <a href="https://www.facebook.com/profile.php?id=100006757421091" target="_blank"><img alt="Facebook" width="40px" src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg"></a> &nbsp&nbsp&nbsp
        <a href="mailto:himanshuaaagarwal2002@gmail.com" target="_blank"><img alt="Gmail" width="40px" src="https://cdn-icons-png.flaticon.com/512/5968/5968534.png"></a>&nbsp&nbsp&nbsp
        <a href="https://api.whatsapp.com/send/?phone=%2B919967432086&text&type=phone_number&app_absent=0" target="_blank"><img alt="Whatsapp" width="40px" src="https://cdn-icons-png.flaticon.com/512/5968/5968841.png"></a>   
        </p> 
    '''
,unsafe_allow_html=True)

st.text("")
st.markdown("<h3 style='color:#DE1F1F'>©️ Important Links</h3>",unsafe_allow_html=True)
st.markdown(
    '''
        - Projects: [github.com/himanshu-03](https://github.com/himanshu-03)
        - Linkedin: [linkedin.com/hiimanshu-agarwal](https://linkedin.com/in/hiimanshu-agarwal)
        - Kaggle: [kaggle.com/hiimanshuagarwal](https://www.kaggle.com/hiimanshuagarwal)
        - Resume: [resume/himanshu-agarwal](https://drive.google.com/file/d/1ezkwZcdzHqzjEtQ6gLJnRmRj7liq9YFC/view?usp=share_link)
    '''
)

st.text("")
st.markdown("<h3 style='color:#DE1F1F'>🚀 Skills</h3>",unsafe_allow_html=True)
st.markdown(
    '''
        Domain | Tech Stacks
        -------- | :-------:
        **Web** | <img src="https://cdn-icons-png.flaticon.com/512/1126/1126012.png" width="40px"><img src="https://cdn-icons-png.flaticon.com/512/174/174854.png" width="40px"><img src="https://cdn-icons-png.flaticon.com/512/732/732190.png" width="40px"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968292.png" width="40px">
        **Blockchain** | <img src="https://cdn-icons-png.flaticon.com/512/4125/4125334.png" width="40px">
        **Languages** | <img src="https://cdn-icons-png.flaticon.com/512/5968/5968350.png" width="40px"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968282.png" width="40px"><img src="https://cdn-icons-png.flaticon.com/512/1199/1199124.png" width="40px"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968322.png" width="40px"><img src="https://cdn-icons-png.flaticon.com/512/6132/6132222.png" width="40px">
        **Databases** | <img src="https://cdn-icons-png.flaticon.com/512/4726/4726022.png" width="40px"><img src="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/erkxwhl1gd48xfhe2yld" width="40px">
        **Tools** | <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png" width="40px"><img src="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/postman-icon.png" width="40px"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968705.png" width="40px"><img src="https://cdn-images-1.medium.com/max/1200/1*A6kkoOVJVpXPWewg8axc5w.png" width="40px"><img src="https://cdn-icons-png.flaticon.com/512/5968/5968472.png" width="40px">
    '''

,unsafe_allow_html=True)

st.text("")
st.markdown("<h3 style='color:#DE1F1F'>🔭 Projects</h3>",unsafe_allow_html=True)
st.markdown(
    '''
    <details>
    <summary><b>Data Science<b></summary>
    <br/>
    
    Project Name | Tech Stack | Source Code | Dataset
    ------- | --------- | :--------: | :--------: 
    Customer Churn Prediction | Python | [Repo](https://github.com/himanshu-03/CC-NOV-DATA_SCIENCE/tree/main/TASK1-Customer_Churn_Prediction), [Kaggle](https://www.kaggle.com/code/hiimanshuagarwal/customer-churn-prediction) | [Kaggle](https://www.kaggle.com/datasets/hiimanshuagarwal/predictive-maintenance-dataset)
    Covid Analysis | Python | [Repo](https://github.com/himanshu-03/CC-NOV-DATA_SCIENCE/tree/main/TASK2-Covid_Analysis), [Kaggle](https://www.kaggle.com/code/hiimanshuagarwal/covid-analysis) | [Kaggle](https://www.kaggle.com/datasets/sudalairajkumar/covid19-in-india)
    Exploratory Data Analysis - IPL | Python | [Repo](https://github.com/himanshu-03/Exploratory-Data-Analysis-IPL), [Kaggle](https://www.kaggle.com/code/hiimanshuagarwal/exploratory-data-analysis-sports) | [Kaggle](https://www.kaggle.com/datasets/hiimanshuagarwal/ipl-dataset-2008-2020)
    IRIS Flower Classification | Python | [Repo](https://github.com/himanshu-03/LGMVIP-DataScience/tree/main/TASK1_IRIS_Flower_Classification) | Iris Dataset
    Stock Market Prediction using LSTM | Python | [Repo](https://github.com/himanshu-03/LGMVIP-DataScience/tree/main/TASK2_Stock_Market_Prediction_LSTM), [Kaggle](https://www.kaggle.com/code/hiimanshuagarwal/stock-market-price-prediction-using-lstm) | [Kaggle](https://www.kaggle.com/datasets/hiimanshuagarwal/nse-tataglobal)
    Exploratory Data Analysis on Dataset Terrorism | Python | [Repo](https://github.com/himanshu-03/LGMVIP-DataScience/tree/main/TASK3_EDA_Dataset_Terrorism) | [Kaggle](https://www.kaggle.com/datasets/START-UMD/gtd)
    Prediction using Decision Tree Algorrithm | Python | [Repo](https://github.com/himanshu-03/LGMVIP-DataScience/tree/main/TASK4_Prediction_using_Decision_Tree_Algorithm) | Iris dataset
    </details>

    <details>
    <summary><b>Blockchain</b></summary>
    <br/>
  
    Project Name | Tech Stack | Source Code
    ------- | --------- | :--------:
    The Mutant Planets - NFT | Javascript | 
    </details>
    '''
,unsafe_allow_html=True)

st.text("")
st.markdown("<h3 style='color:#DE1F1F'>📊 Github Statistics</h3>",unsafe_allow_html=True)
st.markdown(
    '''
    <div align = "center">
  
    [![Himanshu's GitHub stats](https://github-readme-stats.vercel.app/api?username=himanshu-03&theme=radical)](https://github.com/himanshu-03/github-readme-stats)<br><br>
    [![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=himanshu-03&theme=radical&line_height=15)](https://github.com/himashu-03/github-readme-stats)
    <br><br>
    [![GitHub Streak Dark](https://streak-stats.demolab.com?user=himanshu-03&theme=radical)](https://git.io/streak-stats)
    </div>  
    '''
,unsafe_allow_html=True)

st.text("")
st.markdown("<h3 style='color:#DE1F1F'>🏆 Github Trophies</h3>",unsafe_allow_html=True)
st.markdown(
    '''
    <div align="center">
    
    [![trophy](https://github-profile-trophy.vercel.app/?username=himanshu-03&column=6&theme=radical)](https://github-profile-trophy.vercel.app/?username=himanshu-03&column=6)
    </div>
    '''
,unsafe_allow_html=True)

st.text("")
st.markdown("<h3 style='color:#DE1F1F'>Support</h3>",unsafe_allow_html=True)
st.markdown(
    '''
    <p><a href="https://www.buymeacoffee.com/himanshuagarwal"> <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="himanshuagarwal" /></a></p><br><br>
    <br>
    '''
,unsafe_allow_html=True)


