# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BlogParagraph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paragraph', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='blogparagraph',
            name='blog_post',
            field=models.ForeignKey(to='blog.BlogPost'),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='paragraph',
            field=models.ForeignKey(related_name='+', to='blog.BlogParagraph'),
        ),
    ]
