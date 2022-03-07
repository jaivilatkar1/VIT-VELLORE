# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 16:25:39 2022

@author: Jai
"""
import streamlit as st
import pandas as pd
st.title("Geeks For Geeks")
#n=int(input("Enter number of years greater than 1:"))
#x=int(input("Enter text amount:"))
year=[2,3,4,5,6,7,8,9,10]
#for i in range(len(year)):
#   year.append(int(input()))
st.write("""# COMPOUND INTREST CALCULATOR""")
st.sidebar.header("# VALUES")
def user_features():
    Rate=st.sidebar.slider("Interest percentage",year[0],year[8],3)
    ##st.sidebar.add_rows
    Principle=st.sidebar.text_input("Please input principle amount",100)
    ##st.sidebar.add_rows
    years=st.sidebar.selectbox("Years",year,1)
    data={"Rate":Rate,"Principle":Principle,"Years":years}
    info=pd.DataFrame(data,index=[0])
    return info
df=user_features()
st.subheader("The following infomation is given below:")
st.write(df)
def compound(Principle,Rate,years):
    c=1
    for i in range(len(year)):
        c*=(1+Rate/100)
    c=float(Principle)*(c-1)
    txt=str("Compound Intrest is:"+str("%.3f" %c))
    st.write(txt)
    d1=pd.DataFrame({"Compound Intrest":txt},index=[0])
    return d1
df1=compound(df.Principle, df.Rate, df.Years)
st.write(df1)
