import pytest

@pytest.fixture
def sample_employees():
    return [
        {'name': 'Bob Smith', 'department': 'Design', 'hours': 150, 'rate': 40},
        {'name': 'Carol Williams', 'department': 'Design', 'hours': 170, 'rate': 60},
        {'name': 'Alice Johnson', 'department': 'Marketing', 'hours': 160, 'rate': 50},
    ]