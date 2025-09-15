import streamlit as st

# ---- Calibration chart ----
calibration = {
    "front": {
        129: 500, 252: 1000, 364: 1500, 470: 2000,
        578: 2500, 681: 3000, 785: 3500, 886: 4000,
        990: 4500, 1093: 5000, 1198: 5500, 1302: 6000,
        1408: 6500, 1516: 7000, 1630: 7500, 1755: 8000
    },
    "middle": {
        114: 500, 235: 1000, 346: 1500, 455: 2000,
        560: 2500, 665: 3000, 768: 3500, 870: 4000,
        972: 4500, 1073: 5000, 1177: 5500, 1286: 6000,
        1388: 6500, 1495: 7000, 1609: 7500, 1735: 8000
    },
    "rear": {
        127: 500, 249: 1000, 362: 1500, 469: 2000,
        576: 2500, 679: 3000, 783: 3500, 884: 4000,
        989: 4500, 1092: 5000, 1196: 5500, 1301: 6000,
        1407: 6500, 1517: 7000, 1633: 7500, 1758: 8000
    }
}

def get_volume(chamber, dip):
    chamber = chamber.strip().lower()
    data = calibration[chamber]
    dips = sorted(data.keys())

    if dip in data:
        return data[dip]

    if dip < dips[0] or dip > dips[-1]:
        return None

    for i in range(len(dips) - 1):
        low_dip, high_dip = dips[i], dips[i+1]
        if low_dip <= dip <= high_dip:
            low_vol, high_vol = data[low_dip], data[high_dip]
            return round(low_vol + (dip - low_dip) * (high_vol - low_vol) / (high_dip - low_dip), 2)

    return None


st.title("HFO Measuring Server")
st.markdown("###### Powered by Sifat") 
st.markdown("### Lorry Number: Dhaka Metro Dha-11-02-72") 

chamber = st.selectbox("Select Chamber", ["Front", "Middle", "Rear"])
dip = st.number_input("Enter Dip (mm)", min_value=100, max_value=2000, step=1)

if st.button("Calculate Volume"):
    vol = get_volume(chamber, int(dip))
    if vol:
        st.success(f"{chamber} chamber at {int(dip)} mm = {vol} Liters")
    else:
        st.error("Dip out of range!")