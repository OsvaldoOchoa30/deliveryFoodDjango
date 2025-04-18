# Generated by Django 5.1.6 on 2025-02-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacionc1', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderproduct',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.AddConstraint(
            model_name='orderproduct',
            constraint=models.UniqueConstraint(fields=('id_order', 'id_product'), name='unique_order_product'),
        ),
    ]
