BEGIN;

INSERT INTO teams(name) VALUES ('Team Alpha'), ('Team Beta');
INSERT INTO employees(employee_name, team_id, shift, role) VALUES
('Ava Johnson',1,'Morning','Manager'),
('Noah Smith',1,'Morning','Viewer'),
('Mia Patel',2,'Evening','Viewer');

INSERT INTO process_metrics(employee_id, process_name, metric_date, transaction_count, calls_handled, avg_handling_time_minutes, login_hours, productive_hours) VALUES
((SELECT id FROM employees WHERE employee_name = 'Ava Johnson'),'Claims','2026-05-06',142,39,7.10,8.00,7.60),
((SELECT id FROM employees WHERE employee_name = 'Noah Smith'),'KYC','2026-05-06',86,25,8.00,8.00,5.00),
((SELECT id FROM employees WHERE employee_name = 'Mia Patel'),'Payments','2026-05-06',110,31,6.20,8.00,7.10);

COMMIT;
