from django.core.urlresolvers import reverse_lazy
from django.test import Client
from rest_framework.renderers import JSONRenderer


__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Reversable(object):
    def get_absolute_url(self):
        return reverse_lazy(self._meta.model_name + '-detail', kwargs={'pk': self.pk})


class ImageCase(object):
    def test_has_image(self):
        self.assertTrue(hasattr(self.object, 'images'))
class AuditCase(object):
    def test_owner_has_permissions(self):
        self.assertTrue(
            self.object.owner.has_perm('view_' + self.object._meta.object_name.lower(),
                                       self.object))
        self.assertTrue(
            self.object.owner.has_perm('delete_' + self.object._meta.object_name.lower(),
                                       self.object))
        self.assertTrue(
            self.object.owner.has_perm('change_' + self.object._meta.object_name.lower(),
                                       self.object))
class RESTCase(object):
    """
    Mixin that combines common functionality for testing the REST API.
    By default will also test the list and absolute endpoints of a resource.
    To use this mixin the child testcase must create a self.object resource.
    """

    @classmethod
    def setUpClass(cls):
        from apps.accounts.factories import AccountFactory
        admin = AccountFactory(email="admin@admin.de")
        admin.set_password("admin")
        admin.is_superuser = True
        admin.save()

        RESTCase.c = Client()
        RESTCase.c.post('/login/',
                        data={'username': 'admin@admin.de', 'password': 'admin'})

    @classmethod
    def tearDownClass(cls):
        from apps.accounts.models import Account

        Account.objects.get(email="admin@admin.de").delete()



    def assert_create(self, url, data):
        response = RESTCase.c.post(url, data)
        try:
            self.assertEqual(response.status_code, 201)
        except AssertionError:
            print response.content
            print data
            raise

    def assert_retrieve(self, url):
        response = RESTCase.c.get(url)
        try:
            self.assertEqual(response.status_code, 200)
        except AssertionError:
            print response.content
            raise

    def assert_update(self, url, data):
        json = JSONRenderer().render(data)
        response = RESTCase.c.put(path=url, data=json, content_type='application/json')
        try:
            self.assertIn(response.status_code, [200, 202, 204])
        except AssertionError:
            print response.content
            raise


    def assert_delete(self, url):
        response = RESTCase.c.delete(path=url)
        try:
            self.assertIn(response.status_code, [200, 202, 204])
        except AssertionError:
            print response.content
            raise


    def setUp(self):
        super(RESTCase, self).setUp()
        if not hasattr(self, "url"):
            self.root = "/api"
            self.url = self.object.get_absolute_url()
            self.data = self.serializer_class(self.object).data
            self.group_url = reverse_lazy(
                self.object._meta.object_name.lower() + '-list')
    def test_rest(self):
        # def test_rest_update_resource(self):
        self.assert_update(self.url, self.data)
        self.assert_retrieve(self.url)
        # def test_rest_list_resource(self):
        self.assert_retrieve(self.group_url)
        #def test_rest_delete_resource(self):
        self.assert_delete(self.url)
        #def test_rest_create_resource(self):
        self.assert_create(self.group_url, self.data)


