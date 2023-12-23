

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectEase_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
