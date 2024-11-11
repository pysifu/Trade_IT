from random import randint
def check_slug_unique(model_class, slug):
    '''
    Checks if slug is unique otherwise function continues 
    adding random number untill is valid. 
    '''
    is_not_unique = model_class.objects.filter(slug=slug).exists()
    if is_not_unique:
        slice_length = 0
        slug += '-'
        while is_not_unique:
            slice_length -= 1
            slug += f'{str(randint(0, 9))}'
            is_not_unique = model_class.objects.filter(slug=slug)
    return slug
        
    