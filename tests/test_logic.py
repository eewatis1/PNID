def test_index_status(client):
    rv = client.get('/')
    assert rv.status_code == 200

def test_api_post(client):
    rv = client.post('/api/add', json={'name': 'GithubActionTest'})
    assert rv.status_code == 201