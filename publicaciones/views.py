from django.views.generic import TemplateView, ListView, DetailView
from .models import Publicacion

# ---------------------------------------------------------------------------
# InicioView
# ---------------------------------------------------------------------------

class InicioView(TemplateView):
    template_name = "publicaciones/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context ["titulo"] = "Portal de Noticias de Tiago"
        context ["mensaje"] = "Bienvenido/a al sitio, glup"
        return context

# ---------------------------------------------------------------------------
# PublicacionListView
# ---------------------------------------------------------------------------

class PublicacionListView(ListView):
    model = Publicacion
    template_name = "publicaciones/publicacion_list.html"
    context_object_name = "publicacion_list"

# ---------------------------------------------------------------------------
# PublicacionDetailView
# ---------------------------------------------------------------------------

class PublicacionDetailView(DetailView):
    model = Publicacion
    context_object_name = "publicacion"
    pk_url_kwarg = "publicacion_id"