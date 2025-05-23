# Generated by Django 4.2.17 on 2025-05-10 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='part_of_speech',
            field=models.CharField(blank=True, choices=[('verb', 'Verb'), ('noun', 'Noun'), ('i-adjective', 'I-Adjective'), ('na-adjective', 'Na-Adjective'), ('adverb', 'Adverb'), ('conjunction', 'Conjunction'), ('particle', 'Particle'), ('interjection', 'Interjection'), ('auxiliary-verb', 'Auxiliary Verb'), ('question-word', 'Question Word'), ('counter', 'Counter'), ('prefix', 'Prefix'), ('suffix', 'Suffix'), ('expression', 'Expression'), ('other', 'Other')], max_length=50, null=True),
        ),
    ]
