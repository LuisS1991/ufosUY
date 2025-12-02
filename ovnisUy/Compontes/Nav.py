import reflex as rx


def nav() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    rx.html(
                        """
                        <svg className="w-8 h-8 text-orange-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <ellipse cx="12" cy="10" rx="8" ry="3" />
                            <ellipse cx="12" cy="9" rx="5" ry="2" />
                            <line x1="12" y1="13" x2="12" y2="20" />
                            <circle cx="12" cy="20" r="1" />
                        </svg>
                        """,
                        class_name="w-8 h-8"
                    ),
                    rx.text.span("OVNI Uruguay", class_name="text-xl font-bold"),
                    class_name="flex items-center gap-2",
                ),
                rx.box(
                    rx.link("Inicio", class_name="hover:text-orange-400 transition"),
                    rx.link(
                        "Avistamientos", class_name="hover:text-orange-400 transition"
                    ),
                    rx.link(
                        "Investigaciones", class_name="hover:text-orange-400 transition"
                    ),
                    rx.link("Archivo", class_name="hover:text-orange-400 transition"),
                    rx.link("Noticias", class_name="hover:text-orange-400 transition"),
                    rx.link("Contacto", class_name="hover:text-orange-400 transition"),
                    class_name="hidden md:flex items-center gap-8 text-sm",
                ),
                class_name="flex items-center justify-between",
            ),
            class_name="max-w-7xl mx-auto px-6 py-4",
        ),
        class_name="relative z-10 border-b border-white/10 backdrop-blur-sm",
    )
