# Generated by Django 4.2.7 on 2024-01-07 08:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PublicId', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('FoodName', models.CharField(max_length=50)),
                ('FoodPrice', models.FloatField(default=5.0)),
                ('FoodDescription', models.CharField(max_length=200)),
                ('FoodStatus', models.BooleanField(default=True)),
                ('FuncStatus', models.BooleanField(default=True)),
                ('CategoryId', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.category')),
            ],
            options={
                'db_table': 'main.menu',
            },
        ),
    ]
