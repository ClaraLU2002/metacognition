import pandas as pd
import streamlit as st

st.set_page_config(page_title="Metacognitive Scaffolding for Optimization Tasks", layout="wide")
st.title("Metacognitive Scaffolding for Optimization Tasks")

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
PROBLEMS = ["Arbitrage", "Hawker Center"]

YES_NO_OPTIONS = ["No", "Yes"]

DECISION_OPTIONS = [
    "Accept and use it",
    "Revise the prompt and ask again",
    "Keep part of it, reject part of it",
    "Try a different strategy (with or without AI)",
    "Pause and rethink the task itself before continuing",
]

REVISIT_ITEMS = [
    "I ask myself periodically if I am meeting my goals.",
    "I set specific goals before I begin a task.",
    "I learn best when I know something about the topic.",
    "I summarize what I’ve learned after I finish.",
    "I ask others (including AI tools) for help when I don’t understand something.",
    "I am aware of what strategies I use when I study.",
    "I am a good judge of how well I understand something.",
    "I try to break studying down into smaller steps.",
]

LIKERT_OPTIONS = [1, 2, 3, 4, 5]

PLANNING_HINT_TEXT = """Hints: Possible planning stages:

- 1.Build a mathematical model

Translate the problem into a mathematical form before trying to solve it. For example, think about how the exchange-rate table can be represented mathematically, what condition would indicate a multi-currency arbitrage opportunity, and how the gain along a sequence of currency exchanges should be calculated.

- 2.Choose a solution strategy

After building the model, decide how you want to solve the problem. For example, consider whether you want to test a few cycles manually, search systematically for possible arbitrage cycles, treat the problem as a graph problem, or transform the multiplicative relationships into a form that is easier to analyse.

- 3.Implement the method in code

Use your mathematical model and chosen strategy to guide your coding. For example, think about how to store the exchange-rate data, how to represent the structure of the problem in code, how to implement your detection method, and what output your program should produce.

- 4.Check and validate the result

Do not assume that a computed result is automatically correct. Check whether the output is consistent with your mathematical model, whether a detected path really produces arbitrage, and whether a failure to detect arbitrage reflects the actual problem rather than an issue in the code or method.

- 5.Interpret and present the solution

Finally, explain clearly what your result means. State whether an arbitrage opportunity exists, what evidence supports your conclusion, and how your mathematical model, code output, and final interpretation connect to one another.
"""

