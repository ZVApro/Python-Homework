import pytest
import pytest
from subject import Subject

@pytest.fixture
def subject_db():
    """Фикстура для создания экземпляра Subject."""
    return Subject()

@pytest.fixture(autouse=True)
def clean_up_db(subject_db):

    yield
    # Удаляем созданные в тестах записи
    cleanup_ids = [999, 998, 997, 996]  # добавляем ID для теста select
    for subject_id in cleanup_ids:
        try:
            subject_db.delete(subject_id)
        except Exception as e:
            print(f"Ошибка при удалении ID {subject_id}: {e}")
