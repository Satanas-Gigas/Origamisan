# Generated by Django 4.2.17 on 2025-01-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_grammar_options_alter_grammar_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='part_of_speech',
            field=models.CharField(blank=True, choices=[('verb', 'Verb'), ('noun', 'Noun'), ('i-adjective', 'I-Adjective'), ('na-adjective', 'Na-Adjective'), ('question-word', 'Question Word'), ('counter_suffix', 'Counter Suffix')], max_length=50, null=True),
        ),
    ]
