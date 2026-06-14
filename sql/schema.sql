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
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE skills (
    skill_abr TEXT PRIMARY KEY,
    skill_name TEXT
);

CREATE TABLE industries (
    industry_id INTEGER PRIMARY KEY,
    industry_name TEXT
);

