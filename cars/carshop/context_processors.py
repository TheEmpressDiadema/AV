from .utils import menu

def get_cars_context(request):
    return {'menu' : menu }