# Generated by Django 5.1.3 on 2024-11-30 13:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nama Kategori')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Deskripsi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Dibuat pada')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Diperbarui pada')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nama Produk')),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Deskripsi')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Harga')),
                ('stock_produk', models.PositiveIntegerField(verbose_name='Stok')),
                ('stock_diskon', models.PositiveIntegerField(verbose_name='Stok Diskon')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Dibuat pada')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Diperbarui pada')),
                ('is_active', models.BooleanField(default=True, verbose_name='Aktif')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shopkategori.category', verbose_name='Kategori')),
            ],
            options={
                'verbose_name': 'Produk',
                'verbose_name_plural': 'Produk',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shopkategori.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopkategori.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', to='shopkategori.product'),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopkategori.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopkategori.product')),
            ],
        ),
    ]