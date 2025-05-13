from src.reports.avg_report import AvgReport

def test_avg_report_output(sample_employees):
    report = AvgReport(sample_employees).generate()

    assert "Design" in report
    assert "avg: 50" in report  # (40 + 60) / 2
    assert "Marketing" in report
    assert "avg: 50" in report  # only one employee
