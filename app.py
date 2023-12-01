import streamlit as st

def main():
    st.title('Streamlit App with Embedded My Google Map')
    st.write('Edmponton FoodDrive Mapping:')

    # Embedding Google Map using HTML iframe
    st.markdown("""
    <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1iWj5_TXUUAJt3hgOJ4k9ah_2V_p8Vmo&ehbc=2E312F&noprof=1" width="640" height="480"></iframe>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