TASK_HINTS = {
    "Arbitrage": {
        1: """Hint for Task 1: Build a Mathematical Model

At this stage, focus on translating the problem into a mathematical form before coding. Think about what each exchange rate means, how to represent a currency conversion mathematically, and what condition would indicate arbitrage.

You may find it helpful to define:

- aij: the exchange rate from currency i to currency j
- xij: the amount of currency i converted to currency j
- yk: the net amount of currency k after all transactions

Then ask yourself:

What objective should be maximized?

How should the flow-balance constraints be written?

How can the model indicate whether arbitrage exists?

One possible way to think about the problem is to use aij, xij, and yk to describe exchange rates, transaction flows, and net outcomes, and then consider whether the model can produce a profitable closed cycle of exchanges.""",

        2: """Hint for Task 2: Choose a Solution Strategy

Once your mathematical model is clear, the next step is to decide how you want to solve the problem. Try not to move directly to coding before you have chosen a method.

You may find it helpful to think about questions such as:

- Do I want to solve this as an optimisation problem, a graph problem, or another type of problem?
- What should my method take as input, and what should it return as output?
- If arbitrage exists, how will I identify the profitable cycle or path?
- How can I make sure that my method matches the mathematical model I built?""",

        3: """Hint for Task 3: Implement the Method in Code

Now use your mathematical model and chosen strategy to guide your coding. Try to keep the code aligned with your own reasoning, rather than writing code first and hoping it works.

A useful coding plan may include:

- loading or storing the exchange-rate data clearly  
- writing a function to detect whether arbitrage exists  
- writing a second function, if needed, to recover the arbitrage path or cycle  
- testing your code on the given exchange-rate table  

You do not need to follow this structure exactly, but it may help you think about how to separate the problem into clear coding steps. As you code, keep asking yourself whether each part of the program corresponds to something meaningful in your mathematical model.

Example code skeleton:

```python
from gurobipy import Model, GRB, quicksum
import numpy as np

def arbitrage_detection(rates):
    # build the model here
    # define decision variables
    # set the objective
    # add the constraints
    # solve the model
    pass

def find_the_path(x_opt_indices):
    # reconstruct a path from the nonzero decisions
    pass
```

Example of loading the rate matrix:

```python
import pandas as pd
rates_df = pd.read_csv("arbitrage.csv")
rates = rates_df.values[:, 1:]  # adjust this if needed
```

""",

        4: """Hint for Task 4: Check and Validate the Result

After you obtain a result, do not assume that it is automatically correct. Your next job is to check whether the output really matches the mathematical meaning of arbitrage.

You may find it helpful to ask:

- Does my code say that arbitrage exists or not?
- If arbitrage exists, does the reported path or cycle actually make sense?
- If I multiply the exchange rates along that cycle, do I really end up with more than I started with?
- If no arbitrage is found, could that be due to a problem in my code or method rather than the data itself?

Example validation idea:

```python
if all_one:
    arbitrage_path = find_the_path(np.argwhere(x_opt))
    print("Arbitrage path is:", arbitrage_path)
```

You may also try a simple manual check on one reported path to confirm that the result is consistent with your model and code.""",

        5: """Hint for Task 5: Interpret and Present the Solution

In this task, do not only report the code output. Explain what the result means in relation to the original problem and how your conclusion is supported by both the model and the computation.

A clear final explanation may include:

- whether an arbitrage opportunity exists  
- if yes, what the profitable path or cycle is  
- why that path creates profit  
- if no arbitrage is found, what evidence supports that conclusion  
- how your mathematical model, code output, and interpretation connect to one another  

Try to present your solution in a way that makes your reasoning visible, rather than only stating the final answer.
""",
    },
    "Hawker Center": {
        "plan": """Hints: Possible planning stages

Before you start solving the problem, try to break it into a few smaller tasks. This can help you organize your thinking and avoid jumping into code too quickly.

A possible way to divide the work is:

- Task 1: Explore the dataset and visualize the first 10 hawker centres on a map
- Task 2: Decide on a solution strategy for the delivery route problem
- Task 3: Implement the method in code, including distance calculation and route solving
- Task 4: Check and validate whether the route is correct
- Task 5: Interpret and present the final solution clearly

""",
        1: """Hint for Task 1: Explore the Data and Visualize the First 10 Hawker Centres

First, load the dataset and identify the columns containing the hawker centre names and coordinates. Then keep only the first 10 hawker centres and plot them on a map. This step helps you understand the delivery locations before starting the optimization.

Essential code structure:

```python
import pandas as pd
import folium

df = pd.read_csv("hawker_centres.csv")
df = df.head(10).copy()

# identify name / latitude / longitude columns
name_col = "..."
lat_col = "..."
lon_col = "..."

# build a map and add markers""",
        2: """Hint for Task 2: Choose a Solution Strategy

Before writing the full program, think about how this milk delivery problem should be solved. Your goal is to find a route that visits each hawker centre once and returns to the starting point with the minimum total travel distance.

You may find it helpful to think about questions such as:

- What should the input be: coordinates, a distance matrix, or something else?
- What should the output be: a route, a list of locations in visiting order, or both?
- How will I represent the route in code?
- How can I organize the problem into clear steps before writing the full solution?

One possible way is to break the task into smaller functions. For example:

```python
def build_distance_matrix(df, lat_col, lon_col):
    # compute pairwise distances
    pass

def solve_route(distance_matrix):
    # solve the routing problem
    pass

def plot_route(df, path, lat_col, lon_col):
    # visualize the route on a map
    pass
    """,
        3: """Hint for Task 3: Implement the Method in Code

Now use your chosen strategy to guide your coding. At this stage, your goal is to turn the delivery problem into a working computational method.

A useful coding plan may include:

- loading the hawker centre data clearly
- extracting the coordinates of the selected locations
- building a distance matrix
- writing a function to solve the route problem
- returning the final visiting order

Try to keep the code aligned with your own reasoning, rather than writing code first and hoping it works.

Example code skeleton:

```python
import numpy as np

def build_distance_matrix(df, lat_col, lon_col):
    # compute pairwise distances between hawker centres
    return distance_matrix

def solve_route(distance_matrix):
    # build and solve the routing problem
    # return the final path
    pass

distance_matrix = build_distance_matrix(df, lat_col, lon_col)
path = solve_route(distance_matrix)
print(path)
""",
        4: """Hint for Task 4: Check and Validate the Result

After you obtain a route, do not assume that it is automatically correct. Your next job is to check whether the output really matches the delivery problem.

You may find it helpful to ask:

- Does the route visit every hawker centre exactly once?
- Does the route return to the starting point?
- Is the visiting order complete and sensible?
- Does the route match the distance data used in the program?
- If the result looks unusual, could the issue come from the distance matrix, the solver logic, or the way the path was reconstructed?

Example validation structure:

```python
print("Route:", path)

# check whether all locations are included
print("Number of stops in route:", len(path))

# optional: inspect whether the route returns to the start
print("Start:", path[0], "End:", path[-1])

You may also manually check a few consecutive stops to see whether the reported route is consistent with your method.
""",
        5: """Hint for Task 5: Interpret and Present the Solution

In this task, do not only report the code output. Explain what the final route means in relation to the original milk delivery problem and present the result in a clear way.

A clear final explanation may include:

- the final visiting order
- whether the route forms a complete delivery tour
- how the result is shown on the map
- what the route suggests about the delivery plan
- how your code output and interpretation connect to one another

Example presentation structure:

```python
print("Final route:", path)

# create a map
# add hawker centre markers
# draw the route in visiting order
# display the map

Try to present your solution in a way that makes your reasoning visible, rather than only stating the final answer.
""",
    },
}

