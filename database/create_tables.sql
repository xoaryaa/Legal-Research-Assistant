-- create_tables.sql
CREATE TABLE cases (
    case_id SERIAL PRIMARY KEY,
    case_name VARCHAR(255),
    court VARCHAR(255),
    decision_date DATE,
    summary TEXT
);

CREATE TABLE laws (
    law_id SERIAL PRIMARY KEY,
    law_name VARCHAR(255),
    description TEXT,
    jurisdiction VARCHAR(255)
);

CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,
    client_name VARCHAR(255),
    contact_info TEXT
);

CREATE TABLE research_notes (
    note_id SERIAL PRIMARY KEY,
    case_id INT REFERENCES cases(case_id),
    note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
