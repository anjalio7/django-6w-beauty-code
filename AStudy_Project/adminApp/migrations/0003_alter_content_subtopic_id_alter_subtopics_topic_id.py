# Generated by Django 4.0.6 on 2022-07-25 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_alter_subtopics_iframe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='subtopic_id',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='subtopic_id', to='adminApp.subtopics'),
        ),
        migrations.AlterField(
            model_name='subtopics',
            name='topic_id',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='topic_id', to='adminApp.topics'),
        ),
    ]