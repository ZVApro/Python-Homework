def test_select(subject_db):
    """Тест выборки данных по ID."""
    test_id = 996
    test_title = "Test for Select"

    # Добавляем тестовую запись
    subject_db.insert(test_title, test_id)

    # Получаем запись именно по созданному ID
    result = subject_db.get_by_id(test_id)

    assert result is not None, f"Запись с ID {test_id} не найдена в БД"
    assert result['subject_id'] == test_id, f"Ожидался ID {test_id}, но получен {result['subject_id']}"
    assert result['subject_title'] == test_title, f"Ожидался заголовок '{
    test_title}', но получен '{result['subject_title']}'"

    # Удаляем тестовую запись
    subject_db.delete(test_id)


def test_insert_subject(subject_db):
    subject_id = 999
    subject_title = "Test Subject"

    subject_db.insert(subject_title, subject_id)
    result = subject_db.get_by_id(subject_id)

    assert result is not None
    assert result['subject_id'] == subject_id
    assert result['subject_title'] == subject_title


def test_update_subject(subject_db):
    subject_id = 998
    initial_title = "Initial Title"
    updated_title = "Updated Title"

    subject_db.insert(initial_title, subject_id)
    subject_db.update(subject_id, updated_title)
    result = subject_db.get_by_id(subject_id)

    assert result is not None
    assert result['subject_id'] == subject_id
    assert result['subject_title'] == updated_title


def test_delete_subject(subject_db):
    """Тест удаления сущности."""
    subject_id = 997
    subject_title = "To Be Deleted"

    subject_db.insert(subject_title, subject_id)
    subject_db.delete(subject_id)
    result = subject_db.get_by_id(subject_id)

    assert result is None
