import argparse
import sys
from pathlib import Path
from typing import Type

sys.path.append(str(Path(__file__).parent.parent))

from src.utils.reader import read_employees
from src.reports.base import BaseReport
from src.reports.payout_report import PayoutReport
from src.reports.avg_report import AvgReport

REPORTS: dict[str, Type[BaseReport]] = {
    'payout': PayoutReport,
    'avg': AvgReport
}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='+')
    parser.add_argument('--report', required=True, choices=REPORTS.keys())
    args = parser.parse_args()

    employees = []
    for file in args.files:
        employees.extend(read_employees(file))

    report_class = REPORTS[args.report]
    report = report_class(employees).generate()
    print(report)

if __name__ == "__main__":
    main()