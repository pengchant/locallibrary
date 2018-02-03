from django.test import TestCase

# class YourTestClass(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         print('setupdata:run once to setup non-modified data for all class methods.')
#         pass

#     def setUp(self):
#         print('setup:run once for every test method to setup clean data.')
#         pass

#     def test_false_is_false(self):
#         print('Mehod:test_false_is_false')
#         self.assertFalse(False)

#     def test_false_is_true(self):
#         print("method:test_false_is_true.")
#         self.assertTrue(True)

#     def test_one_plus_one_equals_two(self):
#         print('Method:test_one_plus_one_equals_two.')
#         self.assertEqual(1+1,2)

from catalog.models import Author

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big',last_name='Bob')

    def test_first_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_date_of_death_label(self):
        author = Author.objects.get(id = 1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label,'Died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id = 1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = '{0} , {1}'.format(author.last_name,author.first_name)
        self.assertEquals(expected_object_name,str(author))
    
    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(),'/catalog/author/1')











