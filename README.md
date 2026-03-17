# Federal Workforce Staffing Risk Index

### Workforce Analytics Project (Federal Program Analysis)

## Project Overview

This project develops a **Federal Workforce Staffing Risk Index** using workforce data from the U.S. Office of Personnel Management (OPM).

The objective is to analyze workforce demographics and identify federal agencies at risk of staffing shortages due to retirement trends and workforce composition.

---

## Purpose

Federal agencies must anticipate workforce shortages to ensure mission readiness and operational effectiveness.

This project demonstrates:

* Workforce trend analysis
* Retirement risk assessment
* Staffing risk modeling
* Executive-level data visualization
* Program evaluation support

The model produces a **risk ranking across federal agencies** and highlights the relative position of the Department of the Navy.

---

## Data Source

Data used in this project comes from:

U.S. Office of Personnel Management (OPM)
Federal Workforce Data Portal
https://data.opm.gov

Dataset utilized:

* Federal Employment Cube (workforce demographic snapshot)

---

## Methodology

### Workforce Risk Model

The Staffing Risk Index is calculated as:

Staffing Risk Index =
(Number of Employees Age 55+) / (Total Workforce)

This approach reflects common workforce planning methods used in federal manpower analysis.

### Analytical Steps

1. Load and clean federal workforce data
2. Aggregate workforce counts by agency
3. Identify retirement-risk population (age 55+)
4. Compute retirement risk ratio
5. Rank agencies by staffing risk
6. Generate executive visualization
7. Force-include Department of the Navy for leadership context

---

## Key Features

* Federal workforce demographic analysis
* Retirement risk modeling
* Agency risk ranking system
* Executive briefing visualization
* Navy workforce contextual analysis
* Automated reporting output

---

## Visualization Example

The chart displays:

* Top federal agencies by workforce staffing risk
* Department of the Navy highlighted
* True federal-wide ranking of Navy workforce risk
* Executive-style briefing presentation

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Federal Open Data (OPM)

---

## How to Run This Project

### Step 1 — Install Required Packages

```bash
pip install pandas matplotlib
```

### Step 2 — Download Dataset

Download the Federal Employment dataset from:

https://data.opm.gov

Save as:

employment.txt

### Step 3 — Run Analysis Script

```bash
python workforce_risk_model.py
```

---

## Example Output

* Federal Staffing Risk Ranking Table
* Executive Workforce Risk Chart
* Navy True Federal Rank Visualization

---

## Project Relevance to Federal Program Analysis

This project demonstrates competencies aligned with federal program analyst roles:

* Program evaluation
* Workforce planning
* Trend analysis
* Decision support analytics
* Data-driven reporting
* Strategic workforce insight

---

## Future Enhancements

Planned extensions include:

* Occupational series staffing risk model
* Department of Defense workforce subset analysis
* Supervisory workforce risk assessment
* Predictive workforce shortage modeling
* Interactive dashboard (Power BI / Plotly)

---

## Author

Cesar
Federal Workforce Analytics Portfolio Project

---

## License

This project uses publicly available federal workforce data and is intended for educational and professional portfolio use.
