from django.db import models

class Copy(models.Model):
    class Meta:
        ordering = ['id']
    
    amount = models.IntegerField()
    copy_booked = models.IntegerField(default=0)
    books = models.OneToOneField("livros.Book", on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)


class Borrow (models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="borrows")
    copy = models.ForeignKey("copias.Copy", on_delete=models.CASCADE, related_name="borrows")
    borrowing_start_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    is_returned = models.BooleanField(default=False)

