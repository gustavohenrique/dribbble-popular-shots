# coding: utf-8
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

import json

from shot.models import Shot


def shots(request):
    return render(request, 'shots.html')

def add_to_favorites(request):
    status = 403
    if request.method == 'POST':
        try:
            form = json.loads(request.body)
            obj, created = Shot.objects.get_or_create(
                id=form.get('id'), title=form.get('title'), description=form.get('description'),
                html_url=form.get('html_url'), image_url=form.get('images').get('normal')
            )
            status = 201 if created else 200
        except:
            status = 400

    return JsonResponse({}, status=status)

def remove_from_favorites(request, id):
    status = 403
    if request.method == 'DELETE':
        try:
            Shot.objects.filter(pk=id).delete()
            status = 200
        except:
            status = 400

    return JsonResponse({}, status=status)


def list_favorites(request):
    status = 403
    data = {}
    if request.method == 'GET':
        try:
            data = serializers.serialize('json', Shot.objects.all())
            status = 200
        except:
            status = 500

    return JsonResponse(data, status=status, safe=False)
