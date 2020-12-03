# Generated by Django 3.1.3 on 2020-12-03 07:59

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0084_auto_20201203_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('carousel', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False))])))])), ('product', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('cost', wagtail.core.blocks.IntegerBlock(required=False))])))])), ('categories', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('photo3', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(required=False))])))])), ('blog', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('date', wagtail.core.blocks.DateBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('instagram', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('indexcarousel', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(required=False)), ('cost', wagtail.core.blocks.IntegerBlock(required=False))])))])), ('listing', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(required=False)), ('cost', wagtail.core.blocks.IntegerBlock(required=False))])))])), ('lookbook', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(required=False)), ('text1', wagtail.core.blocks.CharBlock(required=False))])))])), ('cta', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.RichTextBlock(required=False))])))])), ('partner', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(required=False))])))])), ('blogcard', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('categories', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False))])))])), ('comingsoon', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(required=False))])))])), ('signin', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('productscroll', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('tagname', wagtail.core.blocks.CharBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock(required=False)), ('cost', wagtail.core.blocks.IntegerBlock(required=False)), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('photo3', wagtail.images.blocks.ImageChooserBlock())])))])), ('info', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading1', wagtail.core.blocks.CharBlock(required=False)), ('heading2', wagtail.core.blocks.CharBlock(required=False)), ('heading3', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.CharBlock(required=False)), ('link1', wagtail.core.blocks.CharBlock(required=False)), ('link2', wagtail.core.blocks.CharBlock(required=False)), ('link3', wagtail.core.blocks.CharBlock(required=False)), ('paragraph1', wagtail.core.blocks.CharBlock(required=False)), ('paragraph2', wagtail.core.blocks.CharBlock(required=False))])))])), ('banner', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.RichTextBlock(required=False)), ('paragraph', wagtail.core.blocks.CharBlock(required=False)), ('buttontext', wagtail.core.blocks.CharBlock(required=False))])))])), ('indexcategories', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(required=False))])))])), ('indexminimalcategories', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(required=False))])))])), ('posthero', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock(required=False))])))])), ('interpost', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.core.blocks.CharBlock(required=False)), ('blockquotetext', wagtail.core.blocks.CharBlock(required=False)), ('paragraph1', wagtail.core.blocks.CharBlock(required=False)), ('text1', wagtail.core.blocks.CharBlock(required=False)), ('text2', wagtail.core.blocks.CharBlock(required=False)), ('text3', wagtail.core.blocks.CharBlock(required=False))])))])), ('numbers', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('number', wagtail.core.blocks.IntegerBlock()), ('paragraph', wagtail.core.blocks.CharBlock(required=False))])))])), ('text', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('paragraph', wagtail.core.blocks.CharBlock())])))])), ('herolistingmasonary', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('linkname', wagtail.core.blocks.CharBlock())])))])), ('productlistingmasonary', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(required=False)), ('cost', wagtail.core.blocks.CharBlock(required=False))])))])), ('carouseltransition2', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))])))])), ('indexmoderntitle', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.RichTextBlock())])))])), ('Productindexmodern', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(required=False)), ('cost', wagtail.core.blocks.IntegerBlock(required=False))])))])), ('cta2', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.RichTextBlock(required=False)), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('heading1', wagtail.core.blocks.CharBlock(required=False)), ('cost', wagtail.core.blocks.IntegerBlock(required=False))])))])), ('seperator', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading1', wagtail.core.blocks.CharBlock(required=False)), ('paragraph1', wagtail.core.blocks.CharBlock(required=False)), ('heading2', wagtail.core.blocks.CharBlock(required=False)), ('paragraph2', wagtail.core.blocks.CharBlock(required=False)), ('heading3', wagtail.core.blocks.CharBlock(required=False)), ('paragraph3', wagtail.core.blocks.CharBlock(required=False))])))])), ('lookbook2', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraphtop1', wagtail.core.blocks.CharBlock(required=False)), ('paragraphtop2', wagtail.core.blocks.CharBlock(required=False)), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('photo3', wagtail.images.blocks.ImageChooserBlock()), ('heading1', wagtail.core.blocks.CharBlock(required=False)), ('paragraph1', wagtail.core.blocks.CharBlock(required=False)), ('heading2', wagtail.core.blocks.CharBlock(required=False)), ('paragraph2', wagtail.core.blocks.CharBlock(required=False)), ('heading3', wagtail.core.blocks.CharBlock(required=False)), ('paragraph3', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))])))])), ('cta3', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('photo', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.RichTextBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False))])))])), ('instagram2', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('promoproduct', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('heading', wagtail.core.blocks.CharBlock(required=False)), ('cost', wagtail.core.blocks.IntegerBlock(required=False))])))])), ('productclassic', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo1', wagtail.images.blocks.ImageChooserBlock()), ('photo2', wagtail.images.blocks.ImageChooserBlock()), ('photo3', wagtail.images.blocks.ImageChooserBlock()), ('brandname', wagtail.core.blocks.CharBlock(required=False)), ('title', wagtail.core.blocks.CharBlock(required=False)), ('cost1', wagtail.core.blocks.IntegerBlock(required=False)), ('cost2', wagtail.core.blocks.IntegerBlock(required=False)), ('paragraph', wagtail.core.blocks.CharBlock(required=False))])))])), ('productmodern', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock())])))])), ('blogproducttext', wagtail.core.blocks.StructBlock([('items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('date', wagtail.core.blocks.DateBlock(required=False)), ('heading', wagtail.core.blocks.CharBlock(required=False))])))]))]),
        ),
    ]
