from django.test import TestCase

from singleactiveobject.tests.models import SingleActiveObject


class ModelTestCase(TestCase):
    def setUp(self):
        self.objects = []
        for i in range(0,3):
            obj = SingleActiveObject()
            obj.save()
            self.objects.append(obj)

    def test_save(self):
        self.objects[0].active  = True
        self.objects[0].save()
        self.assertTrue(self.objects[0].active)

        self.objects[1].active  = True
        self.objects[1].save()
        # reload
        self.objects[0] = SingleActiveObject.objects.get(pk=self.objects[0].pk)
        self.assertFalse(self.objects[0].active)
        self.assertTrue(self.objects[1].active)

    def test_state_string(self):
        self.assertEqual(self.objects[0].get_state_string(), "not active")
        self.objects[0].active = True
        self.assertEqual(self.objects[0].get_state_string(), "active")

