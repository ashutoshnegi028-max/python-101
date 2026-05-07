from pydantic import BaseModel
from typing import Literal


StatusType = Literal['Overutilized', 'Optimally Utilized', 'Available for More Work']


class EmployeeMetric(BaseModel):
    employee_name: str
    team: str
    shift: str
    process_name: str
    transaction_count: int
    calls_handled: int
    avg_handling_time_minutes: float
    login_hours: float
    productive_hours: float
    utilization_pct: float
    capacity_pct: float
    status: StatusType


class KPIResponse(BaseModel):
    total_transactions: int
    total_calls: int
    avg_utilization_pct: float
    overloaded_count: int
    available_capacity_count: int


class DashboardResponse(BaseModel):
    kpis: KPIResponse
    employees: list[EmployeeMetric]
