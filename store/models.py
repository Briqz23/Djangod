from django.db import models

#id criado autometicamente

#produto pode ter promoções e promoçõesp odem ser aplicadas a produtos
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    
class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete= models.SET_NULL, null=True,related_name='+')

class Product(models.Model):
     
    title = models.CharField(max_length=255) #varchar 255
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2) #xxxx,xx
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)




class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [(MEMBERSHIP_BRONZE, 'Bronze'),
                           (MEMBERSHIP_SILVER, 'Silver'), 
                           (MEMBERSHIP_GOLD, 'Gold')
                          ] 
    
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
class Order(models.Model):
    placed_at = models.DateField(auto_now_add=True)

    PAYMENT_COMPLETED = 'C'
    PAYMENT_PENDING = 'P'
    PAYMENT_FAILED = 'F'
    PAYMENT_OPTIONS = [(PAYMENT_PENDING, 'P'),(PAYMENT_COMPLETED, 'Completed'),  (PAYMENT_FAILED, 'F')]
    payment = models.CharField(max_length=1, choices=PAYMENT_OPTIONS, default=None)
    customer= models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT) # se um order tiver pelo meons 1 item, ele n pode ser deletado
    product = models.ForeignKey(Product, on_delete = models.PROTECT) #se deletar produto, n deleta os orderItems
    quantity = models.PositiveSmallIntegerField
    unit_price = models.DecimalField(max_digits=6, decimal_places=2) #guardar valor do produto na hora que foi comprado, pra evitar problemas, não referenciar o PRICE de PRODUCT

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE) #se deletar carrinho deleta todos os produtos no carrinho
    product = models.ForeignKey(Product, on_delete=models.CASCADE)#se produto é deletado, ele sai de todos os carrinhos tbm
    qunatity = models.PositiveSmallIntegerField
#Adress fihlo de Customer
class Adress(models.Model):
    #relacao 1 : 1 endereço e usuário
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    #já que não existe endereço sem cliente, ao deletar cleinte endereço é deletado automaticamente
    

