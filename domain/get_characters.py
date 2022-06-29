from app.models import Process
from django.shortcuts import get_object_or_404
from domain.operations import letters_in_roman


def get_characters(process_id):

    process = get_object_or_404(Process, pk=process_id)
    characters = letters_in_roman(process.result)

    return characters

