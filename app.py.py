import streamlit as st

def main():
    st.title('Streamlit App with Embedded My Google Map')
    st.write('FoodDrive Stakes_Ward_DropOffLocation:')

    # Embedding Google Map using HTML iframe
    st.markdown("""
    <iframe src="https://www.google.com/maps/d/embed?mid=1xych3q6SLdy5f2WdPC0GIQrU-hA9wk8&ehbc=2E312F" width="640" height="480"></iframe>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

