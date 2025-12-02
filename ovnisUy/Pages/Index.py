"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from ovnisUy.Secciones.Footer import footer
from ovnisUy.Compontes.Nav import nav
from ovnisUy.Secciones.Index.Main import main


class State(rx.State):
    """The app state."""


@rx.page("/", title="Ovnis UY")
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.box(class_name="stars absolute inset-0 opacity-50"),
        nav(),
        main(),
        footer(),
        class_name="min-h-screen bg-gradient-to-b from-slate-900 via-blue-950 to-slate-900 text-white relative overflow-hidden",
    )
