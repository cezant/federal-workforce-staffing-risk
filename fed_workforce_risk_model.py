#!/usr/bin/env python
# coding: utf-8

# ## First download the data from OPM
# 
# ## 1)Employment
# ## 2)Hires (Accession)
# ## 3)Separation

# Now that you have the data.  It needs to be delimited since all files have been txt.

# In[11]:


import pandas as pd

employment = pd.read_csv(f"E://program_analyst//employment.txt",  delimiter="|")

print(employment.head())
print(employment.columns)


# In[2]:


employment.head(5)


# In[5]:


hires = pd.read_csv(f"E://program_analyst//hires.txt",  delimiter="|")

print(hires.head())
print(hires.columns)


# In[9]:


separations = pd.read_csv(f"E://program_analyst//separations.txt",  delimiter="|")

print(separations.head())
print(separations.columns)


# ##  Afte all data has benn parsed.  Best to turn data to csv to clean and manage data.

# In[4]:


employment.to_csv(f"E://program_analyst//employment_clean.csv", index=False)


# In[10]:


separations.to_csv(f"E://program_analyst//separations_clean.csv", index=False)


# In[6]:


hires.to_csv(f"E://program_analyst//hires_clean.csv", index=False)


# ## Federal employment by agency.  Which agency has the largest

# In[12]:


agency_counts = employment.groupby("agency")["count"].sum()

print(agency_counts.sort_values(ascending=False))


# ## Now Analyse the workforce by age:

# In[14]:


age_risk = employment.groupby("age_bracket")["count"].sum()

print(age_risk)


# ## Ploting the retirement risk

# In[15]:


import matplotlib.pyplot as plt

age_risk.plot(kind="bar")

plt.title("Federal Workforce Age Distribution")
plt.xlabel("Age Bracket")
plt.ylabel("Employees")

plt.show()


# ## Agencies With Highest Retirement Risk

# In[16]:


retirement_risk = employment[employment["age_bracket"].isin(["55-59","60-64","65-69"])]

risk_summary = retirement_risk.groupby("agency")["count"].sum()

print(risk_summary.sort_values(ascending=False).head(10))


# ##  Federal Workforce Staffing Risk Index

# In[18]:


# Load dataset
employment = pd.read_csv(f"E://program_analyst//employment.txt", delimiter="|")

# Keep only columns we need
employment = employment[[
    "agency",
    "age_bracket",
    "length_of_service_years",
    "grade",
    "count"
]]

print(employment.head())


# # Identifying Retirement Risk employees
# 
# ### Looking at ages 55+ employees

# In[19]:


retirement_brackets = ["55-59", "60-64", "65-69", "70 AND OVER"]

retirement_data = employment[employment["age_bracket"].isin(retirement_brackets)]


# ## Calculating Workforce Totals by Agency

# In[20]:


total_workforce = employment.groupby("agency")["count"].sum().reset_index()

total_workforce.columns = ["agency", "total_employees"]


# ## Calculating Retirement Risk by Agency

# In[21]:


retirement_totals = retirement_data.groupby("agency")["count"].sum().reset_index()

retirement_totals.columns = ["agency", "retirement_risk_employees"]


# In[22]:


#Merging the data

risk_table = pd.merge(total_workforce, retirement_totals, on="agency", how="left")

risk_table = risk_table.fillna(0)


# ## Staffing Risk Index

# In[23]:


risk_table["retirement_ratio"] = (
    risk_table["retirement_risk_employees"] /
    risk_table["total_employees"]
)

risk_table["staffing_risk_index"] = risk_table["retirement_ratio"] * 100


# ## Now I can rank Agencies by Risk

# In[24]:


risk_ranked = risk_table.sort_values(
    by="staffing_risk_index",
    ascending=False
)

print(risk_ranked.head(10))


# This produces a Top 10 Agenecies with the Highest Workforce Risk 

# ## Risk Visualizaiton

# In[26]:


import matplotlib.pyplot as plt

top10 = risk_ranked.head(10)

plt.barh(top10["agency"], top10["staffing_risk_index"])

plt.xlabel("Staffing Risk Index")
plt.title("Federal Workforce Staffing Risk by Agency")

plt.gca().invert_yaxis()

plt.show()


