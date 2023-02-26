from tortoise import models, fields


class User(models.Model):
    """
    User model
    """

    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, null=False)

    created = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"
        ordering = ["id"]


class Position(models.Model):
    """
    User portfolio of cryptocurrency
    """

    id = fields.IntField(pk=True)
    currency = fields.CharField(max_length=20, null=False)
    amount = fields.FloatField()
    user = fields.ForeignKeyField("user.User", related_name="positions", on_delete="CASCADE")

    created_dt = fields.DatetimeField(auto_now_add=True)
    created = fields.DateField(auto_now_add=True)
    updated = fields.DateField(auto_now=True)

    class Meta:
        table = "positions"
        ordering = ["id", "updated"]
