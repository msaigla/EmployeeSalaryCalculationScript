from src.reports.payout_report import PayoutReport

def test_payout_report_output(sample_employees):
    report = PayoutReport(sample_employees).generate()

    assert "Design" in report
    assert "Bob Smith" in report
    assert "$6000" in report
    assert "$10200" in report
    assert "$16200" in report
    assert "Marketing" in report
    assert "$8000" in report