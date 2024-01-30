from django.contrib.auth import get_user_model
from django.test.testcases import TestCase


User = get_user_model()


class TestStaffView(TestCase):

    def setUp(self):
        super().setUp()
        self.user = User.objects.create_user('admin', password='foobar', is_staff=True)

    def test_get(self):
        self.client.login(username='admin', password='foobar')
        response = self.client.get('/testapp/add-user/')
        self.assertEqual(response.status_code, 200)

    def test_get_not_logged_in(self):
        response = self.client.get('/testapp/add-user/')
        self.assertEqual(response.status_code, 302)

    def test_get_permission_denied(self):
        User.objects.create_user('admin2', password='foobar')
        self.client.login(username='admin2', password='foobar')
        response = self.client.get('/testapp/add-user/')
        self.assertEqual(response.status_code, 403)

    def test_post(self):
        self.client.login(username='admin', password='foobar')
        response = self.client.post('/testapp/add-user/', {
            'username': 'johndoe',
            'email': 'johndoe@example.com'
        })
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username='johndoe')
        self.assertEqual(user.email, 'johndoe@example.com')

    def test_post_with_error(self):
        self.client.login(username='admin', password='foobar')
        response = self.client.post('/testapp/add-user/', {
            'username': '',
            'email': 'johndoe@example.com'
        })
        self.assertEqual(response.status_code, 200)
