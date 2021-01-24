from fastapi.testclient import TestClient

from freezegun import freeze_time

from main import app

client = TestClient(app)


@freeze_time("2021-01-24")
def test_discover(user_location):
    lat = user_location[1]
    lon = user_location[0]
    response = client.post(f"/discover/?lat={lat}&lon={lon}")
    assert response.status_code == 200


@freeze_time("2021-01-24")
def test_discover_missing_request_parameters(user_location):
    lat = user_location[1]
    response = client.post(f"/discover/?lat={lat}")
    assert response.status_code == 422
