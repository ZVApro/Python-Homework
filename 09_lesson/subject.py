from sqlalchemy import create_engine, text

class Subject:
    def __init__(self):
        self.db_connection_string = "postgresql://postgres:456@localhost:5432/QA"
        self.db = create_engine(self.db_connection_string, echo=False)

    def select_all(self):
        with self.db.connect() as connection:
            result = connection.execute(text("SELECT * FROM subject"))
            return result.mappings().all()

    def insert(self, subject_title, subject_id):
        with self.db.connect() as connection:
            connection.execute(
                text("INSERT INTO subject (subject_title, subject_id) VALUES (:subject_title, :subject_id)"),
                {"subject_title": subject_title, "subject_id": subject_id}
            )

    def update(self, subject_id, new_title):
        with self.db.connect() as connection:
            connection.execute(
                text("UPDATE subject SET subject_title = :new_title WHERE subject_id = :subject_id"),
                {"new_title": new_title, "subject_id": subject_id}
            )

    def delete(self, subject_id):
        with self.db.connect() as connection:
            connection.execute(
                text("DELETE FROM subject WHERE subject_id = :subject_id"),
                {"subject_id": subject_id}
            )

    def get_by_id(self, subject_id):
        """Возвращает запись по конкретному ID."""
        with self.db.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM subject WHERE subject_id = :subject_id"),
                {"subject_id": subject_id}
            )
            row = result.mappings().first()
            return row