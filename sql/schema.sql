CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    company_size INTEGER,
    state TEXT,
    country TEXT,
    city TEXT,
    zip_code TEXT,
    address TEXT,
    url TEXT
);

CREATE TABLE postings (
    job_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    title TEXT,
    description TEXT,
    location TEXT,
    formatted_work_type TEXT,
    formatted_experience_level TEXT,
    remote_allowed INTEGER,
    work_type TEXT,
    currency TEXT,
    normalized_salary REAL,
    FOREIGN KEY (company_id) 
        REFERENCES companies(company_id)

);

CREATE TABLE skills (
    skill_abr TEXT PRIMARY KEY,
    skill_name TEXT
);

CREATE TABLE industries (
    industry_id INTEGER PRIMARY KEY,
    industry_name TEXT
);

CREATE TABLE job_skills (

    job_id INTEGER,
    skill_abr VARCHAR(20),

    PRIMARY KEY(job_id, skill_abr),

    FOREIGN KEY(job_id)
        REFERENCES postings(job_id),

    FOREIGN KEY(skill_abr)
        REFERENCES skills(skill_abr)

);

CREATE TABLE job_industries (

    job_id INTEGER,
    industry_id INTEGER,

    PRIMARY KEY(job_id, industry_id),

    FOREIGN KEY(job_id)
        REFERENCES postings(job_id),

    FOREIGN KEY(industry_id)
        REFERENCES industries(industry_id)

);

CREATE TABLE salaries (

    salary_id INTEGER PRIMARY KEY,
    job_id INTEGER,
    max_salary REAL,
    med_salary REAL,
    min_salary REAL,
    pay_period VARCHAR(20),
    currency VARCHAR(10),
    compensation_type VARCHAR(50),

    FOREIGN KEY(job_id)
        REFERENCES postings(job_id)

);