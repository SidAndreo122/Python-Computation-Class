import streamlit as st
import requests
import pandas as pd

# Streamlit page initial configs
st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="wide")
st.title("🌤️ Weather Dashboard")
st.caption("Live data from OpenWeatherMap API")

API_KEY = st.secrets["OPENWEATHER_API_KEY"]
api_url = "https://api.openweathermap.org/data/2.5"

# Fetch API data functions
@st.cache_data
def fetch_data(city:str, units:str) -> dict:
    response = requests.get(
        f"{api_url}/weather",
        params={"q": city, "appid": API_KEY, "units": units},
    )
    return response.json()

@st.cache_data
def fetch_forecast(city:str, units:str) -> dict:
    response = requests.get(
        f"{api_url}/forecast",
        params={'q':city, 'appid': API_KEY, 'units':units},
    )
    return response.json()


# Sidebar configs
with st.sidebar:
    st.header("Settings")

    city = st.text_input("City name", value="New York", placeholder="e.g. London")

    unit_label = st.radio("Temperature unit", ["Celsius", "Fahrenheit"])
    units = "metric" if unit_label == "Celsius" else "imperial"
    unit_symbol = "°C" if units == "metric" else "°F"

    forecast_days = st.slider("forecast days to show", min_value = 1, max_value = 5, value=3)

    st.divider()
    st.info("Data refreshes every 5 minutes via @st.cache_data")

# fetch data
current_data = fetch_data(city, units)
current_forecast = fetch_forecast(city, units)

# API Error Handling
if current_data.get("cod") != 200:
    st.error(f"Could not fetch current weather: {current_data.get('message', 'Unknown error')}." "Check the city name or your API key.")
    st.stop()

if str(current_forecast.get("cod")) != "200":
    st.error(f" Could not fetch forecast data: {current_forecast.get('message', 'Unknown error')}.")
    st.stop()


# Converting Fetched data into Dataframes
df = pd.DataFrame([{
    "City":        current_data["name"],
    "Temperature": current_data["main"]["temp"],
    "Feels Like":  current_data["main"]["feels_like"],
    "Humidity %":  current_data["main"]["humidity"],
    "Wind Speed":  current_data["wind"]["speed"],
    "Condition":   current_data["weather"][0]["description"].title(),
    "Visibility":  current_data.get("visibility", 0) / 1000,   # metres → km
}])

forecast_records = []
for entry in current_forecast["list"]:
    forecast_records.append({
        "timestamp":   pd.to_datetime(entry["dt"], unit="s"),
        "temp":        entry["main"]["temp"],
        "feels_like":  entry["main"]["feels_like"],
        "humidity":    entry["main"]["humidity"],
        "wind_speed":  entry["wind"]["speed"],
        "condition":   entry["weather"][0]["description"].title(),
    })
 
forecast_df = pd.DataFrame(forecast_records) 

# Filter to the user-selected number of days

cutoff = forecast_df["timestamp"].min() + pd.Timedelta(days=forecast_days)
forecast_df = forecast_df[forecast_df["timestamp"] <= cutoff].copy()

# Time Series Chart

st.subheader(f"Temperature Forecast -- Next {forecast_days} Day(s)")

ts_df = forecast_df.set_index("timestamp")[["temp", "feels_like"]]
ts_df.columns = [f"Temp {unit_symbol}", f"Feels Like {unit_symbol}"]
st.line_chart(ts_df)
 
st.divider()

# Bar Chart

st.subheader("Average Humidity by Day")
 
forecast_df["date"] = forecast_df["timestamp"].dt.date
humidity_by_day = (
    forecast_df.groupby("date")["humidity"]
    .mean()
    .reset_index()
    .rename(columns={"date": "Date", "humidity": "Avg Humidity (%)"})
    .set_index("Date")
)
st.bar_chart(humidity_by_day)
 
st.divider()


# Main Data Table
st.subheader("Full Forecast Data")
 
display_df = forecast_df.copy()
display_df["timestamp"] = display_df["timestamp"].dt.strftime("%a %b %d  %H:%M")
display_df = display_df.rename(columns={
    "timestamp":  "Date / Time",
    "temp":       f"Temp ({unit_symbol})",
    "feels_like": f"Feels Like ({unit_symbol})",
    "humidity":   "Humidity (%)",
    "wind_speed": "Wind Speed",
    "condition":  "Condition",
})
display_df = display_df.drop(columns=["date"])
st.dataframe(display_df, use_container_width=True, hide_index=True)

### Please note Claude AI was used to help me generate the main forecast table, and filtering the data to match user inputted data.
### These are specific prompts:
### 1. Based on this given code:
### How could I create a streamlit table that showcases full forecast data for a city based on fetched API data?
### 2. Based on this given code:
### How could I filter my fetched data so it matches the user's selected days? Most likely forecast_df['timestamp'] would have to be filtered.