"""
MAIN POOKALAM DRAWING FUNCTIONS
===============================
Orchestrates all the components to create the complete pookalam design.

Created by: Aaron Kurian Abraham
"""

import turtle
from shapes import (
    draw_filled_circle, draw_sectored_circle, draw_small_circles_ring,
    draw_repeating_triangle_pattern
)
from tux import draw_tux
from diya import draw_diyas_around_pookalam
from border import draw_circular_border

# Global turtle instance 
main_turtle = turtle.Turtle()
main_turtle.hideturtle()
main_turtle.speed(0)

# =============================================================================
# MAIN POOKALAM LAYERS
# =============================================================================

def draw_outer_rings():
    """Draw the outermost decorative rings of the pookalam."""
    draw_filled_circle(600, "#370617")

    draw_small_circles_ring(
        center=(0, 0), big_radius=580, small_radius=14, count=48,
        color="#4cc9f0", start_angle=11, inner_rings=3,
        inner_colors=["#4361ee", "#3a0ca3", "#6b0f9c", "#f72585"]
    )

    draw_small_circles_ring(
        center=(0, 0), big_radius=590, small_radius=120, count=12,
        color="#6a040f", start_angle=15, inner_rings=3,
        inner_colors=["#9d0208", "#d00000", "#6a040f"]
    )

