def serialize_user(user):
    return {
        "username": str(user.get("_id", "")), 
        "email": user.get("email", ""),
    }
