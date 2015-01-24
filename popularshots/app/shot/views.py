# coding: utf-8
from django.shortcuts import render, redirect, urlresolvers, get_object_or_404


def shots(request):
    return render(request, 'shots.html')

