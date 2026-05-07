import streamlit as st

st.title("Logistic Regression for Churn Prediction")

gender = st.selectbox("Select Gender:", options=["Male","Female","Other"])

age = st.selectbox("Select your age", list(range(1, 91)))

st.write("Your age is:", age)

region_circle = st.selectbox("Select Region Circle:", options=["East","West","North","South","Metro"])

connection_type = st.selectbox("Select Connection Type:", options=["4G","5G","Fiber Home BroadBand"])

plan_type = st.selectbox("Plan Type:", options=["Post-Paid","Pre-Paid"])

contract_type = st.selectbox("Contract Type:", options=["1 Year","2 Year","Month to Month","No Contract"])

tenure_months = st.selectbox("Tenure Months", list(range(1, 120)))

st.write("Tenure Months:", tenure_months)

based_plan_category = st.selectbox("Based plan Category:", options=["PostPaid Gold","Postpaid Platinum","Postpaid Silver","Prepaid Mini","Prepaid Regular","Prepaid Unlimiled"])

monthly_charges = st.selectbox("Monthly_Charges", list(range(99, 1550)))

st.write("Monthly_Charges:", monthly_charges)

total_charges = st.selectbox("Total_Charges", list(range(160, 17000)))

st.write("Total_Charges:", total_charges)

# Behaviourial Features

avg_data_speed_mbps = st.selectbox("Avg_Data_Speed_Mbps", list(range(1, 40)))

st.write("Avg_Data_Speed_Mbps:", avg_data_speed_mbps)

avg_voice_mins_month = st.selectbox("Avg_Voice_Mins_Month", list(range(30, 1850)))

st.write("Avg_Voice_Mins_Month:", avg_voice_mins_month)

dropped_call_rate = st.selectbox("Dropped_Call_Rate", list(range(0, 5)))

st.write("Droped_Call_Rate:", dropped_call_rate)

network_issues_3m = st.selectbox("Network_Issues_3m", list(range(160, 17000)))

st.write("Network_Issues_3m:", network_issues_3m)

num_complaints_3m = st.selectbox("Num_Complaints_3m", list(range(0, 4)))

st.write("Num_Complaints_3m:", num_complaints_3m)

num_complaints_12m = st.selectbox("Num_Complaints_12m", list(range(0, 6)))

st.write("Num_Complaints_12m:", num_complaints_12m)

# Binary Features

is_family_plan = st.selectbox("Is_Family_Plan:", options=[0,1,])

is_multi_service = st.selectbox("Is_Multi_Service:", options=[0,1,])

button = st.button("Done")
if button:
    st.markdown(f"""
Gender:{gender}
Age:{age}
Region Cirle:{region_circle}
Connection Type:{connection_type}
Plan Type:{plan_type}
Contract Type:{contract_type}
Tenure Months:{tenure_months}
Based Paln Category:{based_plan_category}
Monthly_Charges:{monthly_charges}
Total_Charges:{total_charges}
Avg_Data_Spedd_Mbps:{avg_data_speed_mbps}
Avg_Voice_Mins_Month:{avg_voice_mins_month}
Dropped_Call_Rate:{dropped_call_rate}
Network_Issues_3m:{network_issues_3m}
Num_Complaints_3m:{num_complaints_3m}
Num_Complaints_12m:{num_complaints_12m}
Is_family_Plan:{is_family_plan}
Is_Multi_Service:{is_multi_service}""")