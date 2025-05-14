import pytest
from pathlib import Path
from src.main import main as run_main
import sys

from _pytest.monkeypatch import MonkeyPatch


def test_missing_file(monkeypatch: MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr(sys, "argv", ["main.py", "not_found.csv", "--report", "payout"])

    with pytest.raises(SystemExit) as e:
        run_main()

    assert e.value.code == 1
    captured = capsys.readouterr()
    assert "файл 'not_found.csv' не найден" in captured.err


def test_invalid_report(monkeypatch: MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setattr(sys, "argv", ["main.py", "data.csv", "--report", "nonexistent"])

    with pytest.raises(SystemExit) as e:
        run_main()

    assert e.value.code == 2
    captured = capsys.readouterr()
    assert "invalid choice" in captured.err.lower()


def test_broken_file(monkeypatch: MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    bad_file: Path = Path("tests/bad.csv")
    bad_file.write_text("")

    monkeypatch.setattr(sys, "argv", ["main.py", str(bad_file), "--report", "payout"])

    with pytest.raises(SystemExit) as e:
        run_main()

    assert e.value.code == 1
    captured = capsys.readouterr()
    assert "Ошибка при чтении файла" in captured.err