"""
TUX DRAWING FUNCTIONS
====================
Functions for drawing the Linux mascot Tux penguin.

Created by: Aaron Kurian Abraham
"""

import turtle
import math
from advanced_shapes import draw_rounded_triangle_sides

# =============================================================================
# BASIC TUX SHAPE FUNCTIONS
# =============================================================================

def draw_filled_shape(points, color):
    """Draw a filled polygon from a list of points."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color(color, color)
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.begin_fill()
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])
    t.end_fill()

def generate_ellipse_points(cx, cy, rx, ry, angle_deg=0, step_deg=3):
    """Generate points for an ellipse."""
    points = []
    theta = math.radians(angle_deg)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    for degree in range(0, 361, step_deg):
        rad = math.radians(degree)
        x = rx * math.cos(rad)
        y = ry * math.sin(rad)
        rotated_x = x * cos_theta - y * sin_theta
        rotated_y = x * sin_theta + y * cos_theta
        points.append((cx + rotated_x, cy + rotated_y))

    return points

def draw_ellipse(cx, cy, rx, ry, color, angle_deg=0, step_deg=2):
    """Draw a filled ellipse."""
    draw_filled_shape(generate_ellipse_points(cx, cy, rx, ry, angle_deg, step_deg), color)

def draw_arc(x, y, width, height, color, angle=0, step=2, thickness=1, start_deg=-90, end_deg=90):
    """Draw an elliptical arc."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor(color)
    t.pensize(thickness)

    theta = math.radians(angle)
    cos_theta = math.cos(theta)
    sin_theta = math.sin(theta)

    # Calculate starting point
    rad_start = math.radians(start_deg)
    x_start = width * math.cos(rad_start)
    y_start = height * math.sin(rad_start)
    rotated_x_start = x_start * cos_theta - y_start * sin_theta
    rotated_y_start = x_start * sin_theta + y_start * cos_theta

    t.penup()
    t.goto(x + rotated_x_start, y + rotated_y_start)
    t.pendown()

    degree = start_deg
    while degree <= end_deg:
        rad = math.radians(degree)
        x_point = width * math.cos(rad)
        y_point = height * math.sin(rad)
        rotated_x = x_point * cos_theta - y_point * sin_theta
        rotated_y = x_point * sin_theta + y_point * cos_theta
        t.goto(x + rotated_x, y + rotated_y)
        degree += max(1, step)

# =============================================================================
# MAIN TUX DRAWING FUNCTION
# =============================================================================

def draw_tux(scale=0.4, offset_y=0):
    """Draw the Linux mascot Tux with all features."""

    def draw_ellipse_scaled(cx, cy, rx, ry, color, angle=0):
        """Helper to draw scaled ellipse."""
        draw_ellipse(cx * scale, (cy + offset_y) * scale, rx * scale, ry * scale, color, angle_deg=angle)

    def draw_arc_scaled(cx, cy, rx, ry, color, angle=0, step=2, thickness=1, start=-90, end=90):
        """Helper to draw scaled arc."""
        draw_arc(cx * scale, (cy + offset_y) * scale, rx * scale, ry * scale, color, angle=angle,
                step=step, thickness=thickness, start_deg=start, end_deg=end)

    # Main body parts
    draw_ellipse_scaled(0, 40, 150, 200, "#000000")
    draw_ellipse_scaled(0, 0, 170, 170, "#000000")
    draw_ellipse_scaled(0, 220, 90, 110, "#000000")
    draw_ellipse_scaled(-5, 20, 100, 180, "#FFFFFF")  # Belly
    draw_ellipse_scaled(-5, 150, 60, 60, "#FFFFFF")   # Head
    draw_ellipse_scaled(-5, 185, 20, 12, "#FFFFFF")   # Face patch

    # Flippers
    draw_ellipse_scaled(-90, -50, 40, 100, "#000000", angle=35)
    draw_ellipse_scaled(90, -50, 40, 100, "#000000", angle=-35)
    draw_ellipse_scaled(120, -15, 20, 30, "#000000", angle=-35)

    # Feet
    foot_color = "#F4B400"

    # Left feet
    draw_ellipse_scaled(-95, -80, 80, 30, "#000000", angle=-50)
    draw_ellipse_scaled(-105, -90, 80, 30, "#000000", angle=-30)
    draw_ellipse_scaled(-115, -110, 80, 30, "#000000", angle=-10)
    draw_ellipse_scaled(-90, -80, 75, 25, foot_color, angle=-50)
    draw_ellipse_scaled(-100, -90, 75, 25, foot_color, angle=-30)
    draw_ellipse_scaled(-110, -110, 75, 25, foot_color, angle=-10)

    # Right feet
    draw_ellipse_scaled(85, -70, 80, 30, "#000000", angle=70)
    draw_ellipse_scaled(95, -80, 80, 30, "#000000", angle=50)
    draw_ellipse_scaled(105, -100, 80, 30, "#000000", angle=30)
    draw_ellipse_scaled(75, -80, 75, 25, foot_color, angle=70)
    draw_ellipse_scaled(90, -90, 75, 25, foot_color, angle=50)
    draw_ellipse_scaled(100, -110, 75, 25, foot_color, angle=30)

    draw_ellipse_scaled(120, -15, 20, 30, "#000000", angle=-35)

    # Eyes
    draw_ellipse_scaled(-50, 220, 18, 24, "#FFFFFF")
    draw_ellipse_scaled(10, 220, 18, 24, "#FFFFFF")
    draw_ellipse_scaled(-52, 215, 10, 14, "#000000")
    draw_ellipse_scaled(7, 215, 10, 14, "#000000")

    # Mouth using rounded triangles
    draw_rounded_triangle_sides(
        center=(-75 * scale, (180 + offset_y) * scale),
        sides=(4, 6, 8), radius=10 * scale, rotation_deg=-45,
        edge_color="#FFA000", fill_color="#FFA000",
        thickness=max(1, int(6 * scale)), step_deg=4, scale=6.0
    )
    draw_rounded_triangle_sides(
        center=(30 * scale, (170 + offset_y) * scale),
        sides=(4, 6, 8), radius=10 * scale, rotation_deg=135,
        edge_color="#FFA000", fill_color="#FFA000",
        thickness=max(1, int(6 * scale)), step_deg=4, scale=6.0
    )

    # Decorative arcs
    draw_arc_scaled(-25, 175, 35, 20, "#000000", angle=180, step=1, thickness=1, start=10, end=170)
    draw_arc_scaled(-30, 200, 1, 1, "#000000", step=1, thickness=4, start=10, end=170)
    draw_arc_scaled(-10, 200, 1, 1, "#000000", step=1, thickness=4, start=10, end=170)
    draw_arc_scaled(110, 60, 50, 20, "#3B3B3B", angle=270, step=1, thickness=2, start=10, end=190)
    draw_arc_scaled(125, 0, 20, 5, "#3B3B3B", angle=0, step=1, thickness=2, start=0, end=190)
    draw_arc_scaled(-100, 80, 50, 20, "#3B3B3B", angle=75, step=1, thickness=2, start=10, end=170)