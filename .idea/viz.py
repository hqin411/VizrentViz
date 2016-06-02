import pandas as pd
import numpy as np
import plotly.plotly as py
py.sign_in('baozi5098900','6yrmwg7z51')
import plotly.graph_objs as go
import numexpr as nu
import statistics as stat
from dictmysql import DictMySQL
vizrent=DictMySQL(db='vizrent',host='104.131.11.156',user='qin',passwd='90E4@C3#7378')

#get the data, recode data
a1=vizrent.select(table='apt_attributes')
a2=vizrent.select(table='floorplans')
a3=vizrent.select(table='prices')
a4=vizrent.select(table='properties')
a5=vizrent.select(table='terms')
a6=vizrent.select(table='units')
apt_attribute=pd.DataFrame(list(a1),columns=['apt_attributes_id','properties_id','units_id','floorplans_id','external_id'])
floorplans=pd.DataFrame(list(a2),columns=['floorplans_id','name','floorplans'])
price=pd.DataFrame(list(a3),columns=['id','apt_attributes_id','created_at','available_at','term_id','value'])
properties=pd.DataFrame(list(a4),columns=['id','name','external_id','url'])
terms=pd.DataFrame(list(a5),columns=['id','value'])
units=pd.DataFrame(list(a6),columns=['id','name'])

for i in range(len(floorplans.name)):
    if floorplans.name[i][0] == '1':
        floorplans.floorplans[i] = '1B1B'
    elif floorplans.name[i][0] == 'S':
        floorplans.floorplans[i] = 'Studio'
    elif floorplans.name[i][0] == '4':
        floorplans.floorplans[i] = '4B'
    elif floorplans.name[i][0] == '2':
        floorplans.floorplans[i] = '2B'
    elif floorplans.name[i][0] == '3':
        floorplans.floorplans[i] = '3B'
apt_attributes=pd.merge(apt_attribute,floorplans,on='floorplans_id')
prices=pd.merge(price,apt_attributes,on='apt_attributes_id')

#Available date
##CP 12
median12=prices[(prices.term_id == 2) & (prices.properties_id==1)].groupby(['floorplans', 'created_at'])['value'].median()
data=[]
for i in range (0, len(median12.index.levels[0])):
    trace=go.Scatter(
        y=median12.loc[median12.index.levels[0][i]].values,
        x=median12.loc[median12.index.levels[0][i]].index,
        mode='lines',
        name=median12.index.levels[0][i]
    )
    data.append(trace)
    layout=go.Layout(
        title='Crystal Plaza-12 Month Lease',
        xaxis=dict(
            title='Available Date',
        ),
        yaxis=dict(
            title='US dollar per month'
        )
    )
    fig=go.Figure(data=data,layout=layout)
py.plot(fig,filename='12mplaza')

##CP 6
median6=prices[(prices.term_id == 1) & (prices.properties_id==1)].groupby(['floorplans', 'created_at'])['value'].median()
data=[]
for i in range (0, len(median6.index.levels[0])):
    trace=go.Scatter(
        y=median6.loc[median6.index.levels[0][i]].values,
        x=median6.loc[median6.index.levels[0][i]].index,
        mode='lines',
        name=median6.index.levels[0][i]
    )
    data.append(trace)
    layout = go.Layout(
        title='Crystal Plaza-6 Month Lease',
        xaxis=dict(
            title='Available Date',
        ),
        yaxis=dict(
            title='US dollar per month'
        )
    )
    fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='6mplaza')

##CT 12
median12=prices[(prices.term_id == 2) & (prices.properties_id==2)].groupby(['floorplans', 'created_at'])['value'].median()
data=[]
for i in range (0, len(median12.index.levels[0])):
    trace=go.Scatter(
        y=median12.loc[median12.index.levels[0][i]].values,
        x=median12.loc[median12.index.levels[0][i]].index,
        mode='lines',
        name=median12.index.levels[0][i]
    )
    data.append(trace)
    layout = go.Layout(
        title='Crystal Tower-12 Month Lease',
        xaxis=dict(
            title='Available Date',
        ),
        yaxis=dict(
            title='US dollar per month'
        )
    )
    fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='12mtower')

##CT 6
median6=prices[(prices.term_id == 1) & (prices.properties_id==2)].groupby(['floorplans', 'created_at'])['value'].median()
data=[]
for i in range (0, len(median6.index.levels[0])):
    trace=go.Scatter(
        y=median6.loc[median6.index.levels[0][i]].values,
        x=median6.loc[median6.index.levels[0][i]].index,
        mode='lines',
        name=median6.index.levels[0][i]
    )
    data.append(trace)
    layout = go.Layout(
        title='Crystal Tower-6 Month Lease',
        xaxis=dict(
            title='Available Date',
        ),
        yaxis=dict(
            title='US dollar per month'
        )
    )
    fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='6mtower')