GENERIC_TASK_HINT = """General hint for this task

At this stage, focus on keeping your work aligned with your own task plan and reasoning.

You may find it helpful to ask:

- What exactly is this task trying to achieve?
- How does this task connect to my earlier model, method, or result?
- What kind of AI support do I actually need here: explanation, options, checking, debugging, or interpretation?
- What part of this task should still remain my responsibility?
- How will I know whether the output is valid, useful, and relevant to the problem?

Try to make sure that:
- your task goal is clear,
- your prompt asks for specific help,
- your evaluation checks the response critically,
- and your next step follows from evidence rather than convenience.
"""


# --------------------------
# Helpers
# --------------------------
def key_prefix(problem: str) -> str:
    return problem.lower().replace(" ", "_")


def init_welcome_state():
    if "welcome_step" not in st.session_state:
        st.session_state.welcome_step = 0


def get_hint(decision: str) -> str:
    if decision == "Revise the prompt and ask again":
        return "Hint: Make the prompt more specific and ask only for the kind of help you actually need."
    if decision == "Try a different strategy (with or without AI)":
        return "Hint: Consider whether the task should be split differently or whether another representation would work better."
    if decision == "Pause and rethink the task itself before continuing":
        return "Hint: Revisit the task goal and check whether this is the right subproblem to work on now."
    return ""


def get_task_hint_text(problem: str, task_no: int) -> str:
    problem_hints = TASK_HINTS.get(problem, {})
    if task_no in problem_hints:
        return problem_hints[task_no]
    return GENERIC_TASK_HINT


def get_plan_hint_text(problem: str) -> str:
    problem_hints = TASK_HINTS.get(problem, {})
    return problem_hints.get("plan", PLANNING_HINT_TEXT)


