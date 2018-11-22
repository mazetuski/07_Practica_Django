from django.contrib import admin

from blog.models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    filter_horizontal = ('category', )
    list_display = ['title', 'description_short', 'url_assert', 'get_categories', 'owner_fullname']
    list_filter = ['category', 'owner']
    search_fields = ['title', 'category__name', 'description_long', 'owner__first_name']
    fieldsets = [
        [None, {
            'fields': ['title', 'description_short', 'description_long', 'url_assert', 'category', 'owner', 'pub_date']
        }]
    ]

    def get_categories(self, obj):
        return "\n".join([c.name for c in obj.category.all()])

    # Put owner object fullname and allow order by it
    def owner_fullname(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']