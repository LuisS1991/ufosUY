import reflex as rx

def main()->rx.Component:
    return rx.box(
        rx.text("contenido"),
        class_name="relative z-10"
    )
