# Generated by Django 3.2 on 2021-05-22 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('title', models.CharField(max_length=25)),
                ('Experience', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'db_table': 'Employee_details',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.employee')),
            ],
        ),
    ]