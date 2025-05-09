from django.test import TestCase
from django.contrib.auth.models import User
from .models import Hilo, Mensaje

# Create your tests here.
class HiloTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'Hell3210')
        self.user2 = User.objects.create_user('user2', None, 'Hell3210')
        self.user3 = User.objects.create_user('user3', None, 'Hell3210')

        self.hilo1 = Hilo.objects.create()

    def test_anadir_usu_a_hilo(self):
        self.hilo1.users.add(self.user1, self.user2)
        self.assertEqual(len(self.hilo1.users.all()), 2)

    def test_filter_hilo_por_usu(self):
        self.hilo1.users.add(self.user1, self.user2)
        hilos = Hilo.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(self.hilo1, hilos[0])

    def test_filter_hilo_inexistente(self):
        hilos = Hilo.objects.filter(users=self.user1).filter(users=self.user2)
        self.assertEqual(0, len(hilos))

    def test_anadir_mensaje_a_hilo(self):
        self.hilo1.users.add(self.user1, self.user2)
        msj1 = Mensaje.objects.create(emisor=self.user1, contenido='Muy buenas por parte de usu1')
        msj2 = Mensaje.objects.create(emisor=self.user2, contenido='Hola por parte de usu2')
        self.hilo1.mensajes.add(msj1, msj2)
        self.assertEqual(len(self.hilo1.mensajes.all()), 2)

        for msj in self.hilo1.mensajes.all():
            print(f'{msj.fecha_emision} - ({msj.emisor.username}): {msj.contenido}')

    def test_anadir_msj_por_usu_no_dentro_hilo(self):
        self.hilo1.users.add(self.user1, self.user2)
        msj1 = Mensaje.objects.create(emisor=self.user1, contenido='Muy buenas por parte de usu1')
        msj2 = Mensaje.objects.create(emisor=self.user2, contenido='Hola por parte de usu2')
        msj3 = Mensaje.objects.create(emisor=self.user3, contenido='Hola usu3 está aquí también')
        self.hilo1.mensajes.add(msj1, msj2, msj3)
        self.assertEqual(len(self.hilo1.mensajes.all()), 2)

        for msj in self.hilo1.mensajes.all():
            print(f'{msj.fecha_emision} - ({msj.emisor.username}): {msj.contenido}')

    def test_find_hilo_custom(self):
        self.hilo1.users.add(self.user1, self.user2)
        hilo_encontrado = Hilo.objects.find(self.user1, self.user2)
        self.assertEqual(self.hilo1, hilo_encontrado)

    def test_find_or_create_hilo(self):
        self.hilo1.users.add(self.user1, self.user2)
        hilo_encontrado = Hilo.objects.find_or_create(self.user1, self.user2)
        self.assertEqual(self.hilo1, hilo_encontrado)
        hilo_creado = Hilo.objects.find_or_create(self.user1, self.user3)
        self.assertIsNotNone(hilo_creado)





