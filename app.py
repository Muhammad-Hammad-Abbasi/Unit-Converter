import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()


UNIT_SYSTEM = {
    'Length': [
        'meter', 'kilometer', 'centimeter', 'millimeter',
        'micrometer', 'nanometer', 'mile', 'yard', 'foot', 'inch', 'light_year'
    ],
    'Temperature': ['kelvin', 'celsius', 'fahrenheit'],
    'Area': ['meter**2', 'kilometer**2', 'mile**2', 'acre', 'hectare'],
    'Volume': ['liter', 'milliliter', 'gallon', 'cubic_meter'],
    'Weight': ['gram', 'kilogram', 'milligram', 'pound', 'ounce'],
    'Time': ['second', 'minute', 'hour', 'day', 'week', 'year']
}


category = st.sidebar.selectbox("Category", list(UNIT_SYSTEM.keys()))

st.title("📐 Unit Converter Express")
st.header("Convert Any Unit with Ease")


col1, col2, col3 = st.columns([3,1,3])

with col1:
    value = st.number_input("Enter Value", value=1.0)
    from_unit = st.selectbox("From Unit", UNIT_SYSTEM[category])

with col3:
    to_unit = st.selectbox("To Unit", UNIT_SYSTEM[category])
    st.write("")  

if st.button("Convert Now", type="primary"):
    try:
        if category == "Temperature":
            # Special handling for temperature
            input_q = ureg.Quantity(value, ureg(from_unit))
            output_q = input_q.to(ureg(to_unit))
        else:
            # Normal units (length/weight/etc)
            input_q = value * ureg(from_unit)
            output_q = input_q.to(to_unit) 
        
        st.success(f"Result: {output_q.magnitude:.2f} {to_unit}")
    except Exception as e:
        st.error(f"Error: {str(e)}")


st.markdown("---")
st.subheader("Additional Features")
expander = st.expander("Unit Systems Info")
with expander:
    st.write("""
    - **Metric System**: meter, kilogram, liter
    - **Imperial System**: mile, pound, gallon
    - **Scientific Units**: light_year, nanometer
    """)

st.markdown("""
<style>
    [data-testid=stSuccess] {
        background: #e6f4ea;
        border: 1px solid #00cc66;
        padding: 20px;
        border-radius: 5px;
    }
    [data-testid=stError] {
        padding: 20px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)


