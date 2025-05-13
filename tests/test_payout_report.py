from pathlib import Path
from typing import List, Dict, Union

from src.utils.reader import read_employees
from src.reports.payout_report import PayoutReport

Employee = Dict[str, Union[str, int]]

def test_payout_report_output(sample_csv: Path) -> None:
    employees: List[Employee] = read_employees(str(sample_csv))
    report: str = PayoutReport(employees).generate()

    assert "Design" in report
    assert "$16200" in report
    assert "Marketing" in report
    assert "$8000" in report