from applications.home.models import Home


# proceso para mostrar el correo y numero telefono footer

def home_contacto(request):
    home = Home.objects.latest('created')
    return {
        'phone': home.phone,
        'correo': home.email
    }
