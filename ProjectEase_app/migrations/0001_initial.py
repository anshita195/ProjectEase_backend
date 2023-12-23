
import ProjectEase_app.utils
import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=40)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(blank=True, choices=[('h', 'high'), ('m', 'medium'), ('l', 'low')], max_length=1, null=True)),
                ('is_resolved', models.BooleanField(blank=True, null=True)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('wiki', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('locked', models.BooleanField(default=False)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('year1_visibility', models.BooleanField(default=True)),
                ('year2_visibility', models.BooleanField(default=True)),
                ('year3_visibility', models.BooleanField(default=True)),
                ('year4_visibility', models.BooleanField(default=True)),
                ('year5_visibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(max_length=60)),
                ('year', models.PositiveSmallIntegerField()),
                ('enabled', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('a', 'admin'), ('n', 'normal_user')], default='n', max_length=1)),
                ('email', models.EmailField(max_length=60)),
                ('enrollment_no', models.BigIntegerField(unique=True)),
                ('image', models.CharField(blank=True, max_length=400, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'unique_together': {('name', 'enrollment_no')},
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project_role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_role', models.CharField(choices=[('l', 'leader'), ('m', 'member')], max_length=1)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectEase_app.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='member',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField()),
                ('redirection_link', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('color', models.CharField(default=ProjectEase_app.utils.generate_unique_colour, max_length=7)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='ProjectEase_app.project')),
            ],
            options={
                'unique_together': {('name', 'project')},
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ProjectEase_app.card')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='assignees',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='card',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='ProjectEase_app.list'),
        ),
        migrations.AlterUniqueTogether(
            name='card',
            unique_together={('title', 'list')},
        ),
    ]