# ## The specific agency I would like to highlight

# In[30]:


highlight_agency = "DEPARTMENT OF THE NAVY"
print(risk_ranked["agency"].unique())


# In[34]:


print(risk_ranked[risk_ranked["agency"].str.contains("NAVY")])


# In[31]:


import matplotlib.pyplot as plt

#creating the color logic
top10 = risk_ranked.head(10)

highlight_agency = "DEPARTMENT OF THE NAVY"

colors = [
    "red" if agency == highlight_agency else "steelblue"
    for agency in top10["agency"]
]


# # The chart below will show the Top 9 risk department and lastly the Department of the Navy Risk Rank.
# ## Federal Workforce Risk Chart (With Rank Numbers + Navy Forced)  Federal Workforce Risk Chart (boarder extension)

# In[53]:


import pandas as pd
import matplotlib.pyplot as plt

# =========================
# USER INPUT
# =========================
highlight_agency = "DEPARTMENT OF THE NAVY"

# =========================
# STEP 1 — Sort full risk table
# =========================
risk_ranked = risk_table.sort_values(
    by="staffing_risk_index",
    ascending=False
).reset_index(drop=True)

risk_ranked["federal_rank"] = risk_ranked.index + 1

# =========================
# STEP 2 — Extract Navy TRUE rank
# =========================
navy_row = risk_ranked[
    risk_ranked["agency"].str.upper().str.contains("NAVY")
]

navy_true_rank = navy_row["federal_rank"].values[0]

# =========================
# STEP 3 — Top 9 highest risk
# =========================
top9 = risk_ranked.head(9)

# =========================
# STEP 4 — Combine Top9 + Navy
# =========================
chart_df = pd.concat([top9, navy_row])
chart_df = chart_df.drop_duplicates(subset="agency")

# =========================
# STEP 5 — Sort for plotting
# =========================
chart_df = chart_df.sort_values(
    by="staffing_risk_index",
    ascending=False
).reset_index(drop=True)

chart_df["chart_rank"] = chart_df.index + 1

# =========================
# STEP 6 — Colors
# =========================
colors = [
    "red" if highlight_agency in agency else "steelblue"
    for agency in chart_df["agency"]
]

# =========================
# STEP 7 — Plot
# =========================
# CREATE FIGURE OBJECT (IMPORTANT)
fig, ax = plt.subplots(figsize=(12,7))

plt.barh(
    chart_df["agency"],
    chart_df["staffing_risk_index"],
    color=colors
)

plt.xlabel("Staffing Risk Index")
plt.title("Federal Workforce Staffing Risk (Top Agencies 1-9 + Navy Focus)")
plt.gca().invert_yaxis()

# =========================
# STEP 8 — Extend border
# =========================
max_value = chart_df["staffing_risk_index"].max()
plt.xlim(0, max_value * 1.4)

# =========================
# STEP 9 — Chart rank labels (EXCLUDE NAVY)
# =========================
for i in range(len(chart_df)):
    agency = chart_df["agency"].iloc[i]

    if highlight_agency not in agency:
        plt.text(
            chart_df["staffing_risk_index"].iloc[i] + max_value * 0.02,
            i,
            f"Chart Rank {chart_df['chart_rank'].iloc[i]}",
            va="center",
            fontsize=9
        )

# =========================
# STEP 10 — Navy TRUE rank annotation ONLY
# =========================
for i, agency in enumerate(chart_df["agency"]):
    if highlight_agency in agency:
        plt.text(
            chart_df["staffing_risk_index"].iloc[i] + max_value * 0.02,
            i,
            f"NAVY TRUE FEDERAL RANK: {navy_true_rank}",
            color="red",
            fontweight="bold",
            va="center",
            fontsize=11
        )


# SAVE BEFORE SHOW (CRITICAL)
fig.savefig(
    f"E://Federal-Workforce-Staffing-Risk-Index//output//staffing_risk_chart.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


# In[ ]:





# ## Automation of report to CSV

# In[46]:


risk_ranked.to_csv(f"E://program_analyst//federal_staffing_risk_report.csv", index=False)


# In[54]:


risk_ranked.to_csv(f"E://Federal-Workforce-Staffing-Risk-Index//output//staffing_risk_table.csv", index=False)


# In[ ]:




