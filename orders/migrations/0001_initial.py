# Generated by Django 2.2.4 on 2020-01-30 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20191120_1201'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.UUIDField(default=uuid.uuid4, help_text='Auto generated', unique=True)),
                ('cart_keys', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Started'), (1, 'Completed'), (2, 'Cancelled')], default=0)),
                ('source', models.CharField(default='Postman', max_length=100, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='CustomerSession', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Order Session',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=100, null=True)),
                ('razorpay_signature', models.CharField(blank=True, max_length=100)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100)),
                ('razor_order_id', models.CharField(max_length=100, null=True)),
                ('invoice_id', models.CharField(max_length=100, null=True)),
                ('payment_method', models.CharField(max_length=100, null=True)),
                ('payment_detail', models.CharField(max_length=100, null=True)),
                ('payment_status', models.PositiveSmallIntegerField(choices=[(0, 'Pending'), (1, 'Success'), (2, 'Cancelled By Seller'), (3, 'Cancelled By Buyer')], default=0)),
                ('is_multiple', models.BooleanField(default=False)),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('delivery_status', models.PositiveSmallIntegerField(choices=[(0, 'Started'), (1, 'Placed'), (1, 'Delivered'), (2, 'Cancelled By Seller'), (3, 'Cancelled By Buyer')], default=0)),
                ('source', models.CharField(default='Postman', max_length=100, null=True)),
                ('delivery_address', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='Customer', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='products.Products')),
                ('session_key', models.ForeignKey(db_column='OrderSession', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.OrderSession', to_field='session_key')),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
