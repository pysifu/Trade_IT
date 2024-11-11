from django.core.exceptions import PermissionDenied


class SpecialGroupRequiredMixin:    
    '''
    Checks if user is staff or superuser to get access to page
    '''
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        
        if not (request.user.is_staff or request.user.is_superuser):
            raise PermissionDenied
        return super(SpecialGroupRequiredMixin, self).dispatch(request, 
                                                               *args, 
                                                               **kwargs)
    
    