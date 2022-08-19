# Generated by Django 4.0.6 on 2022-08-09 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('online', '0008_rename_product_montre_product_enfant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('commande', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='commander',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commande', models.BooleanField(default=False)),
                ('date_commande', models.DateTimeField(blank=True, null=True)),
                ('articles', models.ManyToManyField(to='online.article')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=128)),
                ('price', models.FloatField(default=0.0)),
                ('stock', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='products')),
            ],
        ),
        migrations.DeleteModel(
            name='Product_enfant',
        ),
        migrations.DeleteModel(
            name='Product_femme',
        ),
        migrations.DeleteModel(
            name='Product_homme',
        ),
        migrations.AddField(
            model_name='article',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.product'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]