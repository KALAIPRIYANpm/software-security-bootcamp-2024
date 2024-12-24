def validate_client_route(route, allowed_routes, user_permissions):
    """
    Validates a client-side route against a whitelist and detects unauthorized access attempts.

    :param route: str - The requested route
    :param allowed_routes: list - List of allowed routes with wildcard patterns
    :param user_permissions: list - List of user's current permissions
    :return: dict - Result indicating if the route is allowed and the reason if not
    """
    import fnmatch

    route_permissions = {
        "/admin/*": ["admin"],
        "/dashboard/*": ["user"],
        "/profile/*": ["viewer"]
    }
#py
    for pattern in allowed_routes:
        if fnmatch.fnmatch(route, pattern):
            required_permissions = route_permissions.get(pattern, [])
            if all(permission in user_permissions for permission in required_permissions):
                return {
                    "allowed": True
                }
            else:
                return {
                    "allowed": False,
                    "reason": f"Insufficient permissions for {pattern} route",
                    "required_permissions": required_permissions
                }

    return {
        "allowed": False,
        "reason": "Route is not in the allowed list",
        "required_permissions": []
    }

requested_route = input("Enter the requested route (e.g., /admin/users): ")
allowed_routes = input("Enter allowed routes as a comma-separated list (e.g., /dashboard/*,/profile/*,/admin/*): ").split(",")
user_permissions = input("Enter user permissions as a comma-separated list (e.g., user,viewer): ").split(",")

result = validate_client_route(requested_route, allowed_routes, user_permissions)

print("\nValidation Result:")
print(result)
