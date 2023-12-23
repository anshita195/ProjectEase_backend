from rest_framework import permissions

class isAdminPermission(permissions.BasePermission):
    message="only admin is allowed to do so."
    def has_permission(self, request, view):
        return request.user.role=='a'
        
# class isProjectMember(permissions.BasePermission):
#     message="only project member can do so"
#     def has_permission(self, request, view):
#         return request.user.id in request.project.member.all()

class PermissionPolicyMixin:
    def check_permissions(self, request):
        try:
            # This line is heavily inspired from `APIView.dispatch`.
            # It returns the method associated with an endpoint.
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None

        if (
            handler
            and self.permission_classes_per_method
            and self.permission_classes_per_method.get(handler.__name__)
        ):
            self.permission_classes = self.permission_classes_per_method.get(
                handler.__name__)

        super().check_permissions(request)

