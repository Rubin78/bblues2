# Generated by Django 3.1.3 on 2020-11-19 10:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201118_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='homepagetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='date',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='intro',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='tags',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('carousel', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock())])))]))]),
        ),
        migrations.DeleteModel(
            name='HomePageGalleryImage',
        ),
        migrations.DeleteModel(
            name='HomePageTag',
        ),
    ]