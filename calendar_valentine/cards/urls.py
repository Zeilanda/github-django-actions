

from django.urls import path, re_path
import cards.views as cards


urlpatterns = [
    path('', cards.index, name='index'),
    # path('cards/', cards.cards_list),
    path('cards/',
         cards.CardsListView.as_view(),
         name='cards_list'),
    path('cards/<slug:slug>/',
         cards.CardDetailView.as_view(template_name='cards/card_detail.html'),
         name='card_detail'),
]
