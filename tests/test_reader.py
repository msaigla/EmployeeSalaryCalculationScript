from src.utils.reader import read_employees
import tempfile

def test_read_employees_with_variants():
    content = """id,email,name,department,hours_worked,salary
1,a@a.com,Alice Johnson,Marketing,160,50
2,b@b.com,Bob Smith,Design,150,40
"""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
        f.write(content)
        f.seek(0)
        result = read_employees(f.name)

    assert len(result) == 2
    assert result[0]['name'] == 'Alice Johnson'
    assert result[0]['department'] == 'Marketing'
    assert result[0]['hours'] == 160
    assert result[0]['rate'] == 50