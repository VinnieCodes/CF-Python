# Generated by Django 4.2.16 on 2024-10-30 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.FloatField(help_text='in US dollars $')),
                ('genre', models.CharField(choices=[('classic', 'Classic'), ('romantic', 'Romantic'), ('comic', 'Comic'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('educational', 'Educational')], default='cl', max_length=12)),
                ('book_type', models.CharField(choices=[('hardcover', 'Hard cover'), ('ebook', 'E-Book'), ('audiobook', 'Audiobook')], default='hc', max_length=12)),
            ],
        ),
    ]
