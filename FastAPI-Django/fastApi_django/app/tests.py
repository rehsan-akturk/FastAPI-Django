from django.test import SimpleTestCase
from django.urls import reverse  


###########test get dirvers limit 50   ##############
class Driverall(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get(reverse("driver_get_all"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get(reverse("driver_get_all"))
        self.assertTemplateUsed(response, "driver.html")

    def test_template_content(self):
        response = self.client.get(reverse("driver_get_all"))
        self.assertContains(response, " <h2>Driver List</h2>")
        self.assertNotContains(response, "Not on the page")



########### test get dirvers with params limit 50   ##############
class Driver(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/driver_driver/2022-03-01/2022-03-05/1.26/3.3")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):  
        response = self.client.get("/driver_driver/2022-03-01/2022-03-05/1.26/3.3")
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):  
        response = self.client.get("/driver_driver/2022-03-01/2022-03-05/1.26/3.3")
        self.assertTemplateUsed(response, "driver_filter.html")

    def test_template_content(self):
        response = self.client.get("/driver_driver/2022-03-01/2022-03-05/1.26/3.3")
        self.assertContains(response, " <h2>Driver List</h2>")
        self.assertNotContains(response, "Not on the page")
