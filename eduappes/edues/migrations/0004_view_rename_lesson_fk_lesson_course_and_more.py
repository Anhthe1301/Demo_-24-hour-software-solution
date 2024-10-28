# Generated by Django 5.1.2 on 2024-10-27 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edues', '0003_alter_course_unique_together_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('view_count', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson_fk',
            new_name='course',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='acctive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='update_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
