from wagtail.admin import blocks
from wagtail.core.blocks import PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock


# <======== carousel =======>


class CarouselItemBlock(blocks.StructBlock):
    heading=blocks.RichTextBlock()
    link=PageChooserBlock()
    photo=ImageChooserBlock(required=False)

    class Meta:
        template="vendor/blocks/carousel_item.html"
        icon='user'


class CarouselBlock(blocks.StructBlock):
    items=blocks.ListBlock(CarouselItemBlock())

    class Meta:
        template="vendor/blocks/carousel.html"
        icon='user'


# <======== categories =======>

class CategoriesItemBlock(blocks.StructBlock):
    heading=blocks.RichTextBlock()
    link=PageChooserBlock()
    photo1=ImageChooserBlock()
    photo2=ImageChooserBlock()
    photo3=ImageChooserBlock()
    text=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/categories_item.html"
        icon='user'


class CategoriesBlock(blocks.StructBlock):
    items=blocks.ListBlock(CategoriesItemBlock())

    class Meta:
        template="vendor/blocks/categories.html"
        icon='user'


# <======== product =======>

class ProductItemBlock(blocks.StructBlock):
    heading=blocks.CharBlock(required=False)
    link=PageChooserBlock(required=False)
    photo1=ImageChooserBlock()
    photo2=ImageChooserBlock()
    cost=blocks.IntegerBlock(required=False)

    class Meta:
        template="vendor/blocks/product_item.html"
        icon='user'


class ProductBlock(blocks.StructBlock):
    items=blocks.ListBlock(ProductItemBlock())

    class Meta:
        template="vendor/blocks/product.html"
        icon='user'


# <======== blog =======>

class BlogItemBlock(blocks.StructBlock):
    heading=blocks.CharBlock()
    date=blocks.DateBlock()
    link=PageChooserBlock()
    photo=ImageChooserBlock()

    class Meta:
        template="vendor/blocks/blog_item.html"
        icon='user'


class BlogBlock(blocks.StructBlock):
    items=blocks.ListBlock(BlogItemBlock())

    class Meta:
        template="vendor/blocks/blog.html"
        icon='user'


# <======== instagram =======>

class InstagramItemBlock(blocks.StructBlock):
    link=PageChooserBlock()
    photo1=ImageChooserBlock()
    photo2=ImageChooserBlock()
    photo3=ImageChooserBlock()
    photo4=ImageChooserBlock()
    photo5=ImageChooserBlock()

    class Meta:
        template="vendor/blocks/instagram_item.html"
        icon='user'


class InstagramBlock(blocks.StructBlock):
    items=blocks.ListBlock(InstagramItemBlock())

    class Meta:
        template="vendor/blocks/instagram.html"
        icon='user'


# <======== carouselindex page =======>


class IndexcarouselItemBlock(blocks.StructBlock):
    link=PageChooserBlock()
    # photo=ImageChooserBlock()
    photo1=ImageChooserBlock()
    photo2=ImageChooserBlock()
    heading=blocks.CharBlock()
    cost=blocks.IntegerBlock()

    class Meta:
        template="vendor/blocks/indexcarousel_item.html"
        icon='user'


class IndexcarouselBlock(blocks.StructBlock):
    items=blocks.ListBlock(IndexcarouselItemBlock())

    class Meta:
        template="vendor/blocks/indexcarousel.html"
        icon='user'


# <======== lookbook page =======>


class LookbookItemBlock(blocks.StructBlock):
    link=PageChooserBlock()
    photo=ImageChooserBlock()
    photo1=ImageChooserBlock()
    photo2=ImageChooserBlock()
    text=blocks.CharBlock()
    text1=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/lookbook_item.html"
        icon='user'


class LookbookBlock(blocks.StructBlock):
    items=blocks.ListBlock(LookbookItemBlock())

    class Meta:
        template="vendor/blocks/lookbook.html"
        icon='user'


# <======== listing card page =======>


class ListingItemBlock(blocks.StructBlock):
    link=PageChooserBlock()
    photo1=ImageChooserBlock()
    photo2=ImageChooserBlock()
    heading=blocks.CharBlock()
    cost=blocks.IntegerBlock()

    class Meta:
        template="vendor/blocks/listing_item.html"
        icon='user'


class ListingBlock(blocks.StructBlock):
    items=blocks.ListBlock(ListingItemBlock())

    class Meta:
        template="vendor/blocks/listing.html"
        icon='user'


# <======== cta  =======>


class CtaItemBlock(blocks.StructBlock):
    link=PageChooserBlock()
    photo=ImageChooserBlock()
    heading=blocks.RichTextBlock()

    class Meta:
        template="vendor/blocks/cta_item.html"
        icon='user'


class CtaBlock(blocks.StructBlock):
    items=blocks.ListBlock(CtaItemBlock())

    class Meta:
        template="vendor/blocks/cta.html"
        icon='user'


