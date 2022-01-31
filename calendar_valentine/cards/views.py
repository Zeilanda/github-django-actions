from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from cards.models import Card


def index(request):
    cards = Card.objects.all()
    context = {
        'card_list': cards,
    }
    return render(request, 'cards/index.html', context=context)


class CardsListView(ListView):
    model = Card


class CardDetailView(DetailView):
    model = Card
    context_object_name = 'card'

    def get_object(self, queryset=None):
        return get_object_or_404(Card, slug__iexact=self.kwargs['slug'])


# def cards_list(request):
#     cards = Card.objects.all()
#     context = {
#         'cards': cards,
#     }
#     return render(request, 'cards/card_list.html', context=context)


# def card_details(request, card_id):
#     cards = Card.objects.all()
#     card = get_object_or_404(Card, pk=card_id)
#     context = {
#         'card': card,
#         'cards': cards,
#
#     }
#     return render(request, 'cards/card_detail.html', context=context)
#


