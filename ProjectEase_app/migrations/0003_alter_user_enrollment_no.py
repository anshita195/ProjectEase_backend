

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectEase_app', '0002_alter_user_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='enrollment_no',
            field=models.BigIntegerField(blank=True, null=True, unique=True),
        ),
    ]
