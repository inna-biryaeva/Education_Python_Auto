from sqlalchemy import create_engine, text

class Subject_db_client:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def create_subject(self, subject_id, title):
        connection = self.engine.connect()
        transaction = connection.begin()
        sql = text("INSERT INTO subject (subject_id, subject_title) VALUES (:id, :title)")
        connection.execute(sql, {"id": subject_id, "title": title})
        transaction.commit()
        connection.close()

    def get_subject(self, subject_id):
        connection = self.engine.connect()
        sql = text("SELECT subject_title FROM subject WHERE subject_id = :id")
        result = connection.execute(sql, {"id": subject_id})
        row = result.fetchone()
        connection.close()
        return row

    def update_subject(self, subject_id, new_title):
        connection = self.engine.connect()
        transaction = connection.begin()
        sql = text("UPDATE subject SET subject_title = :title WHERE subject_id = :id")
        connection.execute(sql, {"title": new_title, "id": subject_id})
        transaction.commit()
        connection.close()

    def delete_subject(self, subject_id):
        connection = self.engine.connect()
        transaction = connection.begin()
        sql = text("DELETE FROM subject WHERE subject_id = :id")
        connection.execute(sql, {"id": subject_id})
        transaction.commit()
        connection.close()
