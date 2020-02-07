from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=1000)),
                ('urlToImage', models.CharField(max_length=1000)),
                ('publishedAt', models.DateTimeField()),
            ],
            options={
                'db_table': 'news',
                'ordering': ['pk'],
            },
        ),
    ]
