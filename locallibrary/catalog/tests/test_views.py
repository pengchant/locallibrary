from django.test import TestCase

from catalog.models import Author
from django.urls import reverse

class AuthorListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_authors = 13
        for author_num in range(number_of_authors):
            Author.objects.create(first_name='Christian{0}'.format(author_num),last_name='Surname{0}'.format(author_num))

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/catalog/authors')
        self.assertEqual(resp.status_code,200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('authors'))
        self.assertEqual(resp.status_code,200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('authors'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'catalog/author_list.html')        

    def test_pagination_is_five(self):
        resp = self.client.get(reverse('authors'))
        self.assertEqual(resp.status_code,200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['autor-list']==5))

    
    