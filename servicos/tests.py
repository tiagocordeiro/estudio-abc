import pytest
# from django.conf import settings
# from django.test import Client
# from django.urls import reverse


# from website.django_assertions import dj_assert_template_used


@pytest.fixture
def servicos_home_resp(client):
    return client.get('/dashboard/servicos/', secure=True)


def test_servicos_home_status_code(servicos_home_resp):
    assert 302 == servicos_home_resp.status_code
