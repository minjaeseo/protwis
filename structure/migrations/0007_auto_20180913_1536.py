# Generated by Django 2.0.4 on 2018-09-13 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signprot', '0005_auto_20180809_1647'),
        ('structure', '0006_structure_signprot_complex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='structure',
            name='signprot_complex',
        ),
        migrations.AddField(
            model_name='structure',
            name='signprot_complex',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='signprot_complex', to='signprot.SignprotComplex'),
        ),
    ]
