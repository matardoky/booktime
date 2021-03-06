# Generated by Django 3.1 on 2020-12-06 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_basket_basketline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(10, 'NEW'), (20, 'PAID'), (30, 'DONE')], default=10, max_length=4)),
                ('billing_name', models.CharField(max_length=60)),
                ('billing_address1', models.CharField(max_length=60)),
                ('billing_address2', models.CharField(blank=True, max_length=60)),
                ('billing_zip_code', models.CharField(max_length=12)),
                ('billing_city', models.CharField(max_length=60)),
                ('billing_country', models.CharField(max_length=3)),
                ('shipping_name', models.CharField(max_length=60)),
                ('shipping_address1', models.CharField(max_length=60)),
                ('shipping_address2', models.CharField(blank=True, max_length=60)),
                ('shipping_zip_code', models.CharField(max_length=12)),
                ('shipping_city', models.CharField(max_length=60)),
                ('shipping_country', models.CharField(max_length=3)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(10, 'NEW'), (20, 'PROCESSING'), (30, 'SENT'), (40, 'CANCELLED')], default=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='main.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product')),
            ],
        ),
    ]
