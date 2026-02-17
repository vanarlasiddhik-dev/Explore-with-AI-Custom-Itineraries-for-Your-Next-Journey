import streamlit as st
from google import genai
client = genai.Client(api_key="AIzaSyBioEv7fXimGgKerCcET8Aj9kopvom-jNw")

for model in client.models.list():
    print(model.name)

# --- Gemini Function ---
def generate_itinerary(destination, days, nights):
    try:
        client = genai.Client(api_key="AIzaSyBioEv7fXimGgKerCcET8Aj9kopvom-jNw")

        response = client.models.generate_content(
            model="models/gemini-2.5-flash",  # If this fails, change to gemini-1.5-pro
            contents=f"""
            Create a detailed travel itinerary for {days} days and {nights} nights in {destination}.
            Include:
            - Daily activities
            - Food recommendations
            - Attractions
            - Travel tips
            """
        )

        return response.text

    except Exception as e:
        return f"Error occurred: {e}"


# --- Streamlit UI ---
st.title("🌍 AI Travel Itinerary Generator")

destination = st.text_input("Enter Destination")
days = st.number_input("Number of Days", min_value=1, max_value=30, value=2)
nights = st.number_input("Number of Nights", min_value=1, max_value=30, value=1)

if st.button("Generate Itinerary"):
    if destination:
        with st.spinner("Generating itinerary..."):
            itinerary = generate_itinerary(destination, days, nights)

        st.subheader("📍 Your Travel Plan")
        st.write(itinerary)
    else:
        st.warning("Please enter a destination.")
