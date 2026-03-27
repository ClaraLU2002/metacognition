import pandas as pd
import streamlit as st

st.set_page_config(page_title="Portfolio Optimization", layout="wide")
st.title("Portfolio Optimization")

st.markdown(
    """
    <style>
    div[data-testid="stExpander"] summary p {
        font-size: 1.05rem;
        font-weight: 700;
    }

    .welcome-hero {
        background: linear-gradient(135deg, #eef6ff 0%, #f7fbff 100%);
        border: 1px solid #d6e6ff;
        border-radius: 20px;
        padding: 28px 24px;
        margin-bottom: 18px;
    }

    .welcome-title {
        font-size: 1.9rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-bottom: 0.5rem;
    }

    .welcome-subtitle {
        font-size: 1rem;
        color: #475569;
        line-height: 1.7;
    }

    .welcome-shell {
        background: linear-gradient(135deg, #f8fbff 0%, #eef5ff 100%);
        border: 1px solid #dbeafe;
        border-radius: 22px;
        padding: 24px;
        margin-bottom: 18px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.04);
    }

    .guide-card {
        background: linear-gradient(135deg, #f8fbff 0%, #eef5ff 100%);
        border: 1px solid #dbeafe;
        border-radius: 22px;
        padding: 24px;
        margin-bottom: 18px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.04);
    }

    .second-note-box {
    background: linear-gradient(135deg, #eef8ff 0%, #f7fbff 100%);
    border: 1px solid #93c5fd;
    border-left: 8px solid #2563eb;
    border-radius: 18px;
    padding: 20px 22px;
    margin-top: 10px;
    margin-bottom: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
}

.second-note-title {
    font-size: 1.02rem;
    font-weight: 800;
    color: #1d4ed8;
    margin-bottom: 10px;
}

.second-note-text {
    font-size: 0.98rem;
    line-height: 1.8;
    color: #1e3a8a;
}

    .guide-title {
        font-size: 1.8rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-bottom: 0.6rem;
    }

    .guide-text {
        font-size: 1rem;
        line-height: 1.8;
        color: #334155;
    }

    .chat-wrap {
        display: flex;
        flex-direction: column;
        gap: 12px;
        margin-top: 12px;
        margin-bottom: 10px;
    }

    .teacher-bubble {
        background: #f3f8ff;
        border-left: 5px solid #5b8def;
        padding: 14px 16px;
        border-radius: 16px 16px 16px 6px;
        color: #1e293b;
        line-height: 1.7;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }

    .student-bubble {
        background: #f8fafc;
        border-left: 5px solid #cbd5e1;
        padding: 14px 16px;
        border-radius: 16px 16px 6px 16px;
        color: #334155;
        line-height: 1.7;
        margin-left: 28px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }

    .guide-row {
        display: flex;
        align-items: flex-start;
        gap: 16px;
        margin-top: 16px;
        margin-bottom: 16px;
    }

    .notice-box {
    background: linear-gradient(135deg, #fff7ed 0%, #fffaf3 100%);
    border: 1px solid #fdba74;
    border-left: 8px solid #f97316;
    border-radius: 18px;
    padding: 20px 22px;
    margin-top: 8px;
    margin-bottom: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
}

.notice-title {
    font-size: 1.02rem;
    font-weight: 800;
    color: #9a3412;
    margin-bottom: 10px;
}

.notice-text {
    font-size: 0.98rem;
    line-height: 1.8;
    color: #7c2d12;
}

    .photo-frame {
        background: white;
        border: 1px solid #dbeafe;
        border-radius: 18px;
        padding: 10px;
        text-align: center;
        box-shadow: 0 3px 10px rgba(0,0,0,0.03);
    }

    .photo-box {
        background: white;
        border: 1px solid #dbeafe;
        border-radius: 18px;
        padding: 10px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.03);
        text-align: center;
    }

    .speech-box {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 18px 20px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.03);
        color: #334155;
        line-height: 1.8;
        font-size: 1rem;
        min-height: 110px;
        display: flex;
        align-items: center;
    }

    .bubble-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 18px 20px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.03);
        margin-bottom: 14px;
    }

    .goal-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }

    .goal-title {
        font-size: 1rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 6px;
    }

    .goal-text {
        color: #475569;
        line-height: 1.6;
        font-size: 0.96rem;
    }

    .soft-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 18px 20px;
        margin-bottom: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }

    .soft-title {
        font-size: 1.02rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 8px;
    }

    .soft-text {
        color: #475569;
        line-height: 1.7;
        font-size: 0.96rem;
    }

    .problem-card {
        background: #ffffff;
        border: 1px solid #dbeafe;
        border-radius: 16px;
        padding: 16px 18px;
        height: 100%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }

    .problem-title {
        font-size: 1.05rem;
        font-weight: 800;
        color: #1d4ed8;
        margin-bottom: 8px;
    }

    .problem-text {
        color: #475569;
        line-height: 1.6;
        font-size: 0.95rem;
    }

    .role-example-box {
    background: linear-gradient(135deg, #f5f3ff 0%, #faf7ff 100%);
    border: 1px solid #c4b5fd;
    border-left: 8px solid #8b5cf6;
    border-radius: 18px;
    padding: 18px 20px;
    margin-top: 10px;
    margin-bottom: 12px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.03);
}

.role-example-title {
    font-size: 0.98rem;
    font-weight: 800;
    color: #5b21b6;
    margin-bottom: 8px;
}

.role-example-text {
    font-size: 0.96rem;
    line-height: 1.8;
    color: #4c1d95;
}

    .section-soft-title {
        font-size: 1.15rem;
        font-weight: 800;
        color: #0f172a;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    .mini-note {
        background: #fffbea;
        border: 1px solid #fde68a;
        border-radius: 14px;
        padding: 14px 16px;
        color: #854d0e;
        margin-top: 10px;
        margin-bottom: 16px;
    }

    .start-box {
        background: linear-gradient(135deg, #effcf6 0%, #f7fffb 100%);
        border: 1px solid #bbf7d0;
        border-radius: 18px;
        padding: 20px 18px;
        margin-top: 18px;
        margin-bottom: 6px;
    }

    .start-panel {
        background: linear-gradient(135deg, #effcf6 0%, #f7fffb 100%);
        border: 1px solid #bbf7d0;
        border-radius: 18px;
        padding: 18px 20px;
        margin-top: 16px;
        color: #14532d;
    }

    .center-note {
        text-align: center;
        color: #64748b;
        font-size: 0.9rem;
        margin-top: 6px;
    }

    .final-guide-box {
    background: linear-gradient(135deg, #f0fdf4 0%, #ecfeff 100%);
    border: 1px solid #bbf7d0;
    border-left: 8px solid #22c55e;
    border-radius: 20px;
    padding: 22px 24px;
    margin-top: 10px;
    margin-bottom: 16px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.04);
}

.final-guide-label {
    font-size: 0.82rem;
    font-weight: 800;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #15803d;
    margin-bottom: 8px;
}

.final-guide-text {
    font-size: 1.08rem;
    line-height: 1.8;
    color: #14532d;
    font-weight: 500;
}
    """,
    unsafe_allow_html=True,
)


