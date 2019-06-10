# -*- coding: utf-8 -*-
"""
Detect new fixscript files in all apps and run them.
"""
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = ('Detect new fixscript files in all apps and run them.')
