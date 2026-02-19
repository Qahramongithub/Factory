from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db.models import TextChoices, CharField, ForeignKey, CASCADE, Model, DecimalField, TextField, DateTimeField


class User(AbstractUser):
    class Role(TextChoices):
        ADMIN = 'admin', 'Admin'
        USER = 'user', 'User'

    role = CharField(max_length=10, choices=Role.choices, default=Role.USER)
    user = ForeignKey('User', on_delete=CASCADE,
                      related_name='users', blank=True, null=True
                      )
    phone_number = CharField(max_length=14, null=True, blank=True)


class LeadSourceMapping(Model):
    platform = CharField(max_length=100, null=True, blank=True)
    source_id = CharField(max_length=100, null=True, blank=True)
    user = ForeignKey('User', on_delete=CASCADE, null=True,
                      related_name='leads', related_query_name='lead')


class Status(Model):
    name = CharField(max_length=100, unique=True)


class Lead(Model):
    full_name = CharField(max_length=100)
    phone_number = CharField(max_length=20)
    description = TextField()
    status = ForeignKey('Status', on_delete=CASCADE,
                        related_name='leads', default='NEW')
    price = DecimalField(max_digits=10, decimal_places=2)
    user = ForeignKey('User', on_delete=CASCADE, blank=True, null=True)
    source = ForeignKey('LeadSourceMapping', on_delete=CASCADE, null=True, blank=True)


class Meeting(Model):
    lead = ForeignKey('Lead', on_delete=CASCADE)
    date_time = DateTimeField()
    location = TextField()
    description = TextField()


class Category(Model):
    name = CharField(max_length=100, unique=True)


class Product(Model):
    UNIT_CHOICES = (
        ('pcs', 'Dona'),
        ('kg', 'Kilogramm'),
        ('l', 'Litr'),
        ('m', 'Metr'),
    )
    name = CharField(max_length=100)
    price = DecimalField(max_digits=10, decimal_places=2)
    quantity = DecimalField(max_digits=10, decimal_places=2)
    category = ForeignKey('Category', on_delete=CASCADE)
    color = CharField(max_length=100, blank=True, null=True)

    discount_price = DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    unit = CharField(
        max_length=10,
        choices=UNIT_CHOICES,
        default='pcs'
    )

    def __str__(self):
        return self.name


class OrderStatus(Model):
    name = CharField(max_length=100, unique=True)


class Order(Model):
    lead = ForeignKey('Lead', on_delete=CASCADE)
    status = ForeignKey('OrderStatus', on_delete=CASCADE)
    total_price = DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )
    created_at = DateTimeField(auto_now_add=True)


class OrderItem(Model):
    order = ForeignKey(
        Order,
        on_delete=CASCADE,
        related_name='items'
    )
    product = ForeignKey(
        Product,
        on_delete=CASCADE
    )
    quantity = DecimalField(max_digits=10, decimal_places=2)

    price = DecimalField(max_digits=10, decimal_places=2)
    color = CharField(max_length=100, blank=True, null=True)

    def get_total_price(self):
        return self.quantity * self.price
