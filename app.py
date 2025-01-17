import streamlit as st
from model import *


def main():

    st.title("Expresso Churn Prediction")

    user_id = st.selectbox("Insert Your ID", (categorical_columns['user_id']))
    REGION = st.selectbox("Insert Your Region", (categorical_columns['REGION']))
    TENURE = st.selectbox("Insert Your Subscription", (categorical_columns['TENURE']))
    MONTANT = st.number_input("Insert the number", value=None)
    FREQUENCE_RECH = st.number_input("Insert the Frequency Rech number", value=None)
    REVENUE = st.number_input("Insert the  Revenue number", value=None)
    ARPU_SEGMENT = st.number_input("Insert the Segement number", value=None)
    FREQUENCE = st.number_input("Insert the  Frequency number", value=None)
    DATA_VOLUME = st.number_input("Insert the  Data Volume number", value=None)
    ON_NET = st.number_input("Insert the On net number", value=None)
    ORANGE = st.number_input("Insert the orange number", value=None)
    TIGO = st.number_input("Insert the tigo number", value=None)
    ZONE1 = st.number_input("Insert the zone1 number", value=None)
    ZONE2 = st.number_input("Insert the zone2 number", value=None)
    MRG = st.text_input("Insert No into the box")#, value=None)
    REGULARITY = st.number_input("Insert the regularity number", value=None)
    TOP_PACK = st.selectbox("Insert Your Subscription", (categorical_columns['TOP_PACK']))
    FREQ_TOP_PACK = st.number_input("Insert the frquency pack number", value=None)
    
    
    CHURN = ""

    if st.button("Predict"):

        CHURN = prediction([
            user_id, REGION, TENURE, MONTANT, FREQUENCE_RECH, REVENUE,
       ARPU_SEGMENT, FREQUENCE, DATA_VOLUME, ON_NET, ORANGE, TIGO,
       ZONE1, ZONE2, MRG, REGULARITY, TOP_PACK, FREQ_TOP_PACK
        ]) 
    st.success(CHURN)




if __name__ == "__main__":
    main()