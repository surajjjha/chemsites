import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))


def predict_forest(Distancetoroad,Factorydensity,distancetonearesetwatersource,
                   NumberofWatersources,Avgdistancetowatersource,Distancetocity,
                   Distancetonearestdumpsite):
    input=np.array([[Distancetoroad,Factorydensity,distancetonearesetwatersource,
                   NumberofWatersources,Avgdistancetowatersource,Distancetocity,
                   Distancetonearestdumpsite]]).astype(np.float64)
    prediction=model.predict_proba(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("CHEMSITES")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">CHEMSITES </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    Distancetoroad = st.text_input("(Distance to road(m)","Type Here")
    Factorydensity = st.text_input("Factory density","Type Here")
    distancetonearesetwatersource = st.text_input("distance to neareset water source(km)","Type Here")
    NumberofWatersources = st.text_input(" Number of Water sources","Type Here")
    Avgdistancetowatersource = st.text_input(" Avg distance to water source(km)","Type Here")
    Distancetocity = st.text_input(" Distance to city(km)","Type Here")
    Distancetonearestdumpsite = st.text_input(" Distance to nearest dump site(km)","Type Here")
    safe_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> Your Location is safe</h2>
       </div>
    """
    danger_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> Your Location is in danger</h2>
       </div>
    """

    if st.button("Predict"):
        output=predict_forest(Distancetoroad,Factorydensity,distancetonearesetwatersource,
                   NumberofWatersources,Avgdistancetowatersource,Distancetocity,
                   Distancetonearestdumpsite)
        st.success('The probability of being a chemical dumpsite {}'.format(output))

        if output == "yes":
            st.markdown(danger_html,unsafe_allow_html=True)
        elif output =="no":
            st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()