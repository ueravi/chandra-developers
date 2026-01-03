from streamlit_option_menu import option_menu

def render_navbar():
    selected = option_menu(
        menu_title=None,
        options=[
            "Home",
            "About Us",
            "Joint Development",
            "Projects",
            "Buy a Site",
            "Why Choose Us",
            "Testimonials",
            "FAQ",
            "Contact"
        ],
        icons=[
            "house",
            "info-circle",
            "diagram-3",
            "buildings",
            "geo-alt",
            "check-circle",
            "chat-quote",        # Testimonials
            "question-circle",   # FAQ
            "envelope"
        ],
        orientation="horizontal",
        styles={
            "container": {"padding": "10px", "background-color": "#FFFFFF"},
            "icon": {"color": "#0F2A1D", "font-size": "16px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "center",
                "color": "#1E1E1E",
                "--hover-color": "#F4F4F4",
            },
            "nav-link-selected": {
                "background-color": "#0F2A1D",
                "color": "white",
            },
        }
    )
    return selected
