from django.test import SimpleTestCase
from django.urls import reverse,resolve
from te.views import customer

class TestUrls(SimpleTestCase):

    def test_customer_url_is_resolved(self):
        url = reverse('customer',args=[999])
        self.assertEquals(resolve(url).func,customer)
        print("Tested customer url successfully")

