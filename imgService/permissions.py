from rest_framework import permissions


class IsBetaPlayerPermission(permissions.BasePermission):
    """
    Custom permission to only allow users with 
    is_beta_player == True to upload images.
    """

    def has_permission(self, request, view):
        print("------------------------: USER :-------------------")
        print(request.user)
        # Check if the user making the request has is_beta_player set to True
        return request.user.is_authenticated and request.user.is_beta_player
