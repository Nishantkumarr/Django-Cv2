# Generated by Django 3.1.2 on 2020-10-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cartoonizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('GR', 'grayscale')], default='GR', max_length=2)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
