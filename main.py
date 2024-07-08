import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title('Weather Forecast for the next Days')

place = st.text_input("Place: ")
forecast_days = st.slider('Forecast Days', 1, 5, help='Select the number of forecasted days.')

display = st.selectbox('Select data to view:',
                      ('Temperature', 'Sky'))

st.subheader(f"{display} for the next {forecast_days} days in {place}.")
if place:
    try:

# Get the temperatreu/ sky data
        filtered_data = get_data(place, forecast_days)

        if display == 'Temperature':
            temperatures = [dict['main']['temp'] / 10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]


        # Create a temperature plot
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)
        if display == 'Sky':
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png',
                      'Rain': 'images/rain.png','Snow': 'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)

    except KeyError:
        st.write('Place not found, please try another.')



