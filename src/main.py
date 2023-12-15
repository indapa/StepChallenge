import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
import streamlit as st
st.set_page_config(layout="wide")

def _calculate_average_daily_steps(df):
   #calculate average daily steps
   average_daily_steps = df['Steps'].mean().round(0)
   return average_daily_steps

def _calculate_total_steps(df):
   #calculate total steps
   total_steps = df['Steps'].sum()
   return total_steps

def _plot_cumulative_steps(df):
   df['Cumulative Steps'] = df['Steps'].cumsum()
   fig = px.line(df, x='Date', y='Cumulative Steps')
   #set title
   fig.update_layout(title_text='Cumulative Steps')
   st.plotly_chart(fig,use_container_width=True)

def _plot_daily_steps(df):
      fig = px.bar(df, x='Date', y='Steps')  
      #set title 
      fig.update_layout(title_text='Daily Steps')
      st.plotly_chart(fig,use_container_width=True)

def _plot_monthly(df):
   #add column for month in 3 letter format
   df['Month'] = pd.to_datetime(df['Date']).dt.strftime('%b')
   #group by month and calculate average steps
   monthly_df=df.groupby('Month')['Steps'].mean().reset_index()
   monthly_df=monthly_df.sort_values('Month', ascending=False)
   fig = px.bar(monthly_df, x='Month', y='Steps')
  
   #set title
   fig.update_layout(title_text='Average Monthly Steps')
   st.plotly_chart(fig,use_container_width=True)

def _plot_weekly(df):
   df['Week'] = pd.to_datetime(df['Date']).dt.strftime('%U')
   weekly_df=df.groupby('Week')['Steps'].mean().reset_index()
   
   fig = px.bar(weekly_df, x='Week', y='Steps')
   #set title
   fig.update_layout(title_text='Average Weekly Steps')
   st.plotly_chart(fig,use_container_width=True)

default_data = Path(__file__).parent.parent /  "Data" / "steps.csv"
tiger_img = Path(__file__).parent/  "tiger.jpg"


tab1, tab2, tab3= st.tabs(["Introduction", "Benefits of Walking", "Tips for Success"])

with tab1:
   st.header("1 Million Step Challenge")

   st.markdown("""
               
               Join me in my effort to walk 1 million steps in the first 100 days of 2024! That's taking 10,000 steps a day for 100 days!
               
               I've made this app to help me track my progress and keep me motivated. I hope you'll join me in this challenge!

               See this [link](https://docs.google.com/spreadsheets/d/1Gbk39PpU0Ec_bZCs3MnQyTyT_AdhN54TApCMEKY2wy4/edit?usp=sharing) to download a log to track your steps.

               Many smart phones and smart watches have a step counter built in. If you don't have one, you can buy a 
               [pedometer](https://www.amazon.com/s?k=pedometers+for+walking&adgrpid=143345993003&hvadid=673563947727&hvdev=c&hvlocphy=9069547&hvnetw=g&hvqmt=b&hvrand=4109935355670741824&hvtargid=kwd-2246640821&hydadcr=22538_13680667&tag=hydglogoo-20&ref=pd_sl_64txzblgf2_b) or 
                to track your steps.

               As you progress, upload your step count data to plot and visualize your progress! 

               """)

   

   with st.form("my_form"):
     #file csv upload
      uploaded_file = st.file_uploader("Choose a file", type='csv')
      submitted = st.form_submit_button("Submit")
      if submitted:
         df = pd.read_csv(uploaded_file)
         avg_daily_steps=_calculate_average_daily_steps(df)
         total_steps=_calculate_total_steps(df)
      
         col1, col2= st.columns(2)
         col1.metric("Average Daily Steps", avg_daily_steps )
         col2.metric("Total Steps", total_steps)


         _plot_daily_steps(df)
         _plot_cumulative_steps(df)
         _plot_weekly(df)
         _plot_monthly(df)


with tab2:
   st.header("Benefits of Walking")
   st.markdown( """
                

               Did you know that bipedality (the ability walking on two legs) is one of the [hallmarks of human evolution?](https://www.sapiens.org/archaeology/human-bipedality/)

               Humans orginated in Africa and [migrated to other parts of the world by walking](https://outofedenwalk.nationalgeographic.org/#section-3). Walking is a fundamental part of what makes us human.
               But having a sedentary lifefstyle is becoming more common in modern society and there are [many health risks associated with it](https://medlineplus.gov/healthrisksofaninactivelifestyle.html).

               Importantly, even if you exercise regulary, [you can still have a sedentary lifestyle](https://bodyprojectpt.com/blog/sedentary-lifestyle/) if you spend a lot of time sitting.
               This is one reason I wanted to do this challenge. I exercise regularly  (3-4 hours per week) but I spend a lot of time sitting at my desk. I wanted to challenge myself to be active & *mobile*.
               
               The [benefits](https://www.scottsdaleweightloss.com/7-health-benefits-of-walking-10000-steps-a-day/) of walking are numerous. Here are just a few:

               - Walking can help you lose weight
               - Walking can clears the mind and reduces stress
               - Walking can improve your mood
               - Walking can help you sleep better
               - Walking can help improve your blood pressure and blood sugar levels



               """
               )

with tab3:
   st.header("Tips for Success")
   

   st.markdown("""

               Most people average about 3,000-4,000 steps per day. (About 2 miles / 3 km).
               It's not easy to suddenly flip a switch and start walking 10,000 steps per day. Starting in October of 2023, I made it a goal to walk 10,000 steps per day.
               Here are some tips that helped me reach my goal:

               - **Start small**. If you're not used to walking, start with a small goal like 5,000 steps per day. Then gradually increase your goal.
               - **Take walking breaks**. If you work at a desk, take a 5-10 minute walk every hour. 
               - **Walk with a friend**. Walking with a friend can make it more enjoyable and help keep you motivated.



               """)