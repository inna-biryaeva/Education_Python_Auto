test_subject_id = 999

def test_create_subject(db_client):
    db_client.delete_subject(test_subject_id)
    db_client.create_subject(test_subject_id, "Astronomy_" + str(test_subject_id))
    row = db_client.get_subject(test_subject_id)
    assert row is not None
    assert row[0] == "Astronomy_" + str(test_subject_id)
    db_client.delete_subject(test_subject_id)

def test_update_subject(db_client):
    db_client.delete_subject(test_subject_id)
    db_client.create_subject(test_subject_id, "Astronomy_" + str(test_subject_id))
    db_client.update_subject(test_subject_id, "Astrophysics_" + str(test_subject_id))
    row = db_client.get_subject(test_subject_id)
    assert row[0] == "Astrophysics_" + str(test_subject_id)
    db_client.delete_subject(test_subject_id)

def test_delete_subject(db_client):
    db_client.delete_subject(test_subject_id)
    db_client.create_subject(test_subject_id, "Astronomy_" + str(test_subject_id))
    db_client.delete_subject(test_subject_id)
    row = db_client.get_subject(test_subject_id)
    assert row is None
