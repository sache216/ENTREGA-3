from django.urls import path

from control_estudios.views import (
    listar_estudiantes, listar_cursos, crear_curso, buscar_cursos,
    buscar_estudiantes, buscar_profesores,
    eliminar_curso, editar_curso, EstudianteListView, EstudianteCreateView,
    EstudianteDetailView, EstudianteUpdateView, EstudianteDeleteView,ProfesorCreateView,
    ProfesorListView, ProfesorCreateView,
    ProfesorDetailView, ProfesorUpdateView, ProfesorDeleteView,
)

# Son las URLS de la app control_estudios
urlpatterns = [
    # URLS de cursos (funciones)
    path("cursos/", listar_cursos, name="lista_cursos"),
    path("crear-curso/", crear_curso, name="crear_curso"),
    path("buscar-cursos/", buscar_cursos, name="buscar_cursos"),
    path("editar-curso/<int:id>/", editar_curso, name="editar_curso"),
    path("eliminar-curso/<int:id>/", eliminar_curso, name="eliminar_curso"),
    # URLS de estudiantes (clases)
    path("estudiantes/", EstudianteListView.as_view(), name="lista_estudiantes"),
    path("estudiantes/<int:pk>/", EstudianteDetailView.as_view(), name="ver_estudiante"),
    path("crear-estudiante/", EstudianteCreateView.as_view(), name="crear_estudiante"),
    path("editar-estudiante/<int:pk>/", EstudianteUpdateView.as_view(), name="editar_estudiante"),
    path("eliminar-estudiante/<int:pk>/", EstudianteDeleteView.as_view(), name="eliminar_estudiante"),
    path("buscar-estudiantes/", buscar_estudiantes, name="buscar_estudiantes"),
    
    path("profesores/", ProfesorListView.as_view(), name="lista_profesores"),
    path("profesores/<int:pk>/", ProfesorDetailView.as_view(), name="ver_profesor"),
    path("crear-profesor/", ProfesorCreateView.as_view(), name="crear_profesor"),
    path("editar-profesor/<int:pk>/", ProfesorUpdateView.as_view(), name="editar_profesor"),
    path("eliminar-profesor/<int:pk>/", ProfesorDeleteView.as_view(), name="eliminar_profesor"),
    path("buscar-profesores/", buscar_profesores, name="buscar_profesor"),
    
    
]