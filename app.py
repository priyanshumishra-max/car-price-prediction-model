import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model = pk.load(open('model.pkl', 'rb'))

st.header("Car Price Prediction",
          icon="🚗"
)

cars_data = pd.read_csv("Cardetails.csv")
def get_brand_name(car_name):
    car_name = car_name.split(" ")[0]
    return car_name.strip()
cars_data["brand"] = cars_data["name"].apply(get_brand_name)

brand_map = {
    'Maruti': 1, 'Skoda': 2, 'Honda': 3, 'Hyundai': 4, 'Toyota': 5,
    'Ford': 6, 'Renault': 7, 'Mahindra': 8, 'Tata': 9, 'Chevrolet': 10,
    'Datsun': 11, 'Jeep': 12, 'Mercedes-Benz': 13, 'Mitsubishi': 14,
    'Audi': 15, 'Volkswagen': 16, 'BMW': 17, 'Nissan': 18, 'Lexus': 19,
    'Jaguar': 20, 'Land': 21, 'MG': 22, 'Volvo': 23, 'Daewoo': 24,
    'Kia': 25, 'Fiat': 26, 'Force': 27, 'Ambassador': 28, 'Ashok': 29,
    'Isuzu': 30, 'Opel': 31
}
fuel_map = {'Diesel': 1, 'Petrol': 2, 'LPG': 3, 'CNG': 4}
seller_type_map = {'Individual': 1, 'Dealer': 2, 'Trustmark Dealer': 3}
transmission_map = {'Manual': 1, 'Automatic': 2}
owner_map = {
    'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3,
    'Fourth & Above Owner': 4, 'Test Drive Car': 5
}

name = st.selectbox("Select Car Brand", cars_data["name"].unique())
year = st.slider("Car Manufactured Year ", 1994, 2024)
km_driven = st.slider("Car Kms Driven", 0, 200000)
fuel = st.selectbox("Car Fuel Type", cars_data["fuel"].unique())

seller_type = st.selectbox("seller type", cars_data["seller_type"].unique())
transmission = st.selectbox("transmission type", cars_data["transmission"].unique())
owner = st.selectbox("Owner Type", cars_data["owner"].unique())
seats = st.slider("Number of Seats", 1, 10)

mileage = st.slider("Car Mileage", 0, 50)
max_power = st.slider("max power", 0, 500)
engine = st.slider("Engine CC", 0, 5000)



if st.button("Predict Price"):
    input_data_model = pd.DataFrame(
        [[ brand_map.get(name, 1),
            year,
            km_driven,
            fuel_map.get(fuel, 1),
            seller_type_map.get(seller_type, 1),
            transmission_map.get(transmission, 1),
            owner_map.get(owner, 1),
            mileage,
            engine,
            max_power,
            seats
        ]],
        columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage', 'engine', 'max_power', 'seats']
    )

    # Make prediction
    car_price = model.predict(input_data_model)
    st.success(f"Estimated Car Price: ₹{car_price[0]:,.2f}")