from app.schemas.dashboard import EmployeeMetric, DashboardResponse, KPIResponse


def _status_from_utilization(utilization_pct: float) -> str:
    if utilization_pct > 90:
        return 'Overutilized'
    if utilization_pct >= 70:
        return 'Optimally Utilized'
    return 'Available for More Work'


def get_dashboard_data() -> DashboardResponse:
    rows = [
        {'employee_name': 'Ava Johnson', 'team': 'Team Alpha', 'shift': 'Morning', 'process_name': 'Claims', 'transaction_count': 142, 'calls_handled': 39, 'avg_handling_time_minutes': 7.1, 'login_hours': 8.0, 'productive_hours': 7.6},
        {'employee_name': 'Noah Smith', 'team': 'Team Alpha', 'shift': 'Morning', 'process_name': 'KYC', 'transaction_count': 86, 'calls_handled': 25, 'avg_handling_time_minutes': 8.0, 'login_hours': 8.0, 'productive_hours': 5.0},
        {'employee_name': 'Mia Patel', 'team': 'Team Beta', 'shift': 'Evening', 'process_name': 'Payments', 'transaction_count': 110, 'calls_handled': 31, 'avg_handling_time_minutes': 6.2, 'login_hours': 8.0, 'productive_hours': 7.1},
    ]
    employees: list[EmployeeMetric] = []
    for row in rows:
        utilization = round((row['productive_hours'] / row['login_hours']) * 100, 2)
        capacity = round(100 - utilization, 2)
        employees.append(EmployeeMetric(**row, utilization_pct=utilization, capacity_pct=capacity, status=_status_from_utilization(utilization)))

    return DashboardResponse(
        kpis=KPIResponse(
            total_transactions=sum(x.transaction_count for x in employees),
            total_calls=sum(x.calls_handled for x in employees),
            avg_utilization_pct=round(sum(x.utilization_pct for x in employees) / len(employees), 2),
            overloaded_count=sum(1 for x in employees if x.status == 'Overutilized'),
            available_capacity_count=sum(1 for x in employees if x.status == 'Available for More Work'),
        ),
        employees=employees,
    )
