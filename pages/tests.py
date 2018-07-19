import pytest
# from django.conf import settings
# from django.test import Client
# from django.urls import reverse


from website.django_assertions import dj_assert_template_used


@pytest.fixture
def home_resp(client):
    return client.get('/', secure=True)


def test_home_status_code(home_resp):
    assert 200 == home_resp.status_code


def test_home_template(home_resp):
    dj_assert_template_used(home_resp, template_name='pages/index.html')
