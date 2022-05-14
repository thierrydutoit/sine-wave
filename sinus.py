import streamlit as st
from numpy import *
from matplotlib.pyplot import *

st.title('My first signal processing educational webApp')

a=st.slider('Amplitude a', 0, 10, 5)
f=st.slider('Frequency f [Hz]', 0, 1000, 440)

fe=10000;
t=arange(0.0,1,1/fe) 
signal=a*sin(2*pi*f*t)

fig,ax = subplots(figsize=(10,4))
xlim(0,0.010); ylim(-10, 10)
plot(t[0:100],signal[0:100])

st.latex('''a \sin(2 \pi f t)''') 
st.pyplot(fig)

