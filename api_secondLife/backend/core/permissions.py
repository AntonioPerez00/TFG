from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso que permite solo al dueño de un objeto editarlo o borrarlo.
    Otros usuarios solo pueden verlo (GET).
    """

    def has_object_permission(self, request, view, obj):
        # Métodos seguros (GET, HEAD, OPTIONS) se permiten siempre
        if request.method in permissions.SAFE_METHODS:
            return True

        # Solo el dueño puede editar o borrar
        return obj.user == request.user
