# Generated by Django 3.2.12 on 2023-12-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_auto_20231223_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('Book', 'Book'), ('Electronics', 'Electronics'), ('Foods', 'Foods'), ('Ferniture', 'Ferniture'), ('Cloths', 'cloths')], max_length=50, null=True)),
                ('item_name', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('receive_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('receive_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_quantity', models.IntegerField(blank=True, default='0', null=True)),
                ('issue_by', models.CharField(blank=True, max_length=50, null=True)),
                ('issue_to', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by', models.CharField(blank=True, max_length=50, null=True)),
                ('reorder_level', models.IntegerField(blank=True, default='0', null=True)),
                ('last_updated', models.DateTimeField(null=True)),
                ('timestamp', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(blank=True, choices=[('Book', 'Book'), ('Electronics', 'Electronics'), ('Foods', 'Foods'), ('Ferniture', 'Ferniture'), ('Cloths', 'cloths')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]