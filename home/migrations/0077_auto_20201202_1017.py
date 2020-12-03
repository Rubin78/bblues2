# Generated by Django 3.1.3 on 2020-12-02 10:17

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0076_auto_20201202_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('carousel', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))])))])), ('product', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('cost', wagtail.core.blocks.IntegerBlock(required=False))])))])), ('categories', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('photo3', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock())])))])), ('blog', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('date', wagtail.core.blocks.DateBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('instagram', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('photo3', wagtail.images.blocks.ImageChooserBlock()), ('photo4', wagtail.images.blocks.ImageChooserBlock()), ('photo5', wagtail.images.blocks.ImageChooserBlock())])))])), ('indexcarousel', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('cost', wagtail.core.blocks.IntegerBlock())])))])), ('listing', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('cost', wagtail.core.blocks.IntegerBlock())])))])), ('lookbook', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock()), ('text1', wagtail.core.blocks.CharBlock())])))])), ('cta', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.RichTextBlock())])))])), ('partner', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock())])))])), ('blogcard', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('categories', wagtail.core.blocks.CharBlock()), ('title', wagtail.core.blocks.CharBlock())])))])), ('comingsoon', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock())])))])), ('signin', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('productscroll', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('info', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading1', wagtail.core.blocks.CharBlock()), ('heading2', wagtail.core.blocks.CharBlock()), ('heading3', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.CharBlock()), ('link1', wagtail.core.blocks.CharBlock()), ('link2', wagtail.core.blocks.CharBlock()), ('link3', wagtail.core.blocks.CharBlock()), ('paragraph1', wagtail.core.blocks.CharBlock()), ('paragraph2', wagtail.core.blocks.CharBlock())])))])), ('banner', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('indexcategories', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock())])))])), ('indexminimalcategories', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock())])))])), ('posthero', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock()), ('heading', wagtail.core.blocks.CharBlock())])))])), ('interpost', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.CharBlock()), ('blockquotetext', wagtail.core.blocks.CharBlock()), ('paragraph1', wagtail.core.blocks.CharBlock()), ('text1', wagtail.core.blocks.CharBlock()), ('text2', wagtail.core.blocks.CharBlock()), ('text3', wagtail.core.blocks.CharBlock())])))])), ('numbers', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('number', wagtail.core.blocks.IntegerBlock()), ('paragraph', wagtail.core.blocks.CharBlock())])))])), ('text', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('paragraph', wagtail.core.blocks.CharBlock())])))])), ('herolistingmasonary', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('linkname', wagtail.core.blocks.CharBlock())])))])), ('productlistingmasonary', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('cost', wagtail.core.blocks.CharBlock())])))])), ('carouseltransition2', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.PageChooserBlock())])))])), ('indexmoderntitle', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock())])))])), ('Productindexmodern', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock()), ('cost', wagtail.core.blocks.IntegerBlock())])))])), ('cta2', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.RichTextBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('heading1', wagtail.core.blocks.CharBlock()), ('cost', wagtail.core.blocks.IntegerBlock())])))])), ('seperator', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading1', wagtail.core.blocks.CharBlock()), ('paragraph1', wagtail.core.blocks.CharBlock()), ('heading2', wagtail.core.blocks.CharBlock()), ('paragraph2', wagtail.core.blocks.CharBlock()), ('heading3', wagtail.core.blocks.CharBlock()), ('paragraph3', wagtail.core.blocks.CharBlock())])))])), ('lookbook2', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('paragraphtop1', wagtail.core.blocks.CharBlock()), ('paragraphtop2', wagtail.core.blocks.CharBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('photo3', wagtail.images.blocks.ImageChooserBlock()), ('heading1', wagtail.core.blocks.CharBlock()), ('paragraph1', wagtail.core.blocks.CharBlock()), ('heading2', wagtail.core.blocks.CharBlock()), ('paragraph2', wagtail.core.blocks.CharBlock()), ('heading3', wagtail.core.blocks.CharBlock()), ('paragraph3', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.PageChooserBlock())])))])), ('cta3', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.PageChooserBlock())])))])), ('instagram2', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock())])))]))]),
        ),
    ]
