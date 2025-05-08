from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.
# python manage.py test registration
class PerfilTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('nombre_test','correo_toto5@tata.com', 'cred_Hell3210', )
    
    def test_existencia_perfil(self):
        existe = Profile.objects.filter(user__username='nombre_test').exists()
        self.assertEqual(existe, True)
