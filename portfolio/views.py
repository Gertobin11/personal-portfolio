from django.shortcuts import render, get_object_or_404
from .models import Portfolio


def portfolio_page(request):
    """ View to render the portfolio page """
    projects = Portfolio.objects.all()
    template = "portfolio/portfolio_page.html"
    context = {
        'projects': projects
    }

    return render(request, template, context)


def portfolio_details(request, pk):
    """  A view to return the selected project Portfolio """
    project = get_object_or_404(Portfolio, pk=pk)
    context = {
        'project': project
    }
    template = 'portfolio/portfolio_details.html'
    return render(request, template, context)
