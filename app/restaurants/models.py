from django.db import models


class VoteMenus(models.Model):
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE)
    menu = models.ImageField()
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Vote Menu"
        verbose_name_plural = 'Menus for vote' 
    def __str__(self):
        return f"Menu_{self.restaurant.name}"


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    current_menu = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
