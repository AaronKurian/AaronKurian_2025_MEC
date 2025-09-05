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

def draw_triangle_layers():
    """Draw the layered triangular patterns."""
    triangle_patterns = [
        (580, "#DC2F02", 12),
        (560, "#E85D04", 12),
        (540, "#FAA307", 12),
        (520, "#FFBA08", 12),
        (500, "white", 12)
    ]

    for length, color, repeat_count in triangle_patterns:
        draw_repeating_triangle_pattern(length, color, repeat_count)
        main_turtle.right(3)

def draw_middle_section():
    """Draw the middle decorative section with circles and triangles."""
    draw_filled_circle(460, "#38b000")
    draw_filled_circle(445, "#fefae0")

    inner_patterns = [
        (440, "#7D82B8", 36),
        (400, "#613F75", 36),
        (360, "#03071e", 36)
    ]

    for length, color, repeat_count in inner_patterns:
        draw_repeating_triangle_pattern(length, color, repeat_count)

def draw_sectored_layers():
    """Draw the colorful sectored circular layers."""
    draw_filled_circle(330, "white")

    # Color gradients for each layer
    color_palettes = [
        ['#B22222', '#D9412C', '#FF6600', '#FF8C1A', '#FFB733', '#FFE066', '#FFF5CC'],
        ['#D9412C', '#FF6600', '#FF8C1A', '#FFB733', '#FFE066', '#FFF5CC', '#B22222'],
        ['#FF6600', '#FF8C1A', '#FFB733', '#FFE066', '#FFF5CC', '#B22222', '#D9412C'],
        ['#FF8C1A', '#FFB733', '#FFE066', '#FFF5CC', '#B22222', '#D9412C', '#FF6600'],
        ['#FFB733', '#FFE066', '#FFF5CC', '#B22222', '#D9412C', '#FF6600', '#FF8C1A']
    ]

    layer_radii = [290, 260, 230, 200, 170]

    for radius, colors in zip(layer_radii, color_palettes):
        draw_sectored_circle(radius, 28, colors)
