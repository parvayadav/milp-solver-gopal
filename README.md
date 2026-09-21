# go, pal! — Team Capacity Model

*for companies that wanna go somewhere fast*

How go, pal! allocates its own team — Parva, Abhimanyu, Vinayak, and Puneet — across client engagements to maximize contribution margin. Built strictly in Python with an interactive Streamlit GUI, solved with a Mixed-Integer Linear Programming (MILP) model via IBM ILOG CPLEX.

---

## What's in here

1. **Mathematical Formulation**: A complete MILP model with decision variables for allocation hours ($x_{ij}$), binary team assignment indicators ($y_{ij}$), and binary Principal PM designations ($p_{ij}$), across 8 constraint sets.
2. **Interactive Streamlit GUI**:
   - Edit every parameter live — client demand, expertise minimums, billing rates, delivery costs, team capacities.
   - Solve the model with **"Solve Allocation Model"**.
   - Read results in dedicated tabs: KPI summary, client allocation matrix, team slack/utilization, and interactive Plotly charts.
3. **Executive Abstract**: A concise write-up covering context, objectives, key assumptions, parameters, modeling approach, solver choice, and GUI plan.

---

## 🚀 Quickstart (Running Locally)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit Application
```bash
streamlit run app.py
```
The application will launch automatically in your browser (typically at `http://localhost:8501`).

---

## 📁 Repository Structure

```
├── app.py              # Main Streamlit GUI with 4 interactive tabs and KPI dashboards
├── solver.py           # MILP optimization engine (Exclusively IBM ILOG CPLEX via docplex)
├── model_data.py       # Default team, client, and rate data (Appendix A, B, C)
├── assets/             # go, pal! logo (gopal-logo.png)
├── requirements.txt    # Python package dependencies (Streamlit, CPLEX, DOcplex, Pandas, Plotly)
└── README.md           # Project documentation and mathematical formulation
```

---

## 📐 Mathematical Formulation Summary

- **Sets**: $i \in \{M, A, T, AI\}$ (Consultants); $j \in \{1, 2, \dots, 12\}$ (Clients).
- **Decision Variables**:
  - $x_{ij} \ge 0$: Hours consultant $i$ allocates to client $j$.
  - $y_{ij} \in \{0, 1\}$: Binary indicator if consultant $i$ is assigned to client $j$.
  - $p_{ij} \in \{0, 1\}$: Binary indicator if consultant $i$ is Principal PM for client $j$.
- **Objective Function**:
  $$\max Z = \sum_{i} \sum_{j} (R_{ij} - C_{ij}) x_{ij}$$
- **Constraints**:
  1. $\sum_j x_{ij} \le \text{Cap}_i \quad \forall i$ (Consultant Capacity, default 40h)
  2. $\sum_i x_{ij} = H_j \quad \forall j$ (Client Demand Fulfillment)
  3. $x_{ij} \ge S_{ij} \quad \forall i, j$ (Mandatory Expertise Minimums)
  4. $x_{ij} \le H_j y_{ij} \quad \forall i, j$ (Assignment Linkage via Big-M)
  5. $\sum_i p_{ij} = 1 \quad \forall j$ (Exactly One Principal PM per Client)
  6. $p_{ij} \le y_{ij} \quad \forall i, j$ (PM Must Work on Project)
  7. $x_{ij} \ge PM_j \cdot p_{ij} \quad \forall i, j$ (PM Minimum Hours Contribution)
  8. $x_{ij} \ge 0, \; y_{ij}, p_{ij} \in \{0, 1\} \quad \forall i, j$ (Variable Domains)

---

## 👥 The Team

| Key | Name | Role |
|---|---|---|
| M | Parva Yadav | CEO & Managing Director — Marketing Technology |
| A | Abhimanyu Vyas | Strategy & Performance Media — Advertising |
| T | Vinayak Vishvakarma | Whole-time Director, Tech & Engineering — Technology |
| AI | Puneet Agarwal | Engagement Lead, Research & AI — Artificial Intelligence |

## 🔒 Axestrack's Exclusivity Clause

Axestrack holds a hard lock on Parva's (M's) entire 40h weekly capacity — modeled as a minimum-hours constraint ($S_{M,\text{Axestrack}} = \text{Cap}_M$) rather than a bespoke constraint type. That forces $x_{M,\text{Axestrack}} = \text{Cap}_M$ exactly, leaving zero M-hours for any other client. Every other client's demand has to be satisfiable from Advertising, Technology, and AI capacity alone — by default, it is; push the numbers further and the model will correctly report infeasible, flagged clearly as the exclusivity clause binding rather than a generic solver error.

---

## 📊 Benchmark Optimal Results

For the baseline problem parameters (12 clients, including Axestrack's lock on Parva/M):
- **Optimal Contribution Margin**: **$579,650.00**
- **Total Firm Revenue**: **$1,054,000.00**
- **Total Delivery Cost**: **$474,350.00**
- **Profit Margin**: **55.0%**
- **Capacity Utilization**:
  - Parva Yadav (M): 40.0 / 40.0 hours (0 hours slack — fully committed to Axestrack)
  - Abhimanyu Vyas (A): 38.0 / 40.0 hours (2 hours slack)
  - Vinayak Vishvakarma (T): 40.0 / 40.0 hours (100% utilized)
  - Puneet Agarwal (AI): 40.0 / 40.0 hours (100% utilized)
- **Principal PM Distribution**:
  - Parva Yadav (M): 1 project (Axestrack)
  - Abhimanyu Vyas (A): 5 projects (HDFC, IOB, FnP, Nykaa, Masaba)
  - Vinayak Vishvakarma (T): 4 projects (Disney, Kotak, Wildcraft, Coca-Cola)
  - Puneet Agarwal (AI): 2 projects (KFC, Woodland)
