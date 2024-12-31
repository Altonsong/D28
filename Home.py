# practice D28 NASA Open Ai

import streamlit as st
import requests
from datetime import datetime

API_KEY = "8ZSbWLzqlRdwkMRSvxdhQU2gC5ugFbrqUIH2BFfS"
API_URL = "https://api.nasa.gov/planetary/apod"

def fetch_apod(api_key):
    params = {"api_key":api_key}
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()

def main():
    st.set_page_config(page_title="NASA APOD Viewer(Incrk)", layout="centered")
    st.title("🌌 NASA Astronomy Picture of the Day (APOD)")

    try:
        apod_data = fetch_apod(API_KEY)
        date = apod_data.get("date", datetime.now().strftime("%Y-%m-%d"))
        title = apod_data.get("title","No Title")
        explanation = apod_data.get("explanation", "No description available.")
        media_type = apod_data.get("media_type", "image")
        url = apod_data.get("url", "")

        st.subheader(f"{date}:{title}")

        if media_type == "image":
            st.image(url, use_container_width=True, caption=title)
        elif media_type == "video":
            st.video(url)
        else:
            st.write("unsupported media type")

        st.write(explanation)

    except requests.exceptions.RequestExpception as e:
        st.error("Can't load NASA APOD data, please try next time.")
        st.write(e)

if __name__ == "__main__":
    main()

