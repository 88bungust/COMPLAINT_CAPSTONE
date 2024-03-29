import pandas as pd
import matplotlib.pyplot as plt

complaints = pd.read_csv("COMPLAINTS SHEET 2.csv")

complaints2 = pd.read_csv("Copy of Complaints csv.csv")

complaints['Complaint ID'] = complaints['Complaint ID'].astype(str)
complaints2['Complaint ID'] = complaints2['Complaint ID'].astype(str)

complaints["Company_ID"] = complaints["Company"] + "_" + complaints["Complaint ID"]

complaints2["Company_ID"] = complaints2["Company"] + "_" + complaints2["Complaint ID"]

all_complaints = pd.merge(complaints2, complaints, how="left", on="Company_ID")

most_complaints_by_product = pd.DataFrame(all_complaints["Product"].value_counts().reset_index())

plt.barh(most_complaints_by_product["Product"],most_complaints_by_product["count"])
plt.title("Number of Complaints by Product")
plt.show()
# It appears that the number of complaints was the highest for Credit reporting, credit repair services, or other personal consumer reports.

all_complaints["Date received_x"] = pd.to_datetime(all_complaints["Date received_x"])

num_complaints_by_date = pd.DataFrame(all_complaints.groupby("Date received_x")["Complaint ID_x"].count().reset_index())

plt.figure(figsize=(20, 6))
plt.plot(num_complaints_by_date["Date received_x"],num_complaints_by_date["Complaint ID_x"])
plt.title("Number of Complaints by Date")
plt.show()
# It appears that the month of April has the most complaints per month.

product_responses = pd.DataFrame(all_complaints.groupby("Product")["Timely response?"].value_counts().reset_index())
product_responses_yes = product_responses[product_responses["Timely response?"] == "Yes"]

product_responses_no = product_responses[product_responses["Timely response?"] == "No"]

plt.barh(product_responses_yes["Product"], product_responses_yes["count"], label = 'Yes') 

plt.title("Number of Timely Responses per Product")
plt.show()
# It appears that the credit reporting has the most timely responses all of the other Products.