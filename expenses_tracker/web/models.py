from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker.web.validators import validate_only_letters, MaxFileSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 15
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN =2
    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE =0
    UPLOAD_TO_DIR = 'profiles/'
    IMAGE_MAX_FILE_SIZE =5


    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )
    last_name=models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )
    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        )

    )
    image = models.ImageField(
        upload_to=UPLOAD_TO_DIR,
        blank=True,
        null=True,
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_FILE_SIZE),

        )
    )


class Expense(models.Model):
    TITLE_MAX_LEN = 30
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )
    image = models.URLField(
        blank=True,
        null=True,
        verbose_name='Link to Image',
    )
    description = models.TextField(
        blank=True,
        null=True,
    )

    price = models.FloatField()
