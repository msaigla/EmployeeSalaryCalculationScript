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
    parser = argparse.ArgumentParser(description="Employee report generator")
    parser.add_argument('files', nargs='+', help="One or more CSV files with employee data")
    parser.add_argument('--report', required=True, choices=REPORTS.keys(), help="Type of report to generate")
    args = parser.parse_args()

    employees = []

    for file in args.files:
        path = Path(file)
        if not path.exists() or not path.is_file():
            print(f"Ошибка: файл '{file}' не найден или не является файлом.", file=sys.stderr)
            sys.exit(1)
        try:
            employees.extend(read_employees(file))
        except Exception as e:
            print(f"Ошибка при чтении файла '{file}': {e}", file=sys.stderr)
            sys.exit(1)

    try:
        report_class = REPORTS[args.report]
        report = report_class(employees).generate()
        print(report)
    except Exception as e:
        print(f"Ошибка при генерации отчёта: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()