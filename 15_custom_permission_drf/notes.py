# To implement a custom permission, override BasePermission and implement either, or both, of the following methods:
# has_permission(self, request, view)
# has_object_permission(self, request, view, obj)
# The methods should return True if the request should be granted access, and False otherwise.


# Custom permissions:
# custompermissions.py

# class MyPermission(BasePermission):
# 	def has_permission(self, request, view)

# third party apps for permmissions:
# Third party packages:-
# DRF - Access Policy
# Composed Permissions
# REST Condition
# DRY Rest Permissions
# Django Rest Framework Roles
# Django REST Framework API Key
# Django Rest Framework Role Filters
# Django Rest Framework PSQ
