# Generated by Django 4.1 on 2022-12-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0005_award_section_link_alter_award_section_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='no_of_views',
        ),
        migrations.RemoveField(
            model_name='information',
            name='no_of_visted',
        ),
        migrations.AddField(
            model_name='information',
            name='sessionKey',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]