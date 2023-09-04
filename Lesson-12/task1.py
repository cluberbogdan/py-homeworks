def is_admin(func):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type')
        if user_type == 'admin':
            return func(*args, **kwargs)
        else:
            raise ValueError('Permission denied')
    return wrapper

@is_admin
def show_customer_receipt(user_type: str):
    # Some very dangerous operation
    return 'function pass as it should be'


try:
    result = show_customer_receipt(user_type='user')
    print(result)
except ValueError as e:
    print(e)

result = show_customer_receipt(user_type='admin')
print(result)