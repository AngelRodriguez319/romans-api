from app.models import Process, User
from django.shortcuts import get_object_or_404
from domain.operations import decimal_to_roman


def create_process(decimal, user_id):

    user = get_object_or_404(User, pk=user_id)
    number_roman = str(decimal_to_roman(decimal))

    process = Process.objects.create(
        input=decimal, result=number_roman, user=user)
    process.save()

    return number_roman


