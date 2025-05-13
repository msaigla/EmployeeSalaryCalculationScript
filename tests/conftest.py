import sys
from pathlib import Path
from typing import Generator

import pytest

@pytest.fixture
def sample_csv() -> Generator[Path, None, None]:
    content: str = (
        "id,email,name,department,hours_worked,salary\n"
        "1,a@example.com,Alice,Marketing,160,50\n"
        "2,b@example.com,Bob,Design,150,40\n"
        "3,c@example.com,Carol,Design,170,60\n"
    )
    file_path: Path = Path("tests/test_data.csv")
    print( sys.path.append(str(Path(__file__).parent.parent)) )
    file_path.write_text(content, encoding="utf-8")
    yield file_path