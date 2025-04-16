import streamlit as st

st.set_page_config(page_title="Unit Convertor")

st.title("Unit Convertor")

# menu = ["Area", "Length", "Energy", "Frequancy", "Mass", "Pressure", "Speed", "Temprature", "Time", "Volume"]
physical_quantities = st.selectbox("Select your unit", ("Area", "Length", "Mass"))
if physical_quantities == "Area":
    unit1 = st.selectbox("Select unit for value", ["Square Meter", "Square Kilometer", "Square Centimeter", "Square Millimeter", "Square Micrometer", "Hectare", "Square Mile", "Square Yard", "Square Foot", "Square Inch", "Acre"])
    unit2 = st.selectbox("Select unit to convert", ["Square Meter", "Square Kilometer", "Square Centimeter", "Square Millimeter", "Square Micrometer", "Hectare", "Square Mile", "Square Yard", "Square Foot", "Square Inch", "Acre"])
    value = st.number_input("Enter value")
    # Square Meter  
    if unit1 == "Square Meter":
        if unit2 == "Square Meter":
           result = value * 1
           st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
           result = value * 0.000001
           st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
           result = value * 10000
           st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Millimeter":
           result = value * 1000000
           st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Micrometer":
           result = value * 1000000000000
           st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
           result = value * 0.0001
           st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
           result = value * 0.00000038610215855
           st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
           result = value * 1.1959900463011
           st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
           result = value * 10.763910417
           st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
           result = value * 1550.003100006
           st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 0.00024710538147
            st.write(f"{value} {unit1} = {result} {unit2}")
    # Square Kilometer
    elif unit1 == "Square Kilometer":
        if unit2 == "Square Meter":
            result = value * 1000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
            result = value * 10000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Millimeter":
            result = value * 1000000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Micrometer":
            result = value * 1000000000000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
            result = value * 100
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
            result = value * 0.38610215855
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
            result = value * 1195990.0463011
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
            result = value * 10763910.417
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
            result = value * 1550003100.006
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 247.10538147
            st.write(f"{value} {unit1} = {result} {unit2}")
        #Square Centimeter
    # Square Centimeter
    elif unit1 == "Square Centimeter":
        if unit2 == "Square Meter":
            result = value * 0.0001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
            result = value * 0.0000000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Millimeter":
            result = value * 100
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Micrometer":
            result = value * 100000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
            result = value * 0.00000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
            result = value * 0.00000000003861021
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
            result = value * 0.000119599
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
            result = value * 0.001076391
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
            result = value * 0.0015500031
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 0.000000024710538147
            st.write(f"{value} {unit1} = {result} {unit2}")
    #Square Millimeter
    elif unit1 == "Square Millimeter":
        if unit2 == "Square Meter":
            result = value * 0.000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
            result = value * 0.000000000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
            result = value * 0.01
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Micrometer":
            result = value * 1000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
            result = value * 0.00000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
            result = value * 0.00000000003861021
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
            result = value * 0.0011959900463
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
            result = value * 0.010763910417
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
            result = value * 0.1550003100006
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 0.000000024710538147
            st.write(f"{value} {unit1} = {result} {unit2}")
    # Square Micrometer
    elif unit1 == "Square Micrometer":
        if unit2 == "Square Meter":
            result = value * 0.0000000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
            result = value * 0.000000000000000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
            result = value * 0.0000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Millimeter":
            result = value * 0.001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
            result = value * 0.00000000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
            result = value * 0.00000000000003861021
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
            result = value * 0.0000011959900463
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
            result = value * 0.000010763910417
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
            result = value * 0.0001550003100006
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 0.000000000024710538147
            st.write(f"{value} {unit1} = {result} {unit2}")
    # Hectare
    elif unit1 == "Hectare":
        if unit2 == "Square Meter":
            result = value * 10000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
            result = value * 0.01
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
            result = value * 100000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Millimeter":
            result = value * 10000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Micrometer":
            result = value * 10000000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
            result = value * 0.0038610215855
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
            result = value * 11959.900463011
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
            result = value * 107639.10417011
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
            result = value * 15500031.00006
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 2.4710538147
            st.write(f"{value} {unit1} = {result} {unit2}")
    # Square Mile
    elif unit1 == "Square Mile":
        if unit2 == "Square Meter":
            result = value * 2589988.110336
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
            result = value * 2.589988110336
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
            result = value * 25899881103.36
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Millimeter":
            result = value * 2589988110336.8
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Micrometer":
            result = value * 2589988110336580
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
            result = value * 258.9988110336
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
            result = value * 3097600
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
            result = value * 27878400
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
            result = value * 4014489600
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 640.00046614685
            st.write(f"{value} {unit1} = {result} {unit2}")
    # Square Yard
    elif unit1 == "Square Yard":
        if unit2 == "Square Meter":
            result = value * 0.83612736
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
            result = value * 0.000083612736
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
            result = value * 8361.2736
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Millimeter":
            result = value * 836127.36
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Micrometer":
            result = value * 836127360000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
            result = value * 0.000083612736
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
            result = value * 0.000000319660955
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
            result = value * 9
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
            result = value * 1296
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 0.00020661157023
            st.write(f"{value} {unit1} = {result} {unit2}")
    # Square Foot
    elif unit1 == "Square Foot":
        if unit2 == "Square Meter":
            result = value * 0.09290304
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
            result = value * 0.00000009290304
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
            result = value * 929.0304
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Millimeter":
            result = value * 92903.04
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Micrometer":
            result = value * 92903040000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
            result = value * 0.000009290304
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
            result = value * 0.000000035870064
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
            result = value * 0.11111111111
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
            result = value * 144
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 0.00002295684114
            st.write(f"{value} {unit1} = {result} {unit2}")
    # Square Inch
    elif unit1 == "Square Inch":
        if unit2 == "Square Meter":
            result = value * 0.00064516
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
            result = value * 0.00000000064516
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
            result = value * 6.4516
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Millimeter":
            result = value * 645.16
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Micrometer":
            result = value * 645160000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
            result = value * 0.000000064516
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
            result = value * 0.0000000002490976
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
            result = value * 0.00077160493827
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
            result = value * 0.0069444444444
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 0.0000001594225074
            st.write(f"{value} {unit1} = {result} {unit2}")
    # Acre
    elif unit1 == "Acre":
        if unit2 == "Square Meter":
            result = value * 4046.8564224
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Kilometer":
            result = value * 0.0040468564224
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Centimeter":
            result = value * 404685.64
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Millimeter":
            result = value * 404685640
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Micrometer":
            result = value * 4046856400000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Hectare":
            result = value * 0.40468564
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Mile":
            result = value * 0.001562498928
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Yard":
            result = value * 4840
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Foot":
            result = value * 43560
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Square Inch":
            result = value * 6272640
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Acre":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
if physical_quantities == "Length":
    unit1 = st.selectbox("Select the unit to convert from:", ["Kilometre", "Meter", "Centimeter", "Millimeter", "Micrometer", "Neno Meter", "Mile", "Yard", "Foot", "Inch", "Nautical mile"])     
    unit2 = st.selectbox("Select the unit to convert to:", ["Kilometre", "Meter", "Centimeter", "Millimeter", "Micrometer", "Neno Meter", "Mile", "Yard", "Foot", "Inch", "Nautical mile"], index=1)
    value = st.number_input("Enter the value to convert:", min_value=0.0)
    if unit1 == "Kilometre":
        if unit2 == "Kilometre":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 1000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 100000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 1000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 1000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 1000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 0.621371192
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 1093.613298
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 3280.839895
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 39370.07874
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 0.539956803
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Meter
    elif unit1 == "Meter":
        if unit2 == "Kilometre":
            result = value * 0.001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 100
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 1000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 1000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 1000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 0.000621371192
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 1.093613298
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 3.280839895
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 39.37007874
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 0.000539956803
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Centimeter
    elif unit1 == "Centimeter":
        if unit2 == "Kilometre":
            result = value * 0.00001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 0.01
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 10
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 10000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 10000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 0.00000621371192
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 0.01093613298
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 0.032808399
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 0.3937007874
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 0.00000539956803
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Millimeter
    elif unit1 == "Millimeter":
        if unit2 == "Kilometre":
            result = value * 0.000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 0.001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 0.1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 1000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 1000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 0.000000621371192
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 0.001093613298
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 0.003280839895
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 0.03937007874
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 0.000000539956803
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Micrometer
    elif unit1 == "Micrometer":
        if unit2 == "Kilometre":
            result = value * 0.000000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 0.000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 0.0001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 0.001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 1000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 0.000000000621371192
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 0.000001093613298
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 0.000003280839895
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 0.00003937007874
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 0.000000000539956803
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Neno Meter
    elif unit1 == "Neno Meter":
        if unit2 == "Kilometre":
            result = value * 0.000000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 0.000000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 0.0000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 0.000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 0.001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 0.000000000000621371192
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 0.000000001093613298
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 0.000000003280839895
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 0.00000003937007874
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 0.000000000000539956803
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Mile
    elif unit1 == "Mile":
        if unit2 == "Kilometre":
            result = value * 1.609344
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 1609.344
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 160934.4
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 1609344
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 1609344000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 1609344000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 1760
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 5280
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 63360
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 0.868976242
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Yard
    elif unit1 == "Yard":
        if unit2 == "Kilometre":
            result = value * 0.0009144
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 0.9144
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 91.44
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 914.4
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 914400
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 914400000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 0.000568181818
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 3
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 36
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 0.000493736501
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Foot
    elif unit1 == "Foot":
        if unit2 == "Kilometre":
            result = value * 0.0003048
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 0.3048
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 30.48
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 304.8
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 304800
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 304800000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 0.000189393939
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 0.333333333
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 12
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 0.000164578834
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Inch
    elif unit1 == "Inch":
        if unit2 == "Kilometre":
            result = value * 0.0000254
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 0.0254
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 2.54
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 25.4
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 25400
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 25400000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 0.000015782828
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 0.0277777778
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 0.0833333333
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 0.0000137149
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Nautical mile
    elif unit1 == "Nautical mile":
        if unit2 == "Kilometre":
            result = value * 1.852
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Meter":
            result = value * 1852
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Centimeter":
            result = value * 185200
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Millimeter":
            result = value * 1852000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Micrometer":
            result = value * 1852000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Neno Meter":
            result = value * 1852000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Mile":
            result = value * 1.150779448
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Yard":
            result = value * 2025.37183
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Foot":
            result = value * 6076.11549
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Inch":
            result = value * 72913.3858
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Nautical mile":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
if physical_quantities == "Mass":
    unit1 = st.selectbox("Select the unit to convert from:", ["Tonne", "Kilogram", "Gram", "Miligram", "Microgram", "Imperial Ton", "Us ton", "Stone", "Pound", "Ounce"])
    unit2 = st.selectbox("Select the unit to convert to:", ["Tonne", "Kilogram", "Gram", "Miligram", "Microgram", "Imperial Ton", "Us ton", "Stone", "Pound", "Ounce"], index=1)
    value = st.number_input("Enter the value to convert:", min_value=0.0)
    if unit1 == "Tonne":
        if unit2 == "Tonne":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Kilogram":
            result = value * 1000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Gram":
            result = value * 1000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Miligram":
            result = value * 1000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Microgram":
            result = value * 1000000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Imperial Ton":
            result = value * 0.984207
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Us ton":
            result = value * 1.10231
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Stone":
            result = value * 157.473
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Pound":
            result = value * 2204.62
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Ounce":
            result = value * 35274
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Kilogram
    elif unit1 == "Kilogram":
        if unit2 == "Tonne":
            result = value * 0.001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Kilogram":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Gram":
            result = value * 1000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Miligram":
            result = value * 1000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Microgram":
            result = value * 1000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Imperial Ton":
            result = value * 0.000984207
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Us ton":
            result = value * 0.00110231
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Stone":
            result = value * 0.157473
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Pound":
            result = value * 2.20462
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Ounce":
            result = value * 35.274
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Gram
    elif unit1 == "Gram":
        if unit2 == "Tonne":
            result = value * 0.000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Kilogram":
            result = value * 0.001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Gram":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Miligram":
            result = value * 1000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Microgram":
            result = value * 1000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Imperial Ton":
            result = value * 9.84265e-7
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Us ton":
            result = value * 0.0000011023
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Stone":
            result = value * 0.000157473
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Pound":
            result = value * 0.00220462
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Ounce":
            result = value * 0.035274
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Miligram
    elif unit1 == "Miligram":
        if unit2 == "Tonne":
            result = value * 1e-9
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Kilogram":
            result = value * 0.000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Gram":
            result = value * 0.001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Miligram":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Microgram":
            result = value * 1000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Imperial Ton":
            result = value * 9.84265e-10
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Us ton":
            result = value * 1.1023e-9
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Stone":
            result = value * 1.57473e-7
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Pound":
            result = value * 2.2046e-6
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Ounce":
            result = value * 3.5274e-5
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Microgram
    elif unit1 == "Microgram":
        if unit2 == "Tonne":
            result = value * 1e-12
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Kilogram":
            result = value * 1e-9
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Gram":
            result = value * 0.000001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Miligram":
            result = value * 0.001
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Microgram":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Imperial Ton":
            result = value * 9.84265e-13
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Us ton":
            result = value * 1.1023e-12
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Stone":
            result = value * 1.57473e-10
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Pound":
            result = value * 2.2046e-9
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Ounce":
            result = value * 3.5274e-8
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Imperial Ton
    elif unit1 == "Imperial Ton":
        if unit2 == "Tonne":
            result = value * 1.01605
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Kilogram":
            result = value * 1016.05
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Gram":
            result = value * 1016000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Miligram":
            result = value * 1016000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Microgram":
            result = value * 1016000000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Imperial Ton":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Us ton":
            result = value * 1.12
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Stone":
            result = value * 160
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Pound":
            result = value * 2240
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Ounce":
            result = value * 35840
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Us ton
    elif unit1 == "Us ton":
        if unit2 == "Tonne":
            result = value * 0.907185
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Kilogram":
            result = value * 907.185
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Gram":
            result = value * 907185
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Miligram":
            result = value * 907185000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Microgram":
            result = value * 907185000000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Imperial Ton":
            result = value * 0.892857
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Us ton":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Stone":
            result = value * 143
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Pound":
            result = value * 2000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Ounce":
            result = value * 32000
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Stone
    elif unit1 == "Stone":
        if unit2 == "Tonne":
            result = value * 0.00635029
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Kilogram":
            result = value * 6.35029
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Gram":
            result = value * 6350.29
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Miligram":
            result = value * 6350290
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Microgram":
            result = value * 6350290000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Imperial Ton":
            result = value * 0.00625
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Us ton":
            result = value * 0.007
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Stone":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Pound":
            result = value * 14
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Ounce":
            result = value * 224
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Pound
    elif unit1 == "Pound":
        if unit2 == "Tonne":
            result = value * 0.000453592
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Kilogram":
            result = value * 0.453592
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Gram":
            result = value * 453.592
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Miligram":
            result = value * 453592
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Microgram":
            result = value * 453592000
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Imperial Ton":
            result = value * 0.000446429
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Us ton":
            result = value * 0.0005
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Stone":
            result = value * 0.0714286
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Pound":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Ounce":
            result = value * 16
            st.write(f"{value} {unit1} = {result} {unit2}")
            # Ounce
    elif unit1 == "Ounce":
        if unit2 == "Tonne":
            result = value * 0.0000283495
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Kilogram":
            result = value * 0.0283495
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Gram":
            result = value * 28.3495
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Miligram":
            result = value * 28349.5
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Microgram":
            result = value * 28349500
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Imperial Ton":
            result = value * 2.7902e-5
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Us ton":
            result = value * 3.125e-5
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Stone":
            result = value * 0.00446429
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Pound":
            result = value * 0.0625
            st.write(f"{value} {unit1} = {result} {unit2}")
        elif unit2 == "Ounce":
            result = value * 1
            st.write(f"{value} {unit1} = {result} {unit2}")
             