# <======== partner  =======>


class PartnerItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()
    heading=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/partner_item.html"
        icon='user'


class PartnerBlock(blocks.StructBlock):
    items=blocks.ListBlock(PartnerItemBlock())

    class Meta:
        template="vendor/blocks/partner.html"
        icon='user'


# <========index carousel component ====end>

# <========blogcard component ====>


class BlogcardItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()
    categories=blocks.CharBlock()
    title=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/blogcard_item.html"
        icon='user'


class BlogcardBlock(blocks.StructBlock):
    items=blocks.ListBlock(BlogcardItemBlock())

    class Meta:
        template="vendor/blocks/blogcard.html"
        icon='user'


# <========coming soon ====end>


class ComingsoonItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()
    heading=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/comingsoon_item.html"
        icon='user'


class ComingsoonBlock(blocks.StructBlock):
    items=blocks.ListBlock(ComingsoonItemBlock())

    class Meta:
        template="vendor/blocks/comingsoon.html"
        icon='user'


# <========signin ====>


class SigninItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()

    class Meta:
        template="vendor/blocks/signin_item.html"
        icon='user'


class SigninBlock(blocks.StructBlock):
    items=blocks.ListBlock(SigninItemBlock())

    class Meta:
        template="vendor/blocks/signin.html"
        icon='user'


# <========productscroll=====>


class ProductscrollItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()

    # branditem=blocks.CharBlock()
    # brandtitle=blocks.CharBlock()
    # cost=blocks.IntegerBlock()

    class Meta:
        template="vendor/blocks/productscroll_item.html"
        icon='user'


class ProductscrollBlock(blocks.StructBlock):
    items=blocks.ListBlock(ProductscrollItemBlock())

    class Meta:
        template="vendor/blocks/productscroll.html"
        icon='user'


# <========info=====>


class InfoItemBlock(blocks.StructBlock):
    heading1=blocks.CharBlock()
    heading2=blocks.CharBlock()
    heading3=blocks.CharBlock()
    paragraph=blocks.CharBlock()
    link1=blocks.CharBlock()
    link2=blocks.CharBlock()
    link3=blocks.CharBlock()
    paragraph1=blocks.CharBlock()
    paragraph2=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/info_item.html"
        icon='user'


class InfoBlock(blocks.StructBlock):
    items=blocks.ListBlock(InfoItemBlock())

    class Meta:
        template="vendor/blocks/info.html"
        icon='user'


# <========banner====end>


class BannerItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()

    class Meta:
        template="vendor/blocks/banner_item.html"
        icon='user'


class BannerBlock(blocks.StructBlock):
    items=blocks.ListBlock(BannerItemBlock())

    class Meta:
        template="vendor/blocks/banner.html"
        icon='user'


# <========indexcategories====>


class IndexcategoriesItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()
    heading=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/indexcategories_item.html"
        icon='user'


class IndexcategoriesBlock(blocks.StructBlock):
    items=blocks.ListBlock(IndexcategoriesItemBlock())

    class Meta:
        template="vendor/blocks/indexcategories.html"
        icon='user'


# <========indexminmal categories====>


class IndexminimalcategoriesItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()
    heading=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/indexminimalcategories_item.html"
        icon='user'


class IndexminimalcategoriesBlock(blocks.StructBlock):
    items=blocks.ListBlock(IndexminimalcategoriesItemBlock())

    class Meta:
        template="vendor/blocks/indexminimalcategories.html"
        icon='user'


# <========post ====>


class PostheroItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()
    title=blocks.CharBlock()
    heading=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/posthero_item.html"
        icon='user'


class PostheroBlock(blocks.StructBlock):
    items=blocks.ListBlock(PostheroItemBlock())

    class Meta:
        template="vendor/blocks/posthero.html"
        icon='user'


# <========interpost ====>


class InterpostItemBlock(blocks.StructBlock):
    photo1=ImageChooserBlock()
    photo2=ImageChooserBlock()
    paragraph=blocks.CharBlock()
    blockquotetext=blocks.CharBlock()
    paragraph1=blocks.CharBlock()
    text1=blocks.CharBlock()
    text2=blocks.CharBlock()
    text3=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/interpost_item.html"
        icon='user'


class InterpostBlock(blocks.StructBlock):
    items=blocks.ListBlock(InterpostItemBlock())

    class Meta:
        template="vendor/blocks/interpost.html"
        icon='user'


# <========Numbers ====>


class NumbersItemBlock(blocks.StructBlock):
    heading=blocks.CharBlock()
    number=blocks.IntegerBlock()
    paragraph=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/numbers_item.html"
        icon='user'


class NumbersBlock(blocks.StructBlock):
    items=blocks.ListBlock(NumbersItemBlock())

    class Meta:
        template="vendor/blocks/numbers.html"
        icon='user'


