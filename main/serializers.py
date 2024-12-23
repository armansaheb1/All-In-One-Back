from rest_framework import serializers
from . import models
from Analyzer import settings


class ServiceSerializer(serializers.ModelSerializer):
    static_variables = serializers.PrimaryKeyRelatedField(
        many=True, queryset=models.StaticEntry.objects.all()
    )

    class Meta:
        depth = 2
        model = models.Service
        fields = (
            "id",
            "slug",
            "name",
            "prompt",
            "description",
            "variables",
            "static_variables",
            "price",
            "icon",
            "icon_image",
            "button_name",
            "highlight",
            "color",
            "category",
            "get_image",
        )


class UserServiceSerializer(serializers.ModelSerializer):

    class Meta:
        depth = 2
        model = models.Service
        fields = (
            "id",
            "slug",
            "name",
            "prompt",
            "description",
            "variables",
            "static_variables",
            "price",
            "icon",
            "icon_image",
            "button_name",
            "highlight",
            "color",
            "category",
            "get_image",
        )


class NewsServiceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.NewsService
        fields = "__all__"


class ImageServiceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.ImageService
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.File
        fields = ("file", "get_image")


class IdeaStaticEntrySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.IdeaStaticEntry
        fields = "__all__"


class StaticEntrySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.StaticEntry
        fields = "__all__"


class NewsIntrestSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.NewsIntrest
        fields = "__all__"


class SocialIntrestSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.SocialIntrest
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        for item in representation["services"]:
            if not item["icon_image"]:
                item["get_image"] = ""
            else:
                item["get_image"] = settings.My_MEDIA_ROOT + item["icon_image"]
        representation["package_id"] = "custom value"
        return representation

    class Meta:
        depth = 2
        model = models.Category
        fields = ("id", "name", "services", "template", "description", "icon")


class NewsReportSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.NewsReport
        fields = "__all__"


class ToneSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Tone
        fields = "__all__"


class FormatSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = models.Format
        fields = "__all__"
