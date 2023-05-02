from django.db import models

class Category(models.Model):
    rating = models.FloatField(default=0)  # Use FloatField instead of IntegerField
    name = models.CharField(max_length=50, blank=True)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.categorize()

    def categorize(self):
        rating_ranges = [
            (0, 1, 'Low'),
            (1, 2.5, 'Medium'),
            (2.6, 3.5, 'High'),
            (3.6, 5, 'Top'),
        ]
        rating = float(self.rating)
        for start, end, name in rating_ranges:
            if start <= rating <= end:
                if self.name != name:  # check if the name has already been set
                    self.name = name
                    self.save()  # save the category
                break
