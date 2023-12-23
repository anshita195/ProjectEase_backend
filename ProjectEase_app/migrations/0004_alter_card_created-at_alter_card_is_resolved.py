

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectEase_app', '0003_alter_user_enrollment_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='card',
            name='is_resolved',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
