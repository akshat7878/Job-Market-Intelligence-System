import streamlit as st
import plotly.express as px
import sqlite3
import pandas as pd

st.sidebar.title("Analysis")

page = st.sidebar.selectbox(
    "Select Dashboard",
    [
        "Overview",
        "Skills",
        "Industries",
        "Salary Analysis"
    ]
)

@st.cache_data
def run_query_from_file(sql_file):
    conn = sqlite3.connect("jobs.db")

    with open(f"sql/{sql_file}", "r") as f:
        query = f.read()

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

@st.cache_data
def run_query(query):
    conn = sqlite3.connect("jobs.db")

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

st.set_page_config(
    page_title="Job Market Intelligence System",
    layout="wide"
)

st.title("📊 Job Market Intelligence System")

st.markdown(
    """
    Analyze job market trends using LinkedIn job postings.
    """
)



if page == "Overview":
    jobs = run_query(
        "SELECT COUNT(*) AS total FROM postings"
    )

    companies = run_query(
        "SELECT COUNT(*) AS total FROM companies"
    )

    skills = run_query(
        "SELECT COUNT(*) AS total FROM skills"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Jobs",
        f"{jobs.iloc[0]['total']:,}"
    )

    col2.metric(
        "Companies",
        f"{companies.iloc[0]['total']:,}"
    )

    col3.metric(
        "Skills",
        f"{skills.iloc[0]['total']:,}"
    )

elif page == "Skills":
    top_skills = run_query_from_file("top_skills.sql")

    fig = px.bar(
        top_skills,
        x="skill_name",
        y="demand",
        title="Top Skill Categories"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Skills")
    st.dataframe(
        top_skills,
        use_container_width=True
    )

elif page == "Industries":
    top_industries = run_query_from_file("top_industries.sql")

    fig = px.bar(
        top_industries,
        x="industry_name",
        y="jobs_posted",
        title="Top Industries"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Industries")
    st.dataframe(
        top_industries,
        use_container_width=True
    )

elif page == "Salary Analysis":
    highest_paying = run_query_from_file("highest_paying_skill.sql")

    fig = px.bar(
        highest_paying,
        x="skill_name",
        y="avg_salary",
        title="Highest Paying Skills"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Highest Paying Skills")
    st.dataframe(
        highest_paying,
        use_container_width=True
    )
