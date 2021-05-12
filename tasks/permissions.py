from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTaskUserOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        print(request.user.id)
        print(obj.user.id)
        return obj.user == request.user