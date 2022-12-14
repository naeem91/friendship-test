# Generated by Django 4.1.2 on 2022-10-15 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='link',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
