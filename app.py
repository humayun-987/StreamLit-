import streamlit as st
st.title('Geeks for Geeks')
st.header('Geeks for Geeks')
st.subheader('Geeks for Geeks')
st.text('Geeks for Geeks')

st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')

st.success('Success !')
st.info('Information !')
st.warning('Warning !')
st.error('Error !')

exp = ZeroDivisionError("Division not possible with '0'")
st.exception(exp)
st.help(ZeroDivisionError)

st.write(range(1,10))
st.write(1+2+3)

st.code('x=10\n'
         'for i in range(x):\n'
         '\tprint(i)')

st.checkbox('Male')
if(st.checkbox('Adult')):
    st.write('You\'re an adult')
    
radioButton = st.radio('Select:',('Male','Female'))

if(radioButton=='Male'):
    st.write('Your\'re a Male')
elif(radioButton=='Female'):
    st.write('Your\'re a Female')

st.subheader('Select Box')
SelectedBox = st.selectbox("Data Science :",['Data Analysis','Web Scrapping','Machine Learning','Deep Learning','Natural Language Processing','Tableau','Image Processing'])
st.write("You have selected : ",SelectedBox)

st.subheader('Multi Select Box')
MultiSelectedBox = st.multiselect("Data Science :",['Data Analysis','Web Scrapping','Machine Learning','Deep Learning','Natural Language Processing','Tableau','Image Processing'])
st.write("You have selected",len(MultiSelectedBox),"courses")

st.subheader("Button")
if(st.button('Click me')):
    st.write("Clicked")
    
st.subheader("Slider")
vol = st.slider('Adjust the volume',0,100,step = 1)
st.write('Volume is : ',vol)

st.subheader('User Input')
username = st.text_input('Username :')
password = st.text_input('Password :',type = 'password')
org_password = 'humayun@987#a23'
if(password == org_password):
    st.write('Hi ',username,'!')
else:
    st.write("Incorrect Password")

st.subheader('Text Area')
textArea = st.text_area('Write something interesting about yourself')
# st.write(textArea)

st.subheader('Enter your age :')
st.number_input('Select your age',18,50)
st.subheader('Enter date :')
st.date_input('Date')
st.subheader('Enter time :')
st.time_input('Time')
