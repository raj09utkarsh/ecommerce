# Generated by Django 2.2.4 on 2019-08-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default_course.jpg', upload_to='course')),
                ('description', models.TextField()),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('coursePrice', models.IntegerField()),
            ],
        ),
    ]