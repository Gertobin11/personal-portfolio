from django.shortcuts import render
from .models import Portfolio


def portfolio_page(request):
    """ View to render the portfolio page """
    projects = Portfolio.objects.all()
    template = "portfolio/portfolio_page.html"
    context = {
        'projects': projects
    }

    return render(request, template, context)
