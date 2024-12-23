def serialize_user(user):
    return {
        "id": str(user.get("_id", "")),
        "username": user.get("username"), 
        "email": user.get("email", ""),
    }
