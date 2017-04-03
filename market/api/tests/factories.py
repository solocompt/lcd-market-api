from django.contrib.auth import get_user_model

from factory.django import DjangoModelFactory as Factory
from factory import LazyAttribute, Sequence, SubFactory

from market.api import models


model = get_user_model()

# Create your factories here.
