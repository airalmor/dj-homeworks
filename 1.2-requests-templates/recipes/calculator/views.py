from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def show_recipt(request, dish):
    ask_recipt = DATA.get(dish, {})
    person_quantity = int(request.GET.get('servings', 1))
    context = {
        'recipe': {},
    }
    for food, quantity in ask_recipt.items():
        context['recipe'][food] = round(quantity * person_quantity, 2)

    return render(request, 'calculator/index.html', context)
