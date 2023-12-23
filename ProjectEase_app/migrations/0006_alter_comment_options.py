

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectEase_app', '0005_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at']},
        ),
    ]
