import re
from django.shortcuts import render
from core.models import PersonData
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    """ Custom view for the homepage
        to show up the table
    """
    person_data = PersonData.objects.all().order_by('order_value')

    context={
        'person_data' : person_data ,
    }
    return render(request,'home.html',context)


@api_view(['GET','POST'])
def order_database(request):
    """Post view for updating the database order
    """

    if request.method == 'POST':
        req_body = request.data
        first_object_id = req_body.get("first_object_id")
        second_object_id = req_body.get("second_object_id")

        regex = r"\w{8}-\w{4}-\w{4}-\w{4}-\w{12}"
        matches = re.search(regex, first_object_id)
        first_object_id = matches[0]

        matches = re.search(regex, second_object_id)
        second_object_id = matches[0]

        first_object = get_object_or_404(PersonData, id=first_object_id)
        second_object = get_object_or_404(PersonData, id=second_object_id)

        temp_variable = first_object.order_value
        first_object.order_value = second_object.order_value
        second_object.order_value = temp_variable

        first_object.save()
        second_object.save()

        response_dict = {
            'success' : True
        }

        return Response(response_dict, status=status.HTTP_200_OK)

    else:
        response_dict = {
            'success' : True,
            'req_type' : 'GET'
        }
        return Response(response_dict, status=status.HTTP_200_OK)