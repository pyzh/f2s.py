# Generated by Django 2.1.3 on 2018-11-14 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_id', models.CharField(max_length=36)),
                ('context', models.TextField(max_length=140)),
                ('time', models.DateTimeField(verbose_name='时间')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24)),
                ('url_id', models.CharField(max_length=36)),
                ('base', models.CharField(max_length=12)),
                ('type', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=360)),
                ('bio', models.TextField(max_length=1080)),
                ('email', models.CharField(max_length=64)),
                ('code', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='msg',
            name='p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ff.People'),
        ),
    ]