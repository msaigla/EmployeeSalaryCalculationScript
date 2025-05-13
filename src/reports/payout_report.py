from collections import defaultdict
from typing import Dict, List

from src.reports.base import BaseReport

class PayoutReport(BaseReport):
    def generate(self) -> str:
        departments: Dict[str, List[tuple[str, int, int, int]]] = defaultdict(list)
        for emp in self.employees:
            payout = emp['hours'] * emp['rate']
            departments[emp['department']].append((emp['name'], emp['hours'], emp['rate'], payout))

        lines: List[str] = []
        for dept in sorted(departments):
            lines.append(dept)
            total = 0
            for name, hours, rate, payout in sorted(departments[dept], key=lambda x: x[0]):
                total += payout
                lines.append(f"{'':>15}{name:<20}{hours:<10}{rate:<10}${payout}")
            lines.append(f"{'':>35}${total}")
            lines.append("")
        return '\n'.join(lines)