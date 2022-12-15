# Generated by Django 4.0.4 on 2022-04-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('Ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('device_type', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='no_of_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='about',
            name='no_of_visted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contact',
            name='no_of_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contact',
            name='no_of_visted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contact',
            name='sent_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='no_of_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='home',
            name='no_of_visted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='work',
            name='no_of_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='work',
            name='no_of_visted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