# --------------------------
# Constants
# --------------------------
PAGE_NAME = "Portfolio Optimization"
YES_NO_OPTIONS = ["No", "Yes"]
LIKERT_OPTIONS = [1, 2, 3, 4, 5]

REVISIT_ITEMS = [
    "I can identify the key elements of a portfolio optimization problem.",
    "I can break the optimization task into smaller and manageable steps.",
    "I can decide when AI support is useful and when my own judgment is more important.",
    "I can revise my model or code based on whether the result is logically correct.",
    "I am aware of the strategies I use when solving optimization problems.",
    "I can judge whether a solution is mathematically and computationally reasonable.",
    "I reflect on whether my final interpretation matches the optimization result.",
    "I can improve my work by reviewing and refining it step by step.",
]

TASK_HINTS = {
    "plan": """A possible way to continue dividing the work:


- Task 2: Compute returns and expected returns  
Convert stock prices into daily returns.  
Then compute average daily returns and yearly returns.  
These values will later represent expected returns in the optimization model.

- Task 3: Measure risk using variance and covariance  
Calculate the variance of each stock and the covariance matrix.  
This step defines how risk is represented in the portfolio optimization model.

- Task 4: Formulate and solve the optimization model  
Use expected returns and covariance matrix to build the portfolio optimization model.  
Define decision variables, objective function, and constraints.  
Solve the model using an optimization solver.

- Task 5: Analyze and interpret the results  
Examine the optimal portfolio weights.  
Check whether the solution is diversified.  
Interpret the trade-off between return and risk.  
Present the results clearly.
""",
    1: """Hint for Task 1: Pull the stock price data from Yahoo Finance

**Task focus:**  
Use the Markowitz model for portfolio optimization. The first step is to collect historical stock price data from Yahoo Finance. In the original notebook, the data source is the **Adjusted Close price**, covering the period from **1 January 2010 to 31 December 2017**, for the following stocks:  
`['HSBC', 'JPM', 'AAPL', 'WMT', 'AMZN', 'MSFT']`. :contentReference[oaicite:2]{index=2}

**What you should do in this task:**  
1. Define the list of stock tickers and the date range.  
2. Download the adjusted closing prices for all selected stocks.  
3. Organize the result into a clean table where:

- rows represent trading dates,
- columns represent stocks,
- values are adjusted closing prices.

4. Check whether the downloaded dataset has missing values or inconsistent dates.
5. Display the first few rows so that you can verify the data was loaded correctly.
6. If requested, normalize the price series to compare the relative movement of different stocks over time. This helps visualize how the assets evolve on a common scale before any return calculation. :contentReference[oaicite:3]{index=3}

**Suggested code structure:**
```python
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ['HSBC', 'JPM', 'AAPL', 'WMT', 'AMZN', 'MSFT']
start_date = '2010-01-01'
end_date = '2017-12-31'

def load_price_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

prices = load_price_data(tickers, start_date, end_date)
print(prices.head())
print(prices.isna().sum())

# optional: normalized price plot
normalized_prices = prices / prices.iloc[0]
normalized_prices.plot(figsize=(10, 6))
plt.title('Normalized Stock Prices')
plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.show()
```
You should pay attention to:

- Make sure you are using Adj Close, not only Close.
- Ensure all selected stocks are aligned on the same trading dates.
- Keep the output clean and readable, because this table will be reused in later tasks.
""",
    2: """Hint for Task 2: Calculate daily returns and average returns

**Task focus:**  
After collecting the stock price data, the next step is to compute stock returns.  
In portfolio optimization, expected return is a key input. Therefore, you need to convert price data into return data before building the optimization model.

In this step, you should compute:

- Daily returns  
- Average daily returns  
- Average yearly returns  

**What you should do in this task**

1. Start from the adjusted closing price data obtained

2. Compute daily returns  

3. Remove missing values  
After computing returns, the first row will contain NaN values.  
Remove those rows before further analysis.

4. Compute average daily return for each stock

5. Convert daily return into yearly return  

6. Display results clearly  
Print:

- First few rows of return table  
- Average daily return  
- Average yearly return  

**Suggested code structure**

```python
import numpy as np
import pandas as pd

def compute_log_returns(prices):
    log_returns = np.log(prices / prices.shift(1))
    return log_returns.dropna()

returns = compute_log_returns(prices)

# average daily return
avg_daily_return = returns.mean()

# average yearly return
avg_yearly_return = avg_daily_return * 252

print("Daily returns:")
print(returns.head())

print("\nAverage daily return:")
print(avg_daily_return)

print("\nAverage yearly return:")
print(avg_yearly_return)

""",
    3: """Hint for Task 3: Calculate variance, covariance, and correlation

After computing returns in Task 2, the next step is to measure risk.  
In portfolio optimization, risk is not only determined by how much each stock fluctuates individually, but also by how different stocks move together.

You may find it helpful to think about:

- why variance matters for a single asset
- why covariance matters for a portfolio
- what the covariance matrix should look like
- how these quantities may be used later in the model

You can try to:

- start from the return table
- compute variance for each asset
- compute the covariance matrix
- check whether the dimensions and asset order are correct

Example code structure:

```python
asset_variances = returns.var()
cov_matrix = returns.cov()

print(asset_variances)
print(cov_matrix)


""",
    4: """Hint for Task 4: Formulate and Solve the Optimization Model

At this stage, focus on turning your financial problem into an optimization model and solving it in code.

You may find it helpful to think about:

- what the decision variables represent
- what objective should be optimized
- what constraints are needed
- how to organize the model clearly in code

You can try to:

- define portfolio weights as decision variables
- write the objective function
- add constraints such as budget constraint
- solve the model
- check the solver status before reading the solution

Example code structure:

```python
import gurobipy as gp
from gurobipy import GRB

n = len(mu)
model = gp.Model("portfolio")

w = model.addVars(n, lb=0, ub=1, name="w")

model.addConstr(gp.quicksum(w[i] for i in range(n)) == 1)

portfolio_return = gp.quicksum(mu[i] * w[i] for i in range(n))
portfolio_risk = gp.quicksum(Sigma[i][j] * w[i] * w[j] for i in range(n) for j in range(n))

model.setObjective(portfolio_risk, GRB.MINIMIZE)
model.optimize()
```
After solving, remember to check whether the model is optimal before extracting the weights.
""",
    5: """Hint for Task 5: Check and Interpret the Solution

At this stage, focus on checking whether the solution is correct and explaining what it means.

You may find it helpful to think about:

- whether the solver found an optimal solution
- whether the weights satisfy the constraints
- whether the weights look reasonable
- what the final portfolio says about return and risk

Example code structure:

```python
if model.status == GRB.OPTIMAL:
    weights = [w[i].X for i in range(n)]
    print("Weights:", weights)
    print("Sum of weights:", sum(weights))

    portfolio_return_value = sum(mu[i] * weights[i] for i in range(n))
    portfolio_risk_value = sum(
        Sigma[i][j] * weights[i] * weights[j]
        for i in range(n)
        for j in range(n)
    )

    print("Portfolio return:", portfolio_return_value)
    print("Portfolio risk:", portfolio_risk_value)
```
In your final interpretation, try to explain:

- which assets receive higher weights
- whether the solution looks diversified
- how the result reflects the trade-off between return and risk

""",
}
GENERIC_TASK_HINT = """

At this stage, focus on keeping your work aligned with your own task plan and reasoning.

You may find it helpful to ask:

- What exactly is this task trying to achieve?
- How does this task connect to the overall optimization problem?
- What kind of AI support do I actually need here?
- What part of this task should remain my responsibility?
- How will I know whether the output is useful and appropriate?
"""


