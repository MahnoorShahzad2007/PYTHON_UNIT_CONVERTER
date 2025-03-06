import streamlit as st

st.title("✨ Cute Unit Converter 🦄")
st.subheader("Convert Temperature, Weight & Length Easily! 💖")

# User category selection
category = st.radio("Choose a category:", ["🌡️ Temperature", "⚖️ Weight", "📏 Length"])

if category == "🌡️ Temperature":
    st.write("Convert between Celsius & Fahrenheit! ❄️🔥")
    temp = st.number_input("Enter Temperature:")
    option = st.radio("Select Conversion:", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

    if option == "Celsius to Fahrenheit":
        result = (temp * 9/5) + 32
        st.success(f"🎉 {temp}°C = {result:.2f}°F")
    else:
        result = (temp - 32) * 5/9
        st.success(f"🎉 {temp}°F = {result:.2f}°C")

elif category == "⚖️ Weight":
    st.write("Convert between Kilograms & Pounds! 🏋️‍♂️")
    weight = st.number_input("Enter Weight:")
    option = st.radio("Select Conversion:", ["Kilograms to Pounds", "Pounds to Kilograms"])

    if option == "Kilograms to Pounds":
        result = weight * 2.20462
        st.success(f"🎉 {weight} kg = {result:.2f} lb")
    else:
        result = weight * 0.453592
        st.success(f"🎉 {weight} lb = {result:.2f} kg")

elif category == "📏 Length":
    st.write("Convert between Meters & Feet! 📐")
    length = st.number_input("Enter Length:")
    option = st.radio("Select Conversion:", ["Meters to Feet", "Feet to Meters"])

    if option == "Meters to Feet":
        result = length * 3.28084
        st.success(f"🎉 {length} m = {result:.2f} ft")
    else:
        result = length * 0.3048
        st.success(f"🎉 {length} ft = {result:.2f} m")

st.write("💖 Made with 🥰 in Python & Streamlit!")
