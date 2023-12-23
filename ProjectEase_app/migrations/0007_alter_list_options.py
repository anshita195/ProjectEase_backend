

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectEase_app', '0006_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['id']},
        ),
    ]
