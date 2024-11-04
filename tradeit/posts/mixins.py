from django.core.exceptions import PermissionDenied

#does class name is still valid 
class GroupRequiredMixin:
    group_required = None
    
    def dispatch(self, request, *args, **kwargs):
        if not self.group_required:
            raise AttributeError('GroupRequiredMixin requires "group_required" attribute to set.')
        
        if not request.user.is_authenticated:
            raise PermissionDenied
        
        if not request.user.is_staff or not request.user.is_superuser:
            raise PermissionDenied
        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)