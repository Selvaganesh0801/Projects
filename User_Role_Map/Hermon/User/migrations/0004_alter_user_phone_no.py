# Generated by Django 3.2.25 on 2024-03-14 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_rename_user_user_role_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
