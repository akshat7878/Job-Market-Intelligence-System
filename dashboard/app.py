import streamlit as st
import plotly.express as px
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="Job Market Intelligence System",
    layout="wide"
)

st.sidebar.title("Analysis")

page = st.sidebar.selectbox(
    "Select Dashboard",
    [
        "Overview",
        "Job Title",
        "Skills",
        "Companies",
        "Industries",
        "Salary Analysis",
        "Demand vs Salary",
        "Remote vs Onsite",
        "Geographic Analysis"
    ]
)

@st.cache_data
def run_query_from_file(sql_file):
    with open(f"sql/{sql_file}", "r") as f:
        query = f.read()

    return query

@st.cache_data
def run_query(query):
    conn = sqlite3.connect("jobs_demo.db")

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df

def download_csv(df, filename):
    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        f"{filename}.csv",
        "text/csv"
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

    industries = run_query(
        "SELECT COUNT(*) AS total FROM industries"
    )

    col1, col2, col3, col4 = st.columns(4)

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

    col4.metric(
        "Industries",
        f"{industries.iloc[0]['total']:,}"
    )

    st.info(
        f"""
        This dashboard analyzes {jobs.iloc[0]['total']:,} LinkedIn job postings,
        {companies.iloc[0]['total']:,} companies, {skills.iloc[0]['total']:,} skill categories and {industries.iloc[0]['total']:,}
         industries.
        """
    )

elif page == "Job Title":
    top_jobs_titles = run_query(run_query_from_file("top_jobs_titles.sql"))

    fig = px.bar(
        top_jobs_titles,
        y="title",
        x="jobs",
        orientation="h",
        title="Top Jobs Titles"
    )
    fig.update_layout(
        xaxis_title="Jobs Titles",
        yaxis_title="Demand"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Jobs Titles")
    st.dataframe(
        top_jobs_titles,
        use_container_width=True
    )

    download_csv(top_jobs_titles, "top_jobs_titles")

elif page == "Skills":
    top_skills = run_query(run_query_from_file("top_skills.sql"))

    fig = px.bar(
        top_skills,
        x="skill_name",
        y="demand",
        title="Top Skill Categories"
    )
    fig.update_layout(
        xaxis_title="Skills",
        yaxis_title="Demand"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Skills")
    st.dataframe(
        top_skills,
        use_container_width=True
    )

    download_csv(top_skills, "top_skills")

elif page == "Companies":
    top_companies = run_query(run_query_from_file("top_companies.sql"))

    fig = px.bar(
        top_companies,
        x="jobs_posted",
        y="name",
        orientation="h",
        title="Top Companies"
    )
    fig.update_layout(
        xaxis_title="Companies",
        yaxis_title="Jobs Posted"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Companies")
    st.dataframe(
        top_companies,
        use_container_width=True
    )
    
    download_csv(top_companies, "top_companies")

elif page == "Industries":
    top_industries = run_query(run_query_from_file("top_industries.sql"))

    fig = px.bar(
        top_industries,
        y="industry_name",
        x="jobs_posted",
        orientation="h",
        title="Top Industries"
    )
    fig.update_layout(
        xaxis_title="Industries",
        yaxis_title="Jobs Posted"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Industries")
    st.dataframe(
        top_industries,
        use_container_width=True
    )

    download_csv(top_industries, "top_industries")

elif page == "Salary Analysis":
    highest_paying_skill = run_query(run_query_from_file("highest_paying_skill.sql"))
    highest_paying_industries = run_query(run_query_from_file("highest_paying_industries.sql"))
    salary_by_exp = run_query(run_query_from_file("salary_by_exp.sql"))
    salary_by_work_type = run_query(run_query_from_file("salary_by_work_type.sql"))

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Highest Paying Skills",
            "Highest Paying Industries",
            "Salary By Experience",
            "Salary By Work Type"
        ]
    )

    with tab1:
        fig = px.bar(
            highest_paying_skill,
            x="skill_name",
            y="avg_salary",
            title="Highest Paying Skills"
        )
        fig.update_layout(
            xaxis_title="Skill",
            yaxis_title="Average Salary"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Highest Paying Skills")
        st.dataframe(
            highest_paying_skill,
            use_container_width=True
        )

        download_csv(highest_paying_skill, "highest_paying_skill")

    with tab2:
        fig = px.bar(
            highest_paying_industries,
            x="industry_name",
            y="avg_salary",
            title="Highest Paying Industries"
        )
        fig.update_layout(
            xaxis_title="Industry",
            yaxis_title="Average Salary"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Highest Paying Industries")
        st.dataframe(
            highest_paying_industries,
            use_container_width=True
        )

        download_csv(highest_paying_industries, "highest_paying_industries")

    with tab3:
        fig = px.bar(
            salary_by_exp,
            x="formatted_experience_level",
            y="avg_salary",
            title="Salary by Experience"
        )
        fig.update_layout(
            xaxis_title="Experience Level",
            yaxis_title="Average Salary"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Salary by Experience")
        st.dataframe(
            salary_by_exp,
            use_container_width=True
        )

        download_csv(salary_by_exp, "salary_by_exp")

    with tab4:
        fig = px.bar(
            salary_by_work_type,
            x="work_type",
            y="avg_salary",
            title="Salary By Work Type"
        )
        fig.update_layout(
            xaxis_title="Work Type",
            yaxis_title="Average Salary"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Salary By Work Type")
        st.dataframe(
            salary_by_work_type,
            use_container_width=True
        )

        download_csv(salary_by_work_type, "salary_by_work_type")

elif page == "Demand vs Salary":
    demand_vs_salary = run_query(run_query_from_file("skill_demand_vs_salary.sql"))

    fig = px.scatter(
        demand_vs_salary,
        x="demand",
        y="avg_salary",
        hover_name="skill_name",
        size="demand",
        title="Skill Demand vs Salary"
    )

    fig.update_layout(
        xaxis_title="Demand",
        yaxis_title="Average Salary"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Salary By Work Type")
    st.dataframe(
        demand_vs_salary,
        use_container_width=True
    )

    download_csv(demand_vs_salary, "demand_vs_salary")

elif page == "Remote vs Onsite":
    remote_vs_onsite = run_query(run_query_from_file("remote_jobs.sql"))

    fig = px.bar(
        remote_vs_onsite,
        x="job_type",
        y="jobs",
        title="Remote vs Onsite"
    )

    fig.update_layout(
        xaxis_title="Job Type",
        yaxis_title="Demand"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Remote vs Onsite")
    st.dataframe(
        remote_vs_onsite,
        use_container_width=True
    )

    download_csv(remote_vs_onsite, "remote_vs_onsite")

elif page == "Geographic Analysis":
    geographic_analysis = run_query(run_query_from_file("top_hiring_cities.sql"))

    fig = px.bar(
        geographic_analysis,
        x="location",
        y="jobs",
        title="Geographic Analysis"
    )

    fig.update_layout(
        xaxis_title="Locations",
        yaxis_title="Demand"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Geographic Analysis")
    st.dataframe(
        geographic_analysis,
        use_container_width=True
    )

    download_csv(geographic_analysis, "geographic_analysis")

    
