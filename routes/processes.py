"""
__Seed builder__
  Extended module
"""

from crypt import methods
import seed.routes.processes as SeedRoute
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.shortcuts import get_object_or_404
from seed.util.request_util import has_fields_or_400
from domain.create_process import create_process
from domain.get_characters import get_characters


class ProcessViewSet(SeedRoute.ProcessViewSet):

    @action(detail=False, methods=['POST'])
    def decimal_to_roman(self, request):

        data = request.data
        has_fields_or_400(data, "user_id", "input")

        try:
            user_id = int(data["user_id"])
            decimal = int(data["input"])
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"detail": "Value error."})

        number_roman = create_process(decimal, user_id)
        return Response(status=status.HTTP_201_CREATED, data=number_roman)


    @action(detail=True, methods=['GET'])
    def characters(self, request, pk=None):

        response = get_characters(pk)
        return Response(status=status.HTTP_200_OK, data=response)