# Generated by Django 3.0.8 on 2020-07-16 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gildrose', '0003_remove_item_itemtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemType',
            field=models.CharField(default='reg', max_length=20),
        ),
    ]
