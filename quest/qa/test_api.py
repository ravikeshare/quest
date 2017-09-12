from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase
from rest_framework import status
from quest.tenant.models import Tenant
import time

import datetime

class QuestionAPITest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test',
            'test@test.com',
            'test',
        )
        self.tenant = Tenant.objects.create(name="t1", api_key="123456")

    def test_post_fails(self):
        tenant_api_key = self.tenant.api_key
        response = self.client.post("http://localhost:8200/api/v1/qa/"+tenant_api_key+"/", data={
            'title': 'My new question',
        })
        print("response.status_code ", response.status_code)
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def test_get_wrong_api_key(self):
        response = self.client.get("http://localhost:8200/api/v1/qa/111111/")
        print(" test_get_wrong_api_key: status_code ", response.status_code)
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_tenant_throttle(self):

        self.tenant.remaining_access_count = 0
        self.tenant.save()
        tenant_api_key = self.tenant.api_key

        allowed = self.tenant.is_access_allowed()
        self.assertEqual(allowed, False)
        print("before sleep DateTime " + time.strftime("%c"))
        time.sleep(10)
        print("after sleep DateTime" + time.strftime("%c"))
        allowed = self.tenant.is_access_allowed()
        self.assertEqual(allowed, True)