# --------------------------
# Helpers
# --------------------------
def key_prefix(name: str) -> str:
    return name.lower().replace(" ", "_")


def init_welcome_state() -> None:
    if "portfolio_welcome_step" not in st.session_state:
        st.session_state.portfolio_welcome_step = 0
    if "portfolio_started" not in st.session_state:
        st.session_state.portfolio_started = False


def init_page_state() -> None:
    init_welcome_state()
    p = key_prefix(PAGE_NAME)
    defaults = {
        f"{p}_num_tasks": 3,
        f"{p}_a1_task_decomposition": "",
        f"{p}_h1_need_planning_hint": "No",
        f"{p}_h1_planning_hint_notes": "",
        f"{p}_a2_role_ai_role": "",
        f"{p}_final_reflection": "",
    }
    for idx in range(1, len(REVISIT_ITEMS) + 1):
        defaults[f"{p}_revisit_q{idx}"] = 3

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def init_task_state(task_no: int) -> None:
    p = key_prefix(PAGE_NAME)
    prefix = f"{p}_task_{task_no}"
    defaults = {
        f"{prefix}_step1_define": "",
        f"{prefix}_need_hint": "No",
        f"{prefix}_hint_notes": "",
        f"{prefix}_saved": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def get_task_hint_text(task_no: int) -> str:
    return TASK_HINTS.get(task_no, GENERIC_TASK_HINT)


def export_dataframe() -> pd.DataFrame:
    p = key_prefix(PAGE_NAME)
    rows = []

    rows.append(
        {
            "section": "planning",
            "task_no": "",
            "task_decomposition": st.session_state.get(f"{p}_a1_task_decomposition", ""),
            "need_planning_hint": st.session_state.get(f"{p}_h1_need_planning_hint", ""),
            "planning_hint_notes": st.session_state.get(f"{p}_h1_planning_hint_notes", ""),
            "role_ai_role": st.session_state.get(f"{p}_a2_role_ai_role", ""),
            "task_response": "",
            "final_reflection": "",
            "revisit_q1": "",
            "revisit_q2": "",
            "revisit_q3": "",
            "revisit_q4": "",
            "revisit_q5": "",
            "revisit_q6": "",
            "revisit_q7": "",
            "revisit_q8": "",
        }
    )

    num_tasks = st.session_state.get(f"{p}_num_tasks", 3)
    for task_no in range(1, num_tasks + 1):
        init_task_state(task_no)
        rows.append(
            {
                "section": "task",
                "task_no": task_no,
                "task_decomposition": "",
                "need_planning_hint": "",
                "planning_hint_notes": "",
                "role_ai_role": "",
                "task_response": st.session_state.get(f"{p}_task_{task_no}_step1_define", ""),
                "final_reflection": "",
                "revisit_q1": "",
                "revisit_q2": "",
                "revisit_q3": "",
                "revisit_q4": "",
                "revisit_q5": "",
                "revisit_q6": "",
                "revisit_q7": "",
                "revisit_q8": "",
            }
        )

    rows.append(
        {
            "section": "reflection",
            "task_no": "",
            "task_decomposition": "",
            "need_planning_hint": "",
            "planning_hint_notes": "",
            "role_ai_role": "",
            "task_response": "",
            "final_reflection": st.session_state.get(f"{p}_final_reflection", ""),
            "revisit_q1": "",
            "revisit_q2": "",
            "revisit_q3": "",
            "revisit_q4": "",
            "revisit_q5": "",
            "revisit_q6": "",
            "revisit_q7": "",
            "revisit_q8": "",
        }
    )

    rows.append(
        {
            "section": "revisiting",
            "task_no": "",
            "task_decomposition": "",
            "need_planning_hint": "",
            "planning_hint_notes": "",
            "role_ai_role": "",
            "task_response": "",
            "final_reflection": "",
            "revisit_q1": st.session_state.get(f"{p}_revisit_q1", ""),
            "revisit_q2": st.session_state.get(f"{p}_revisit_q2", ""),
            "revisit_q3": st.session_state.get(f"{p}_revisit_q3", ""),
            "revisit_q4": st.session_state.get(f"{p}_revisit_q4", ""),
            "revisit_q5": st.session_state.get(f"{p}_revisit_q5", ""),
            "revisit_q6": st.session_state.get(f"{p}_revisit_q6", ""),
            "revisit_q7": st.session_state.get(f"{p}_revisit_q7", ""),
            "revisit_q8": st.session_state.get(f"{p}_revisit_q8", ""),
        }
    )

    return pd.DataFrame(rows)


# --------------------------
# Render sections
# --------------------------
def render_plan() -> None:
    p = key_prefix(PAGE_NAME)
    st.subheader("Plan")

    with st.expander("A1. Task Decomposition", expanded=True):
        st.markdown(
            """
Before you start solving the portfolio optimization problem, take time to break the work into smaller tasks and think carefully about how you want to work with AI. In this stage, your goal is not to solve everything yet. Instead, you should create a plan for how you will approach it.

As you complete this section, please focus on:

- What smaller tasks do I need to complete to solve this optimization problem?
- In what order should I attempt them?

For example: 

**Task 1: Pull the stock price data from yahoo finance**
 
- Download historical stock prices and organize them into a clean dataset.  
- Make sure the data is aligned by date and contains no obvious missing values.

"""
        )
        st.text_area(
            "Write your task list here:",
            key=f"{p}_a1_task_decomposition",
            height=180,
            placeholder="Write your task list here:",
        )

    with st.expander("H1. Do you need hints for the planning stage?", expanded=False):
        st.radio(
            "Do you need hints for the planning stage?",
            YES_NO_OPTIONS,
            key=f"{p}_h1_need_planning_hint",
            horizontal=True,
        )
        if st.session_state.get(f"{p}_h1_need_planning_hint", "No") == "Yes":
            st.info(TASK_HINTS["plan"])
            st.text_area(
                "Planning hint notes",
                key=f"{p}_h1_planning_hint_notes",
                height=120,
                placeholder="Write any useful planning notes here...",
            )

    with st.expander("A2. My Role and AI's Role", expanded=True):
        st.markdown(
            """
Before using AI, think about how you want to share the work across the process.

- What should I be responsible for?
- What can AI help with?
- Why does this division make sense for this optimization task?
"""
        )
        st.text_area(
            "My role and AI's role",
            key=f"{p}_a2_role_ai_role",
            height=180,
            placeholder="Write here...",
        )
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Save", key=f"{p}_plan_save_btn", use_container_width=True):
            st.session_state[f"{p}_plan_saved"] = True
    with col2:
        if st.session_state.get(f"{p}_plan_saved", False):
            st.success("Plan saved.")

def render_task(task_no: int) -> None:
    p = key_prefix(PAGE_NAME)
    prefix = f"{p}_task_{task_no}"
    init_task_state(task_no)

    st.subheader(f"Task {task_no}")

    if task_no == 1:
        with st.expander("Task 1. Pull the stock price data from yahoo finance", expanded=True):
            st.markdown(
                """
Please pull the Adj Close price from 1st January 2010 to 31st December 2017 for the following stocks:

```python
['HSBC', 'JPM', 'AAPL', 'WMT', 'AMZN', 'MSFT']
"""
)
        with st.expander("Step 2. Prompt AI", expanded=False):
            st.markdown(
                    """Your prompt should focus only on this task. For example, you may ask AI to help you:

- download the adjusted close prices

- organize the data into a clean table

- check for missing values
"""
)
        with st.expander("Step 3. Continue Working on This Task", expanded=False):
            st.markdown(
                """
                    #### Evaluate AI Prompt

                    After you receive the AI response, think about:

                    - whether it is clear and relevant?
                    - whether it gives the kind of support you actually need?
                    - Any revision needed?

                    #### Implementation

                    At this stage, continue your work by implementing the code in Jupyter Notebook.

                    #### Evaluate the Solution and Interpretation

                    After testing, think about:

                    - What does this result show?
                    - Does it actually answer the current task?
                    - Any revision needed?

                    #### Save the Task

                    Continue your work carefully, then click **Save task** when you are ready to move on.
                    """
            )
    else:
        with st.expander("Step 1. Define This Task", expanded=True):
            st.markdown(
                """Focus on this task from your own plan. Before using AI, first make clear what you are trying to do in this task and why it matters for solving the larger problem."""
            )
            st.markdown(
                """> **Questions to think about:** 
                
> What is my current task goal?  
> Why does this task matter for the larger problem?  
> What do I already think before using AI, and what am I still unsure about?"""
            )
            st.text_area(
                "Write here:",
                key=f"{prefix}_step1_define",
                height=220,
                placeholder="Define this task clearly here...",
            )

        with st.expander(f"Do you need hints for Task {task_no}?", expanded=False):
            st.radio(
            "Do you need hints?",
            YES_NO_OPTIONS,
            key=f"{prefix}_need_hint",
            horizontal=True,
        )
            if st.session_state.get(f"{prefix}_need_hint", "No") == "Yes":
                st.info(get_task_hint_text(task_no))
                st.text_area(
                "Hint notes",
                key=f"{prefix}_hint_notes",
                height=120,
                placeholder="Write any useful notes here...",
            )

        with st.expander("Step 2. Prompt AI", expanded=False):
            st.markdown(
            """
Your prompt should be specific to your current subtask.
Do not ask AI to solve everything at once.
"""
        )

        with st.expander("Step 3. Continue Working on This Task", expanded=False):
            st.markdown(
            """
                #### Evaluate AI Prompt

                After you receive the AI response, think about:

                - whether it is clear and relevant?
                - whether it gives the kind of support you actually need?
                - Any revision needed?

                #### Implementation

                At this stage, continue your work by implementing the code in Jupyter Notebook.

                #### Evaluate the Solution and Interpretation

                After testing, think about:

                - What does this result show?
                - Does it actually answer the current task?
                - Any revision needed?

                #### Save the Task

                Continue your work carefully, then click **Save task** when you are ready to move on.
                """
        )

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Save task", key=f"{prefix}_save_btn", use_container_width=True):
            st.session_state[f"{prefix}_saved"] = True
    with col2:
        if st.session_state.get(f"{prefix}_saved", False):
            st.success(f"Task {task_no} saved.")


def render_reflection() -> None:
    p = key_prefix(PAGE_NAME)
    st.subheader("Reflection")
    st.markdown(
        """Now that you have completed all of your tasks, take some time to reflect on your overall process. In this section, focus on how you approached the problem, how you worked with AI, and what you learned from the experience.

You do not need to describe every detail. Instead, try to identify the most important parts of your thinking, decision-making, testing, and revision process."""
    )
    st.markdown(
        """> **As you reflect, you may find it helpful to think about:**  
> how you broke the problem into tasks and whether that plan worked well?  
> how you divided the work between yourself and AI?  
> how your prompts, testing, and evaluation changed over time?  
> what you would do differently in a similar problem in the future?"""
    )
    st.markdown(
        """Try to write your thoughts based on your actual experience rather than an ideal process."""
    )
    st.text_area(
        "Write your end-of-problem reflection here:",
        key=f"{p}_final_reflection",
        height=260,
        placeholder="Write your end-of-problem reflection here...",
    )

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Save", key=f"{p}_reflection_save_btn", use_container_width=True):
            st.session_state[f"{p}_reflection_saved"] = True
    with col2:
        if st.session_state.get(f"{p}_reflection_saved", False):
            st.success("Reflection saved.")


def render_revisiting() -> None:
    p = key_prefix(PAGE_NAME)
    st.subheader("Revisiting Your Thinking Process")

    st.markdown(
        """
At the end of the last hands-on task, you have answered the following questions. Now that you’ve gone through this session, take another look at them and answer again based on how you really feel now.

There’s no right or wrong answer and your responses are **not graded by correctness**. Just reflect on your experience and how your thinking may have changed.
"""
    )

    st.markdown("### How to complete the questions")
    st.markdown(
        """
For each statement below, please choose a **number from 1 to 5**.
"""
    )

    st.markdown("### Rating Scale")
    st.markdown(
        """
- **1 = Strongly disagree**  
  *(This statement does not describe me at all)*

- **2 = Disagree**  
  *(This statement rarely describes what I do)*

- **3 = Neutral / Not sure**  
  *(This statement sometimes describes me, or I am unsure)*

- **4 = Agree**  
  *(This statement usually describes what I do)*

- **5 = Strongly agree**  
  *(This statement describes me very well)*

**Please select one number (1–5) for each item.**
"""
    )

    for idx, item in enumerate(REVISIT_ITEMS, start=1):
        st.markdown(f"**{idx}. {item}**")
        st.radio(
            label=f"Select your answer for item {idx}",
            options=LIKERT_OPTIONS,
            key=f"{p}_revisit_q{idx}",
            horizontal=True,
            label_visibility="collapsed",
        )


# --------------------------
# Main
# --------------------------
init_page_state()
num_tasks = st.session_state.get(f"{key_prefix(PAGE_NAME)}_num_tasks", 3)
for task_no in range(1, num_tasks + 1):
    init_task_state(task_no)

with st.sidebar:
    st.header("Controls")

    if st.session_state.get("portfolio_started", False):
        if st.button("+ Add Task", use_container_width=True):
            st.session_state[f"{key_prefix(PAGE_NAME)}_num_tasks"] += 1
            init_task_state(st.session_state[f"{key_prefix(PAGE_NAME)}_num_tasks"])
            st.rerun()


        df_export = export_dataframe()
        csv_bytes = df_export.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")

        st.download_button(
            label="Download CSV",
            data=csv_bytes,
            file_name="portfolio_results.csv",
            mime="text/csv",
            use_container_width=True,
        )

        st.caption(f"{PAGE_NAME}: {num_tasks} task(s)")
    else:
        st.caption("Please start from the welcome page.")

if not st.session_state.get("portfolio_started", False):
    step = st.session_state.portfolio_welcome_step

    st.markdown(
        """
        <div class="soft-card">
            <div class="soft-title" style="font-size:1.5rem; font-weight:800; color:#1e3a8a;">Welcome to Week 11 - Portfolio Optimization</div>
            <div class="soft-text">
                Welcome to week 11. Hope you have learned a lot from last week's tasks. This time we will still go through this portfolio optimization task step by step.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if step == 0:
        st.markdown(
            """
            <div class="soft-card">
                <div class="soft-text">
                    Move through the activity step by step, and pay attention not only to what you write, but also to how you plan, revise, evaluate, and reflect.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif step == 1:
        st.markdown(
            """
            <div class="soft-card">
                <div class="soft-text">
                    You will practice breaking the work into smaller tasks, using AI intentionally, checking whether the model and solution are sound, and reflecting on your process.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif step == 2:
        st.markdown(
            """
            <div class="soft-card">
                <div class="soft-text">
                    In this activity, you will work on one portfolio optimization problem through several stages, from planning to final reflection.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif step == 3:
        st.markdown(
            """
            <div class="soft-card">
                <div class="soft-text">
                    You will move through four parts: Plan, complete and monitor each task, Reflection, and revisiting your thinking process.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="notice-box">
                <div class="notice-title">Before you begin</div>
                <div class="notice-text">
                    When you are ready, begin the activity. There is no need to rush — just work through it one step at a time.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if step >= 2:
        st.markdown("### What you will practice")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(
                """
                <div class="soft-card">
                    <div class="soft-title">Plan before coding</div>
                    <div class="soft-text">
                        Break a complex optimization task into smaller parts and decide what should happen first.
                    </div>
                </div>

                <div class="soft-card">
                    <div class="soft-title">Use AI with intention</div>
                    <div class="soft-text">
                        Decide what support you need instead of asking AI to generate everything automatically.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                """
                <div class="soft-card">
                    <div class="soft-title">Check results carefully</div>
                    <div class="soft-text">
                        Check whether the model, code, and output are correct, relevant, and logically consistent.
                    </div>
                </div>

                <div class="soft-card">
                    <div class="soft-title">Reflect on your process</div>
                    <div class="soft-text">
                        Notice what worked, what did not, and what you would change next time.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    if step >= 3:
        st.markdown("### The problem in this activity")
        st.markdown(
            """
            <div class="soft-card">
                <div class="soft-title">Portfolio Optimization</div>
                <div class="soft-text">
                    Analyze financial returns and risk, build an optimization model, solve for portfolio weights, and interpret the final result.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if step >= 4:
        st.markdown("### How the activity is organized")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(
                """
                <div class="soft-card">
                    <div class="soft-title">Plan</div>
                    <div class="soft-text">
                        Break the problem into tasks and think about your role and AI’s role.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                """
                <div class="soft-card">
                    <div class="soft-title">Complete each task</div>
                    <div class="soft-text">
                        Work step by step and use AI only when it helps the current subtask.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c3:
            st.markdown(
                """
                <div class="soft-card">
                    <div class="soft-title">Reflection</div>
                    <div class="soft-text">
                        Look back on your overall process and identify what you learned.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c4:
            st.markdown(
                """
                <div class="soft-card">
                    <div class="soft-title">Revisiting</div>
                    <div class="soft-text">
                        Reconsider your thinking process and how your confidence may have changed.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    col_back, col_next = st.columns(2)
    with col_back:
        if step > 0:
            if st.button("Go Back", use_container_width=True):
                st.session_state.portfolio_welcome_step -= 1
                st.rerun()
    with col_next:
        if step < 4:
            if st.button("Continue", type="primary", use_container_width=True):
                st.session_state.portfolio_welcome_step += 1
                st.rerun()
        else:
            if st.button("I'm Ready to Start", type="primary", use_container_width=True):
                st.session_state.portfolio_started = True
                st.rerun()

else:
    st.markdown(
        """
        <div class="notice-box">
            <div class="notice-title">Important reminders before you start</div>
            <div class="notice-text">
                Please work on the actual optimization analysis and coding in your preferred environment.<br><br>
                This page is here to guide your planning, use of AI, monitoring, and reflection.<br><br>
                At the bottom of each task page, there is a button called <b>Save task</b>. Please click it before moving to the next task.<br><br>
                If you want to review what you have written, you can expand <b>Preview of your responses</b> near the bottom of the page.<br><br>
                Finally, click <b>Download CSV</b> if you need to submit or save your responses.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_labels = ["Plan"] + [f"Task {i}" for i in range(1, num_tasks + 1)] + ["Reflection", "Revisiting Your Thinking Process"]
    sections = st.tabs(section_labels)

    with sections[0]:
        render_plan()

    for task_no in range(1, num_tasks + 1):
        with sections[task_no]:
            render_task(task_no)

    with sections[-2]:
        render_reflection()

    with sections[-1]:
        render_revisiting()

    st.divider()
    with st.expander("Preview of your responses", expanded=False):
        st.dataframe(export_dataframe(), use_container_width=True)
