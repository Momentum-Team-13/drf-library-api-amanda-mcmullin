from rest_framework import filters


class IsOwnerFilterBackend(filters.BaseFilterBackend):
    """
    This filter ensures ONLY owners can see their personal objects. 
    """
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)