CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  name VARCHAR(80) NOT NULL
);

CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  employee_name VARCHAR(120) NOT NULL,
  team_id INT REFERENCES teams(id),
  shift VARCHAR(20) NOT NULL,
  role VARCHAR(20) NOT NULL DEFAULT 'Viewer'
);

CREATE TABLE process_metrics (
  id SERIAL PRIMARY KEY,
  employee_id INT REFERENCES employees(id),
  process_name VARCHAR(100) NOT NULL,
  metric_date DATE NOT NULL,
  transaction_count INT NOT NULL,
  calls_handled INT NOT NULL,
  avg_handling_time_minutes NUMERIC(5,2) NOT NULL,
  login_hours NUMERIC(5,2) NOT NULL,
  productive_hours NUMERIC(5,2) NOT NULL
);
