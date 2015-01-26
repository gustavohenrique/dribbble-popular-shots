# coding: utf-8
from django.shortcuts import render, redirect, urlresolvers, get_object_or_404
from django.http import JsonResponse
from django.core import serializers

import json

from shot.models import Shot


def shots(request):
    return render(request, 'shots.html')

def add_to_favorites(request):
    status = 403

    if request.method == 'POST':
        status = 200
        try:
            form = json.loads(request.body)
            obj, created = Shot.objects.get_or_create(
                id=form.get('id'), title=form.get('title'), description=form.get('description'),
                html_url=form.get('html_url'), image_url=form.get('images').get('normal')
            )
            if created:
                status = 201
        except:
            status = 400

    return JsonResponse({}, status=status)

def list_favorites(request):
    status = 403
    data = {}

    if request.method == 'GET':
        status = 200
        data = serializers.serialize('json', Shot.objects.all())

    return JsonResponse(data, status=status, safe=False)
