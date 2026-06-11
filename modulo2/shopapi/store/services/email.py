# store/services/email.py  (agregar al final)

def send_order_confirmation_email(order) -> None:
    """
    Envía correo de confirmación cuando se crea una nueva orden.
    Incluye el detalle de ítems y el total.
    """
    items = [
        {
            'product_name': item.product.name,
            'quantity':     item.quantity,
            'unit_price':   item.unit_price,
            'subtotal':     round(item.quantity * float(item.unit_price), 2),
        }
        for item in order.items.select_related('product').all()
    ]

    _send(
        subject=f'Confirmación de pedido #{order.id} — ShopAPI',
        to=order.user.email,
        txt_template='emails/order_confirmation.txt',
        html_template='emails/order_confirmation.html',
        context={
            'username':   order.user.username,
            'order_id':   order.id,
            'items':      items,
            'total':      order.total,
            'status':     order.status,
            'created_at': order.created_at.strftime('%d/%m/%Y %H:%M'),
        },
    )
# store/services/email.py  (agregar al final)

def send_notification_email(user, subject: str, message: str) -> None:
    """
    Envía un correo de notificación personalizada a un usuario.
    Usada tanto para envíos individuales como masivos.
    """
    _send(
        subject=subject,
        to=user.email,
        txt_template='emails/notification.txt',
        html_template='emails/notification.html',
        context={
            'username': user.username,
            'subject':  subject,
            'message':  message,
        },
    )
# store/services/email.py  (agregar al final)

def send_password_reset_email(user, reset_url: str) -> None:
    """
    Envía correo con el enlace para restablecer la contraseña.
    """
    _send(
        subject='Restablecimiento de contraseña — ShopAPI',
        to=user.email,
        txt_template='emails/password_reset.txt',
        html_template='emails/password_reset.html',
        context={
            'username':  user.username,
            'reset_url': reset_url,
        },
    )