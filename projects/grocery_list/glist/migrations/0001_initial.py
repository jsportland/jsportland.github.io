from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField()),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