def init_problem_state(problem: str) -> None:
    p = key_prefix(problem)

    defaults = {
        f"{p}_num_tasks": 2,
        f"{p}_planning_intro": "",
        f"{p}_a1_task_decomposition": "",
        f"{p}_h1_need_planning_hint": "No",
        f"{p}_h1_planning_hint_notes": "",
        f"{p}_a2_role_ai_role": "",
        f"{p}_final_reflection": "",
    }

    if problem == "Hawker Center":
        for idx in range(1, len(REVISIT_ITEMS) + 1):
            defaults[f"{p}_revisit_q{idx}"] = 3

    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def init_task_state(problem: str, task_no: int) -> None:
    p = key_prefix(problem)
    prefix = f"{p}_task_{task_no}"

    defaults = {
        f"{prefix}_title": "",
        f"{prefix}_step1_define": "",
        f"{prefix}_need_hint": "No",
        f"{prefix}_hint_notes": "",
        f"{prefix}_step2_prompt_eval": "",
        f"{prefix}_step3_decision": DECISION_OPTIONS[0],
        f"{prefix}_step3_notes": "",
        f"{prefix}_step4_implement_test_interpret": "",
        f"{prefix}_revise_from_beginning": "No",
        f"{prefix}_step5_revise": "",
        f"{prefix}_step6_reflect": "",
        f"{prefix}_saved": False,
    }

    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# --------------------------
# Session state initialization
# --------------------------
init_welcome_state()

if "started" not in st.session_state:
    st.session_state.started = False

for problem in PROBLEMS:
    init_problem_state(problem)
    p = key_prefix(problem)
    for i in range(1, st.session_state.get(f"{p}_num_tasks", 2) + 1):
        init_task_state(problem, i)


