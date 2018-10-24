"""
This test case test the REST API
api/applications.py
"""

from __future__ import absolute_import
import json
from .base import MyTestCase

class APIApplicationsResolverTestCase(MyTestCase):

    def test_get_applications(self):
        with self.app.test_request_context('/application/',
                                           method='GET',
                                           headers={'Authorization': self.at}):
            res = self.app.full_dispatch_request()
            self.assertTrue(res.status_code == 200, res)
            result = res.get_json().get("result")
            detail = res.get_json().get("detail")
            value = result.get("value")
            self.assertTrue("ssh" in list(value.keys()))
            self.assertTrue("luks" in list(value.keys()))
            self.assertTrue(value["ssh"]["options"]["optional"] == ["user"])
