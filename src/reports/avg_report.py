from collections import defaultdict
from typing import Dict, List

from src.reports.base import BaseReport

class AvgReport(BaseReport):
    def generate(self) -> str:
        departments: Dict[str, List[tuple[str, int]]] = defaultdict(list)
        for emp in self.employees:
            departments[emp['department']].append((emp['name'], emp['rate']))

        lines: List[str] = []
        for dept, emps in departments.items():
            lines.append(dept)
            total = 0
            for name, rate in sorted(emps, key=lambda x: x[0]):
                total += rate
                lines.append(f"{'':>15}{name:<20}{rate}")
            avg = total // len(emps)
            lines.append(f"{'':>15}{'':<20}avg: {avg}")
            lines.append("")
        return '\n'.join(lines)