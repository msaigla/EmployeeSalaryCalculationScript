Python-скрипт для генерации различных отчётов по сотрудникам из CSV-файлов.

# Основные задачи:
1. Прочитать CSV-файлы с перемешанным порядком колонок и разными названиями поля со ставкой.
2. Посчитать payout как hours * rate.
3. Сгруппировать по департаментам.
4. Вывести отчёт по образцу.
5. Сделать код расширяемым для других видов отчётов.
6. Использовать только стандартную библиотеку (кроме тестов).
7. Не использует стандартную библиотеку csv.

## ✅ Поддерживаемые отчёты

- `payout` — итоговая зарплата сотрудников по отделам

### 🔧 Требования

- Python 3.10+

### 🏃 Запуск

MAC OS или Linux:
```bash
python3 src/main.py file1.csv file2.csv --report payout
```
Windows
```bash
python src/main.py file1.csv file2.csv --report payout
```
Аргументы:

- `file1.csv file2.csv ...` — один или несколько CSV-файлов
- `--report payout|avg` — тип отчёта

---

## 🧪 Тесты

```bash
pip install pytest
pytest
```

---

## 🛠 Как добавить новый отчёт

Система устроена так, чтобы **удобно добавлять новые типы отчётов**.

### 🔁 Шаги

1. **Создай файл нового отчёта**  
   Например: `src/reports/custom_report.py`

2. **Создай класс, наследующий `BaseReport`**:

```python
# src/reports/custom_report.py

from src.reports.base import BaseReport

class CustomReport(BaseReport):
    def generate(self):
        lines = ["Custom Report"]
        for emp in self.employees:
            lines.append(f"{emp['name']} ({emp['department']}) — rate: {emp['rate']}")
        return '\n'.join(lines)
```

3. **Зарегистрируй отчёт в `main.py`:**

```python
from src.reports.custom_report import CustomReport

REPORTS = {
    "payout": PayoutReport,
    "avg": AvgReport,
    "custom": CustomReport,  # ➕ добавлено
}
```

4. **Запусти:**

```bash
python3 main.py data.csv --report custom
```

---

## 📂 Структура проекта

```
project/
├── src/
│   ├── main.py
│   ├── utils/
│   │   └── reader.py
│   └── reports/
│       ├── base.py
│       ├── payout_report.py
│       ├── avg_report.py
│       └── custom_report.py
├── tests/
│   ├── test_reader.py
│   ├── test_payout_report.py
└── README.md
```