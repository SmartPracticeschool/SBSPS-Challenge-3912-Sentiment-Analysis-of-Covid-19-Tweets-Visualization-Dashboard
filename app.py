import streamlit as st
from PIL import Image

import dashboard
import about
import line_plot
import area_plot
import hashtags_subplots
import notsopopulartags
import month_bar_plot
import city_bar_plot
import geo_plot
import title
import doughnut

HEIGHT = 650
WIDTH = 850

title.main()

# sidebar options

page_options = ['Home', 'Plots', 'About']
st.sidebar.header('Pick a page')
page_choice = st.sidebar.selectbox('', page_options)

if page_choice == 'About':

    st.sidebar.header('About ')
    about_options = ['IBM HACK Challenge?', 'Sentiment Analysis?']
    about_choice = st.sidebar.radio('What is',
                                    about_options,
                                    index=0)

    about.main(about_choice)

    st.sidebar.subheader('Authors')
    st.sidebar.markdown("### [Animesh Singh](https://www.linkedin.com/in/animesh-singh-profile/)")
    st.sidebar.info('B.Tech, IT, 3rd year - KIET Group of Institutions')
    st.sidebar.markdown("### [Aaditya Kapoor](https://www.linkedin.com/in/aadityakapoor06/)")
    st.sidebar.info('B.Tech, CSE, 4th year - Galgotias University')

elif page_choice == 'Plots':
    plot_options = ['Time Series plots', 'Misc. plots',
                    'Geographical plots', 'Hash-tags plots']
    st.sidebar.header('Pick plot category')
    plot_choice = st.sidebar.selectbox('', plot_options)

    themes = ['Light', 'Dark'] if plot_choice != 'Geographical plots' else ['Light', 'Dark', 'Satellite']
    st.sidebar.header('Pick theme')
    theme_choice = st.sidebar.radio('Theme',
                                    themes,
                                    index=1)
    theme_choice = 'plotly' if theme_choice == 'Light' else 'plotly_dark' if theme_choice == 'Dark' else 'satellite'

    if plot_choice == 'Time Series plots':
        st.markdown('<br>', unsafe_allow_html=True)
        sentiment_picker = st.selectbox(label='Pick sentiment for analysis data',
                                        options=('Positive', 'Negative', 'Neutral', 'All'),
                                        index=3,
                                        key='line_plot')
        line_plot.main(theme=theme_choice, height=HEIGHT, width=WIDTH, sentiment_picker=sentiment_picker)
        st.markdown('<br><br>', unsafe_allow_html=True)

        sentiment_picker = st.selectbox(label='Pick sentiment for analysis data',
                                        options=('Positive', 'Somewhat Positive',
                                                 'Negative', 'Somewhat Negative', 'Neutral', 'All'),
                                        index=5,
                                        key='month_bar_plot')

        month_bar_plot.main(theme=theme_choice, height=HEIGHT, width=WIDTH, sentiment_picker=sentiment_picker)
        st.markdown('<br><br>', unsafe_allow_html=True)

        sentiment_picker = st.selectbox(label='Pick sentiment for analysis data',
                                        options=('Positive', 'Negative', 'Neutral', 'All'),
                                        index=3,
                                        key='city_bar_plot')
        city_bar_plot.main(theme=theme_choice, height=HEIGHT, width=WIDTH, sentiment_picker=sentiment_picker)

    elif plot_choice == 'Misc. plots':

        doughnut.main(theme=theme_choice, height=HEIGHT, width=WIDTH)
        st.markdown('<br><br>', unsafe_allow_html=True)
        area_plot.main(theme=theme_choice, height=HEIGHT, width=WIDTH)
        # bar_plot.main(theme_choice, height=650, width=850)

    elif plot_choice == 'Geographical plots':

        # map_plot.main(theme=theme_choice, height=650, width=850)
        geo_plot.main(theme_choice)

    elif plot_choice == 'Hash-tags plots':

        st.markdown('<br>', unsafe_allow_html=True)
        st.subheader('WordCloud for Covid-19 Tweets _Hash-Tags_')
        if theme_choice == 'plotly':
            image = Image.open('Images/img_light.png')
        else:
            image = Image.open('Images/img_dark.png')
        st.image(image, format='png')
        st.markdown('<br>', unsafe_allow_html=True)

        hashtags_subplots.main(theme=theme_choice)
        st.markdown('<br>', unsafe_allow_html=True)

        notsopopulartags.main(theme=theme_choice)


else:
    dashboard.main()
    st.sidebar.subheader('Authors')
    st.sidebar.markdown("### [Animesh Singh](https://www.linkedin.com/in/animesh-singh-profile/)")
    st.sidebar.info('B.Tech, IT, 3rd year - KIET Group of Institutions')
    st.sidebar.markdown("### [Aaditya Kapoor](https://www.linkedin.com/in/aadityakapoor06/)")
    st.sidebar.info('B.Tech, CSE, 4th year - Galgotias University')
# Displaying plots from various files


# Getting data for next 3 plots


# WDcloud.main(theme=theme, height=650, width=850)
# app.line_chart(data=date_data, theme=theme)

# app.line_chart()
