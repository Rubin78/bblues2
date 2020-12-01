# Generated by Django 3.1.3 on 2020-11-29 19:13

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20201129_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('carousel', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))])))])), ('product', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('cost', wagtail.core.blocks.IntegerBlock(required=False))])))])), ('categories', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('photo3', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock())])))])), ('blog', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('date', wagtail.core.blocks.DateBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('instagram', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('photo3', wagtail.images.blocks.ImageChooserBlock()), ('photo4', wagtail.images.blocks.ImageChooserBlock()), ('photo5', wagtail.images.blocks.ImageChooserBlock())])))])), ('indexcarousel', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('cost', wagtail.core.blocks.IntegerBlock())])))])), ('listing', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('cost', wagtail.core.blocks.IntegerBlock())])))])), ('lookbook', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('text1', wagtail.core.blocks.CharBlock())])))])), ('cta', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('partner', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock())])))])), ('blogcard', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.CharBlock())])))])), ('comingsoon', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock())])))])), ('signin', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock())])))]))]),
        ),
    ]
