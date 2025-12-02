import reflex as rx


def footer() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                # secc1
                rx.box(
                    rx.html(
                        """
                        <svg className="w-5 h-5 text-orange-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                            <ellipse cx="12" cy="10" rx="8" ry="3" />
                            <ellipse cx="12" cy="9" rx="5" ry="2" />
                            <line x1="12" y1="13" x2="12" y2="20" />
                            <circle cx="12" cy="20" r="1" />
                        </svg>
                        """,
                        class_name="w-5 h-5"
                    ),
                    rx.text.span(
                        "© 2025 OVNI Uruguay. Investigación seria de fenómenos inexplicables."
                    ),
                    class_name="flex items-center gap-2",
                ),
                # secc2
                rx.box(
                    rx.link(
                        "Privacidad", class_name="hover:text-orange-400 transition"
                    ),
                    rx.link("Términos", class_name="hover:text-orange-400 transition"),
                    rx.button(
                        "Contacto", class_name="hover:text-orange-400 transition"
                    ),
                    class_name="flex gap-6",
                ),
                class_name="flex flex-col md:flex-row justify-between items-center gap-4 text-sm text-blue-300",
            ),
            class_name="max-w-7xl mx-auto px-6 py-8",
        ),
        class_name="relative z-10 border-t border-white/10 mt-20",
    )
