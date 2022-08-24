# Generated by Django 4.0.6 on 2022-08-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0003_alter_content_subtopic_id_alter_subtopics_topic_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topics',
            name='topic_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='subtopics',
            unique_together={('topic_id', 'subtopic_name')},
        ),
    ]
