from django.db import models
from usersmanagement.models import Clients, Trader 
# Create your models here.
class AssetsManagementClients(models.Model):
    trader = models.ForeignKey(Trader, on_delete= models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    amount_changed = models.DecimalField(decimal_places=3, max_digits=10)
    actual_amount = models.DecimalField(decimal_places=3,max_digits=10)
    date_added = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "AssetsClientsManagement"
        ordering = ['-date_added']
        verbose_name = "Log del cliente "
        verbose_name_plural = "Logs de los clientes"

    def __str__(self):
        return  str(self.date_added) + " | " + str(self.client.user.first_name)+ " | "

 