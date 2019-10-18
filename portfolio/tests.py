from django.test import TestCase
from django.contrib.gis.geos import Point
from .models import Profile

class ProfileTestCase(TestCase):
    def setUp(self):

		# location1 = Point(longitude, latitude, srid=4326)
		# location2 = Point(longitude, latitude, srid=4326)

    def test_profile_is_created(self):
        """Test profile creation"""
        #TODO
        # profile1 = Profile.objects.get(id=1)
        # profile2 = Profile.objects.get(id=2)

        # self.assertNotEqual(profile1, None)
        # self.assertNotEqual(profile2, None)
        # self.assertEqual(profile1.location, location1)
        # self.assertEqual(profile2.location, location2)

    def test_profile_update(self):
        """Profile should be updated"""
        # TODO add logic to test if profile and its fields
        # can be updated


        # self.assertEqual(
        # 	profile1.fields_values, 
        # 	new_fields_values)
        # self.assertEqual(profile2.fields_values, 
        # 	new_fields_values2)

    def test_profile_deletion(self):
        """Should delete profile with user"""
        # TODO add logic to test if profile can be
        # deleted 