# <========Numbers ====>


class TextItemBlock(blocks.StructBlock):
    paragraph=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/text_item.html"
        icon='user'


class TextBlock(blocks.StructBlock):
    items=blocks.ListBlock(TextItemBlock())

    class Meta:
        template="vendor/blocks/text.html"
        icon='user'


# <========listingmansory hero ====>


class HerolistingmasonaryItemBlock(blocks.StructBlock):
    title=blocks.CharBlock()
    link=PageChooserBlock()
    linkname=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/herolistingmasonary_item.html"
        icon='user'


class HerolistingmasonaryBlock(blocks.StructBlock):
    items=blocks.ListBlock(HerolistingmasonaryItemBlock())

    class Meta:
        template="vendor/blocks/herolistingmasonary.html"
        icon='user'


# <========listingmansory product ====>


class ProductlistingmasonaryItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()
    heading=blocks.CharBlock()
    cost=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/productlistingmasonary_item.html"
        icon='user'


class ProductlistingmasonaryBlock(blocks.StructBlock):
    items=blocks.ListBlock(ProductlistingmasonaryItemBlock())

    class Meta:
        template="vendor/blocks/productlistingmasonary.html"
        icon='user'


# <========carousel transition2 ====>


class Carouseltransition2ItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()
    heading=blocks.CharBlock()
    link=PageChooserBlock()

    class Meta:
        template="vendor/blocks/carouseltransition2_item.html"
        icon='user'


class Carouseltransition2Block(blocks.StructBlock):
    items=blocks.ListBlock(Carouseltransition2ItemBlock())

    class Meta:
        template="vendor/blocks/carouseltransition2.html"
        icon='user'


# <========Indexmoderntitle hero ====>


class IndexmoderntitleItemBlock(blocks.StructBlock):
    heading=blocks.RichTextBlock()

    class Meta:
        template="vendor/blocks/indexmoderntitle_item.html"
        icon='user'


class IndexmoderntitleBlock(blocks.StructBlock):
    items=blocks.ListBlock(IndexmoderntitleItemBlock())

    class Meta:
        template="vendor/blocks/indexmoderntitle.html"
        icon='user'


# <========Indexmodern product ====>


class ProductindexmodernItemBlock(blocks.StructBlock):
    photo=ImageChooserBlock()
    heading=blocks.CharBlock()
    cost=blocks.IntegerBlock()

    class Meta:
        template="vendor/blocks/productindexmodern_item.html"
        icon='user'


class ProductindexmodernBlock(blocks.StructBlock):
    items=blocks.ListBlock(ProductindexmodernItemBlock())

    class Meta:
        template="vendor/blocks/productindexmodern.html"
        icon='user'


# <======== cta2  =======>


class Cta2ItemBlock(blocks.StructBlock):
    link=PageChooserBlock()
    photo=ImageChooserBlock()
    heading=blocks.RichTextBlock()
    photo1=ImageChooserBlock()
    heading1=blocks.CharBlock()
    cost=blocks.IntegerBlock()

    class Meta:
        template="vendor/blocks/cta2_item.html"
        icon='user'


class Cta2Block(blocks.StructBlock):
    items=blocks.ListBlock(Cta2ItemBlock())

    class Meta:
        template="vendor/blocks/cta2.html"
        icon='user'


# <======== seperator  =======>


class SeperatorItemBlock(blocks.StructBlock):
    heading1=blocks.CharBlock()
    paragraph1=blocks.CharBlock()
    heading2=blocks.CharBlock()
    paragraph2=blocks.CharBlock()
    heading3=blocks.CharBlock()
    paragraph3=blocks.CharBlock()

    class Meta:
        template="vendor/blocks/seperator_item.html"
        icon='user'


class SeperatorBlock(blocks.StructBlock):
    items=blocks.ListBlock(SeperatorItemBlock())

    class Meta:
        template="vendor/blocks/seperator.html"
        icon='user'


# <======== Lookbook2  =======>


class Lookbook2ItemBlock(blocks.StructBlock):
    heading=blocks.CharBlock()
    paragraphtop1=blocks.CharBlock()
    paragraphtop2=blocks.CharBlock()
    photo1=ImageChooserBlock()
    photo2=ImageChooserBlock()
    photo3=ImageChooserBlock()
    heading1=blocks.CharBlock()
    paragraph1=blocks.CharBlock()
    heading2=blocks.CharBlock()
    paragraph2=blocks.CharBlock()
    heading3=blocks.CharBlock()
    paragraph3=blocks.CharBlock()
    link=PageChooserBlock()

    class Meta:
        template="vendor/blocks/lookbook2_item.html"
        icon='user'


class Lookbook2Block(blocks.StructBlock):
    items=blocks.ListBlock(Lookbook2ItemBlock())

    class Meta:
        template="vendor/blocks/lookbook2.html"
        icon='user'
