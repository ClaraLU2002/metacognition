import io
import pandas as pd
import streamlit as st


st.set_page_config(page_title="Metacognitive Regulation Tool", layout="wide")

st.title("AI-Supported Metacognitive Regulation Tool")

# --------------------------
# Session state initialization
# --------------------------
if "num_tasks" not in st.session_state:
    st.session_state.num_tasks = 2

if "planning_tasks" not in st.session_state:
    st.session_state.planning_tasks = ""

if "planning_roles" not in st.session_state:
    st.session_state.planning_roles = ""

if "reflection" not in st.session_state:
    st.session_state.reflection = ""


# --------------------------
# Helper functions
# --------------------------
def get_hint(decision: str) -> str:
    if decision == "Revise prompt":
        return "Hint: Have you clearly defined the task boundary? Can your prompt be more specific?"
    if decision == "Change strategy":
        return "Hint: Re-check whether this task should be split further or approached differently."
    return ""


def export_dataframe() -> pd.DataFrame:
    rows = []

    rows.append(
        {
            "section": "planning",
            "task_id": "",
            "planning_tasks": st.session_state.get("planning_tasks", ""),
            "planning_roles": st.session_state.get("planning_roles", ""),
            "goal": "",
            "idea": "",
            "prompt": "",
            "ai_response": "",
            "evaluation": "",
            "result": "",
            "decision": "",
            "reflection": "",
        }
    )

    for i in range(1, st.session_state.num_tasks + 1):
        rows.append(
            {
                "section": "task",
                "task_id": i,
                "planning_tasks": "",
                "planning_roles": "",
                "goal": st.session_state.get(f"goal_{i}", ""),
                "idea": st.session_state.get(f"idea_{i}", ""),
                "prompt": st.session_state.get(f"prompt_{i}", ""),
                "ai_response": st.session_state.get(f"ai_response_{i}", ""),
                "evaluation": st.session_state.get(f"evaluation_{i}", ""),
                "result": st.session_state.get(f"result_{i}", ""),
                "decision": st.session_state.get(f"decision_{i}", ""),
                "reflection": "",
            }
        )

    rows.append(
        {
            "section": "reflection",
            "task_id": "",
            "planning_tasks": "",
            "planning_roles": "",
            "goal": "",
            "idea": "",
            "prompt": "",
            "ai_response": "",
            "evaluation": "",
            "result": "",
            "decision": "",
            "reflection": st.session_state.get("reflection", ""),
        }
    )

    return pd.DataFrame(rows)


# --------------------------
# Sidebar controls
# --------------------------
with st.sidebar:
    st.header("Controls")

    if st.button("+ Add Task", use_container_width=True):
        st.session_state.num_tasks += 1

    df_export = export_dataframe()
    csv_bytes = df_export.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")

    st.download_button(
        label="Download CSV",
        data=csv_bytes,
        file_name="metacognition_results.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.caption(f"Current number of tasks: {st.session_state.num_tasks}")


# --------------------------
# Tabs
# --------------------------
tab_labels = ["Planning"] + [f"Task {i}" for i in range(1, st.session_state.num_tasks + 1)] + ["Reflection"]
tabs = st.tabs(tab_labels)

# --------------------------
# Planning tab
# --------------------------
with tabs[0]:
    st.subheader("Planning")

    st.markdown(
        """
**Break the problem into smaller tasks and decide your role vs AI's role.**

**Part A: Break the problem into your own tasks (you decide)**  
Before using AI, break the problem into a set of smaller tasks that you think are needed.

**A1. Task decomposition (your design)**  
- What smaller tasks do I need to complete to solve this problem?  
- In what order should I attempt them?  
- Which tasks are about understanding/modeling, checking/calculation, proof/justification, or interpretation?

**A2. What is my role and what is AI’s role?**  
- What should I be responsible for?  
- What can AI help with?  
- What should I not delegate to AI in this problem?

**A3. Task allocation (who does what, and why?)**  
For each task, briefly note:  
- What I should do first  
- What AI may help with  
- What I should not delegate  
- Why this division makes sense
        """
    )

    st.text_area(
        "Tasks",
        key="planning_tasks",
        height=180,
        placeholder="Write your task list here...",
    )

    st.text_area(
        "Roles",
        key="planning_roles",
        height=140,
        placeholder="Describe your role vs AI's role here...",
    )

# --------------------------
# Task tabs
# --------------------------
for i in range(1, st.session_state.num_tasks + 1):
    with tabs[i]:
        st.subheader(f"Task {i}")

        with st.form(f"task_form_{i}"):
            st.text_area(
                "Goal",
                key=f"goal_{i}",
                height=100,
                placeholder="What am I trying to figure out?",
            )

            st.text_area(
                "My idea",
                key=f"idea_{i}",
                height=100,
                placeholder="What do I already think? What am I unsure about?",
            )

            st.text_area(
                "Prompt",
                key=f"prompt_{i}",
                height=120,
                placeholder="Write the prompt to AI",
            )

            st.text_area(
                "AI response",
                key=f"ai_response_{i}",
                height=120,
                placeholder="Summarize AI's response in your own words",
            )

            st.text_area(
                "Evaluation",
                key=f"evaluation_{i}",
                height=120,
                placeholder="What seems useful? What needs checking?",
            )

            st.text_area(
                "Result",
                key=f"result_{i}",
                height=100,
                placeholder="What happened when you tested it?",
            )

            st.radio(
                "Next step",
                options=["Accept", "Revise prompt", "Change strategy"],
                key=f"decision_{i}",
                horizontal=True,
            )

            submitted = st.form_submit_button("Save task")

        if submitted:
            st.success(f"Task {i} saved.")

        hint_text = get_hint(st.session_state.get(f"decision_{i}", ""))
        if hint_text:
            st.info(hint_text)

# --------------------------
# Reflection tab
# --------------------------
with tabs[-1]:
    st.subheader("Final Reflection")

    st.text_area(
        "Reflection",
        key="reflection",
        height=180,
        placeholder="What did you learn about solving the problem and using AI?",
    )

# --------------------------
# Preview
# --------------------------
st.divider()
st.subheader("Preview of export data")
st.dataframe(export_dataframe(), use_container_width=True)
