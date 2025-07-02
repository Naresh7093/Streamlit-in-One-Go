import streamlit as st

st.title("Introduction to Streamlit")
st.header("Basics of Streamlit")
st.subheader("Streamlit Uses:")
st.text("Streamlit is used to deploy web apps and models using python language")

st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi')
st.markdown('#### Hi')
st.markdown('##### Hi')

st.success("Data submitted!")
st.info("Information")
st.warning("Warnig!")
st.error("Error!")

st.exception(ZeroDivisionError("Division not possible with 0"))
st.write(range(10))
st.code("x=10\n"
        "for i in range(x):\n"
        "   print(i)")


if(st.checkbox("Male")):
    st.write("You are a Male")

st.checkbox("Female")
st.radio("Select : ",('Check', 'Uncheck'))
st.subheader("Select Box")
selectBox = st.selectbox("Data Science: ", ["Data Analysis", 'Web Scraping', 'Machine Learning', 'Deep Learning'
                                             'NLP','CV', 'Iamge Processing'])
st.write("You've selected : ", selectBox)

st.subheader("MultiSelect Box")
MultiSelect = st.multiselect("Data Science: ", ["Data Analysis", 'Web Scraping', 'Machine Learning', 'Deep Learning'
                                             'NLP','CV', 'Iamge Processing'])
st.write("You've selected: ", MultiSelect)
st.subheader("Button")
st.button("Click me")
st.subheader("Slider")
vol=st.slider('Select the volume', 1,100,step=1)
st.write("Volume: ",vol)
st.subheader("Text Input")
username:st.text_input("Enter UserName: ")
password:st.text_input("Enter password: ",type='password')

st.subheader("Text Area")
st.text_area("Write something interesting about yourself")

st.subheader("Input number")
st.number_input("Select your age",18,110)

st.subheader("Input Date")
st.date_input("Date")

st.subheader("Input Time")
st.time_input("Time")