# --------------------------
# Export
# --------------------------
def export_dataframe() -> pd.DataFrame:
    rows = []

    for problem in PROBLEMS:
        p = key_prefix(problem)
        num_tasks = st.session_state.get(f"{p}_num_tasks", 0)

        rows.append(
            {
                "problem": problem,
                "section": "planning",
                "task_no": "",
                "planning_intro": st.session_state.get(f"{p}_planning_intro", ""),
                "a1_task_decomposition": st.session_state.get(f"{p}_a1_task_decomposition", ""),
                "h1_need_planning_hint": st.session_state.get(f"{p}_h1_need_planning_hint", ""),
                "h1_planning_hint_notes": st.session_state.get(f"{p}_h1_planning_hint_notes", ""),
                "a2_role_ai_role": st.session_state.get(f"{p}_a2_role_ai_role", ""),
                "task_title": "",
                "step1_define": "",
                "need_hint": "",
                "hint_notes": "",
                "step2_prompt_eval": "",
                "step3_decision": "",
                "step3_notes": "",
                "step4_implement_test_interpret": "",
                "revise_from_beginning": "",
                "step5_revise": "",
                "step6_reflect": "",
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

        for i in range(1, num_tasks + 1):
            prefix = f"{p}_task_{i}"
            init_task_state(problem, i)

            rows.append(
                {
                    "problem": problem,
                    "section": "task",
                    "task_no": i,
                    "planning_intro": "",
                    "a1_task_decomposition": "",
                    "h1_need_planning_hint": "",
                    "h1_planning_hint_notes": "",
                    "a2_role_ai_role": "",
                    "task_title": st.session_state.get(f"{prefix}_title", ""),
                    "step1_define": st.session_state.get(f"{prefix}_step1_define", ""),
                    "need_hint": st.session_state.get(f"{prefix}_need_hint", ""),
                    "hint_notes": st.session_state.get(f"{prefix}_hint_notes", ""),
                    "step2_prompt_eval": st.session_state.get(f"{prefix}_step2_prompt_eval", ""),
                    "step3_decision": st.session_state.get(f"{prefix}_step3_decision", ""),
                    "step3_notes": st.session_state.get(f"{prefix}_step3_notes", ""),
                    "step4_implement_test_interpret": st.session_state.get(
                        f"{prefix}_step4_implement_test_interpret", ""
                    ),
                    "revise_from_beginning": st.session_state.get(f"{prefix}_revise_from_beginning", ""),
                    "step5_revise": st.session_state.get(f"{prefix}_step5_revise", ""),
                    "step6_reflect": st.session_state.get(f"{prefix}_step6_reflect", ""),
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
                "problem": problem,
                "section": "reflection",
                "task_no": "",
                "planning_intro": "",
                "a1_task_decomposition": "",
                "h1_need_planning_hint": "",
                "h1_planning_hint_notes": "",
                "a2_role_ai_role": "",
                "task_title": "",
                "step1_define": "",
                "need_hint": "",
                "hint_notes": "",
                "step2_prompt_eval": "",
                "step3_decision": "",
                "step3_notes": "",
                "step4_implement_test_interpret": "",
                "revise_from_beginning": "",
                "step5_revise": "",
                "step6_reflect": "",
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

        if problem == "Hawker Center":
            rows.append(
                {
                    "problem": problem,
                    "section": "revisiting",
                    "task_no": "",
                    "planning_intro": "",
                    "a1_task_decomposition": "",
                    "h1_need_planning_hint": "",
                    "h1_planning_hint_notes": "",
                    "a2_role_ai_role": "",
                    "task_title": "",
                    "step1_define": "",
                    "need_hint": "",
                    "hint_notes": "",
                    "step2_prompt_eval": "",
                    "step3_decision": "",
                    "step3_notes": "",
                    "step4_implement_test_interpret": "",
                    "revise_from_beginning": "",
                    "step5_revise": "",
                    "step6_reflect": "",
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
def render_plan(problem: str) -> None:
    p = key_prefix(problem)

    st.subheader("Plan")

    with st.expander("A1. Task Decomposition", expanded=True):
        st.markdown(
            """
Before using AI, take time to break the problem into smaller tasks and think carefully about how you want to work with AI. In this stage, your goal is not to solve the problem yet. Instead, you should create a plan for how you will approach it.

As you complete this section, focus on three things:

- What smaller tasks do I need to complete to solve this problem?
- In what order should I attempt them?
- What should be my responsibility and what AI can support?

Try to answer based on your real thinking process. A good plan does not need to be perfect, but it should help you begin the problem in a clear and thoughtful way.
"""
        )

        st.text_area(
            "Write your task list here:",
            key=f"{p}_a1_task_decomposition",
            height=180,
            placeholder="1.\n2.\n3.\n...",
        )

    with st.expander("H1. Do you need hints for the planning stage?", expanded=False):
        st.radio(
            "Do you need hints for the planning stage?",
            YES_NO_OPTIONS,
            key=f"{p}_h1_need_planning_hint",
            horizontal=True,
        )

        if st.session_state.get(f"{p}_h1_need_planning_hint", "No") == "Yes":
            st.info(get_plan_hint_text(problem))
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
- Why does this division make sense for this problem?
"""
        )
        st.text_area(
            "My role and AI's role",
            key=f"{p}_a2_role_ai_role",
            height=180,
            placeholder="Write here...",
        )


def render_task(problem: str, task_no: int) -> None:
    p = key_prefix(problem)
    prefix = f"{p}_task_{task_no}"

    init_task_state(problem, task_no)

    task_header = "Monitor Task 1" if task_no == 1 else f"Task {task_no}"
    st.subheader(task_header)

    with st.expander("Step 1. Define This Task", expanded=True):
        st.markdown(
            """Focus on Task 1 from your own plan. Before using AI, first make clear what you are trying to do in this task and why it matters for solving the larger problem."""
        )

        st.markdown(
            """> **Questions:**  
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
            st.info(get_task_hint_text(problem, task_no))
            st.text_area(
                "Hint notes",
                key=f"{prefix}_hint_notes",
                height=120,
                placeholder="Write any useful notes from the hint here...",
            )

    with st.expander("Step 2. Prompt AI and Evaluate the Response", expanded=False):
        st.text_area(
            "Write a prompt to AI for this specific task.",
            key=f"{prefix}_step2_prompt_eval",
            height=180,
            placeholder="Write your prompt, summarize the AI response...",
        )

    with st.expander("Step 3. Evaluate the Response and Decide What to Do Next", expanded=False):
        st.radio(
            "After receiving a response, do not accept it automatically. Instead, evaluate it carefully and decide how useful or reliable it is for your current task.Then  decide what you will do next. The goal is to make an intentional decision rather than following the response automatically.",
            DECISION_OPTIONS,
            key=f"{prefix}_step3_decision",
        )
        st.text_area(
            "Decision notes",
            key=f"{prefix}_step3_notes",
            height=150,
            placeholder="Explain why you made this decision...",
        )

        hint_text = get_hint(st.session_state.get(f"{prefix}_step3_decision", ""))
        if hint_text:
            st.info(hint_text)

    with st.expander("Step 4. Implement, Test, and Interpret", expanded=False):
        st.markdown(
            """Now apply the idea, method, or response that you decided to use. Record what you tested, what you expected, what actually happened, and what the result means for this task."""
        )
        st.markdown(
            """> **Questions:**  
    > What did I do?  
    > What result(s) did I observe?"""
        )
        st.text_area(
            "Write here:",
            key=f"{prefix}_step4_implement_test_interpret",
            height=220,
            placeholder="Describe implementation, observed results, and interpretation...",
        )

    with st.expander(
            "Based on my evaluation of the result, do I need to revise this task from the beginning?",
            expanded=False,
    ):
        st.radio(
            "Do I need to revise this task from the beginning?",
            YES_NO_OPTIONS,
            key=f"{prefix}_revise_from_beginning",
            horizontal=True,
        )

    if st.session_state.get(f"{prefix}_revise_from_beginning", "No") == "Yes":
        with st.expander("Step 5. Revise if Needed", expanded=True):
            st.markdown(
                """If the response, method, or result was not fully satisfactory, revise your prompt or your approach and try again. Use this step to explain what you changed and what happened after the revision."""
            )
            st.markdown(
                """> **Questions:**  
    > What did I change in my prompt or approach, and why?  
    > What happened after the revision or second test?"""
            )
            st.text_area(
                "Write here:",
                key=f"{prefix}_step5_revise",
                height=220,
                placeholder="Write revisions here...",
            )

    with st.expander("Step 6. Reflect on This Task", expanded=True):
        st.markdown(
            """Finally, reflect on what you learned from this task. Focus on what you understood better about the problem, how AI supported or failed to support you, and what you would do differently in the next task."""
        )
        st.markdown(
            """> **Questions:**  
    > What did I learn about the problem from this task?  
    > What did I learn about using AI from this task?  
    > What would I do differently in the next task?"""
        )
        st.text_area(
            "Write here:",
            key=f"{prefix}_step6_reflect",
            height=220,
            placeholder="Write your reflection here...",
        )
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Save task", key=f"{prefix}_save_btn", use_container_width=True):
            st.session_state[f"{prefix}_saved"] = True
    with col2:
        if st.session_state.get(f"{prefix}_saved", False):
            st.success(f"{problem} - Task {task_no} saved.")


def render_reflection(problem: str) -> None:
    p = key_prefix(problem)

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

def render_revisiting_hawker() -> None:
    p = key_prefix("Hawker Center")

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
# Sidebar
# --------------------------
with st.sidebar:
    st.header("Controls")

    if st.session_state.started:
        for problem in PROBLEMS:
            p = key_prefix(problem)
            if st.button(f"+ Add Task to {problem}", key=f"add_{p}", use_container_width=True):
                st.session_state[f"{p}_num_tasks"] += 1
                init_task_state(problem, st.session_state[f"{p}_num_tasks"])
                st.rerun()

    df_export = export_dataframe()
    csv_bytes = df_export.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")

    st.download_button(
        label="Download CSV",
        data=csv_bytes,
        file_name="metacognition_results.csv",
        mime="text/csv",
        use_container_width=True,
    )

    if st.session_state.started:
        for problem in PROBLEMS:
            p = key_prefix(problem)
            st.caption(f"{problem}: {st.session_state[f'{p}_num_tasks']} task(s)")
    else:
        st.caption("Please start from the welcome page.")

# --------------------------
# Welcome page
# -------------------------


if not st.session_state.started:
    init_welcome_state()
    step = st.session_state.welcome_step

    st.markdown(
        """
        <div class="welcome-shell">
            <div class="welcome-title">Welcome to Today’s Optimization Studio</div>
            <div class="welcome-subtitle">
                Move through the activity step by step, and pay attention not only to the answers,
                but also to how you plan, test, revise, and reflect.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if step == 0:
        st.markdown(
            """
            <div class="speech-box">
                Welcome. We’ll go through this activity one step at a time.
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif step == 1:
        st.markdown(
            """
            <div class="speech-box">
                This time, the focus is not only on getting the answer, but also on noticing how you solve the problem.
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif step == 2:
        st.markdown(
            """
            <div class="speech-box">
                You will practice planning, using AI intentionally, checking outputs, and reflecting on your process.
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif step == 3:
        st.markdown(
            """
            <div class="speech-box">
                In this activity, you will work on two problems: Arbitrage Detection and Hawker Center.
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif step == 4:
        st.markdown(
            """
            <div class="speech-box">
                For each problem, you will move through three parts: Plan, Complete and monitor each task, and Reflection.
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif step >= 5:
        st.markdown(
            """
            <div class="final-guide-box">
                <div class="final-guide-label">Before you begin</div>
                <div class="final-guide-text">
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
                        Break a complex problem into smaller tasks and decide what should happen first.
                    </div>
                </div>

                <div class="soft-card">
                    <div class="soft-title">Use AI with intention</div>
                    <div class="soft-text">
                        Decide what support you need instead of asking AI to do everything automatically.
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
                        Test whether the output is correct, useful, and relevant to the actual task.
                    </div>
                </div>

                <div class="soft-card">
                    <div class="soft-title">Reflect on your learning</div>
                    <div class="soft-text">
                        Notice what worked, what did not, and what you would change next time.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    if step >= 3:
        st.markdown("### Problems in this activity")
        c1, c2 = st.columns(2)

        with c1:
            st.markdown(
                """
                <div class="soft-card">
                    <div class="soft-title">Arbitrage Detection</div>
                    <div class="soft-text">
                        Examine exchange rates and determine whether a profitable arbitrage opportunity exists.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with c2:
            st.markdown(
                """
                <div class="soft-card">
                    <div class="soft-title">Hawker Center</div>
                    <div class="soft-text">
                        Work on a routing problem involving location data, distance calculation, and route optimization.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    if step >= 4:
        st.markdown("### How the activity is organized")
        c1, c2, c3 = st.columns(3)

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
                    <div class="soft-title">Complete and monitor each task</div>
                    <div class="soft-text">
                        Work step by step, prompt AI when needed, and evaluate each response carefully.
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
                        Look back on your process and identify what you learned.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    if step >= 5:
        st.markdown(
            """
            <div class="start-panel">
                Please do your coding in Jupyter Notebook or another environment you are comfortable with.
                This page is here to guide your planning, monitoring, and reflection.
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    col_back, col_next = st.columns(2)

    with col_back:
        if step > 0:
            if st.button("Go Back", use_container_width=True):
                st.session_state.welcome_step -= 1
                st.rerun()

    with col_next:
        if step < 5:
            if st.button("Continue", type="primary", use_container_width=True):
                st.session_state.welcome_step += 1
                st.rerun()
        else:
            if st.button("I'm Ready to Start", type="primary", use_container_width=True):
                st.session_state.started = True
                st.rerun()

else:
    main_tabs = st.tabs(PROBLEMS)

    for idx, problem in enumerate(PROBLEMS):
        p = key_prefix(problem)
        num_tasks = st.session_state.get(f"{p}_num_tasks", 2)

        with main_tabs[idx]:
            st.header(problem)
            st.caption(
                "Please refer to the Jupyter Notebook for the problem description, and also write the coding process and answer in the Jupyter Notebook.")

            if problem == "Hawker Center":
                section_labels = ["Plan"] + [f"Task {i}" for i in range(1, num_tasks + 1)] + ["Reflection",
                                                                                              "Revisiting"]
            else:
                section_labels = ["Plan"] + [f"Task {i}" for i in range(1, num_tasks + 1)] + ["Reflection"]

            inner_tabs = st.tabs(section_labels)


            with inner_tabs[0]:
                render_plan(problem)

            for i in range(1, num_tasks + 1):
                with inner_tabs[i]:
                    render_task(problem, i)

            if problem == "Hawker Center":
                with inner_tabs[-2]:
                    render_reflection(problem)
                with inner_tabs[-1]:
                    render_revisiting_hawker()
            else:
                with inner_tabs[-1]:
                    render_reflection(problem)


    st.divider()
    st.subheader("Preview of export data")
    st.dataframe(export_dataframe(), use_container_width=True)