
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Plastic Hotspot Monitor",
    page_icon="🌊",
    layout="wide"
)

st.title("🌊 Plastic Litter Hotspot Monitor")
st.write(
    "Identify locations where plastic litter "
    "could enter drains and waterways."
)

rainfall = st.selectbox(
    "Choose rainfall scenario",
    ["Light", "Moderate", "Heavy"]
)

df = pd.DataFrame({
    "Location": [
        "Market Road Drain",
        "Residential Drain",
        "Park Drain"
    ],
    "Observed litter": [120, 65, 25],
    "Connectivity": [90, 60, 30],
    "Cleanup feasibility": [80, 75, 95]
})

rain_factor = {
    "Light": 0.7,
    "Moderate": 1.0,
    "Heavy": 1.4
}

df["Priority score"] = (
    0.45 * df["Observed litter"] / 120 * 100
    + 0.35 * df["Connectivity"]
    + 0.20 * df["Cleanup feasibility"]
) * rain_factor[rainfall]

df["Priority score"] = (
    df["Priority score"].clip(upper=100).round(1)
)

df = df.sort_values(
    "Priority score", ascending=False
)

st.subheader("Recommended cleanup priorities")
st.dataframe(df, use_container_width=True)

st.subheader("Hotspot comparison")
st.bar_chart(
    df.set_index("Location")["Priority score"]
)

st.caption(
    "Prototype using illustrative data. "
    "Real drainage and litter data are needed "
    "for real-world predictions."
)
