from goods.models import Products
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline


def query_search(query: str):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    vector = SearchVector('name', 'description')
    search_query = SearchQuery(query)
    result = Products.objects.annotate(
        rank=SearchRank(
            vector,
            search_query
        )).filter(rank__gt=0).order_by('-rank')
    result = result.annotate(headline=SearchHeadline(
        'name',
        search_query,
        start_sel='<span style="background-color: green;">',
        stop_sel='</span>',
    ))
    result = result.annotate(bodyline=SearchHeadline(
        'description',
        search_query,
        start_sel='<span style="background-color: green;">',
        stop_sel='</span>',
    ))
    return result
