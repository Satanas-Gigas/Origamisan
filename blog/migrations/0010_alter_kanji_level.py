# Generated by Django 4.2.17 on 2025-07-13 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_partofspeech_remove_word_part_of_speech_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanji',
            name='level',
            field=models.CharField(default='5', max_length=1),
        ),
    ]
