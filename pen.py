from manimlib import *
import numpy as np

class ConservationOfEnergy(Scene):
    def construct(self):
        # 1. Title
        title = Tex(
            r"\mathbb{C}\text{onservation of }", 
            r"\mathbb{E}\text{nergy}",
            font_size=42
        )
        title[1].set_color("#E77471")
        title.to_edge(UP, buff=0.8)
        self.add(title)

        # 2. Pendulum parameters & setup
        pivot_point = UP * 3.8
        rod_length = 2.4
        theta_max = 35 * DEGREES
        omega = 2.5

        # Fixed Pivot
        pivot_bar = Line(pivot_point + LEFT * 0.4, pivot_point + RIGHT * 0.4, color=WHITE, stroke_width=4)
        self.add(pivot_bar)

        # Baseline (h = 0)
        h_base_y = pivot_point[1] - rod_length
        baseline = DashedLine(
            [-3.2, h_base_y, 0], 
            [3.2, h_base_y, 0], 
            dash_length=0.15, 
            color=GREY_D
        )
        self.add(baseline)

        time_tracker = ValueTracker(0)

        def get_theta():
            return theta_max * np.sin(omega * time_tracker.get_value())

        def get_bob_pos():
            th = get_theta()
            return pivot_point + np.array([rod_length * np.sin(th), -rod_length * np.cos(th), 0])

        # Dynamic Rod & Bob
        rod = always_redraw(lambda: Line(pivot_point, get_bob_pos(), color=WHITE, stroke_width=3))
        bob = always_redraw(lambda: Circle(radius=0.25, color=WHITE, fill_color="#F5F5DC", fill_opacity=1).move_to(get_bob_pos()))

        # Height line (purple)
        h_line = always_redraw(lambda: Line(
            [get_bob_pos()[0], h_base_y, 0],
            get_bob_pos(),
            color="#7B68EE",
            stroke_width=4
        ))
        h_label = always_redraw(lambda: Tex(r"h", color="#7B68EE", font_size=32).next_to(h_line, RIGHT, buff=0.08))

        # Gravity arrow (mg)
        mg_arrow = always_redraw(lambda: Arrow(get_bob_pos(), get_bob_pos() + DOWN * 0.75, color=WHITE, buff=0, stroke_width=3))
        mg_label = always_redraw(lambda: Tex(r"mg", font_size=28).next_to(mg_arrow, DOWN, buff=0.08))

        # Tension arrow (T)
        tension_arrow = always_redraw(lambda: Arrow(
            get_bob_pos(),
            get_bob_pos() + (pivot_point - get_bob_pos()) / rod_length * 0.95,
            color=WHITE, buff=0, stroke_width=3
        ))
        t_label = always_redraw(lambda: Tex(r"T", font_size=28).next_to(tension_arrow.get_end(), LEFT, buff=0.08))

        # Velocity arrow (v)
        def get_v_arrow():
            th = get_theta()
            v_val = theta_max * omega * np.cos(omega * time_tracker.get_value())
            tangent = np.array([np.cos(th), np.sin(th), 0])
            scaled_v = tangent * v_val * 0.55
            if np.linalg.norm(scaled_v) < 0.05:
                return VMobject()
            return Arrow(get_bob_pos(), get_bob_pos() + scaled_v, color="#F5DEB3", stroke_width=3, buff=0)

        v_arrow = always_redraw(get_v_arrow)
        v_label = always_redraw(
            lambda: Tex(r"v", color="#F5DEB3", font_size=28).next_to(v_arrow.get_end(), UP + LEFT, buff=0.05)
            if isinstance(v_arrow, Arrow) else VMobject()
        )

        self.add(rod, bob, h_line, h_label, mg_arrow, mg_label, tension_arrow, t_label, v_arrow, v_label)

        # 3. Bar Chart
        chart_base_y = -1.2
        bar_width = 0.9
        max_bar_height = 2.2

        bar_axis = Line([-3.2, chart_base_y, 0], [3.2, chart_base_y, 0], color=GREY_D, stroke_width=2)
        self.add(bar_axis)

        # Labels
        pe_label = Tex(r"mgh", color="#7B68EE", font_size=32).move_to([-2.1, chart_base_y - 0.35, 0])
        ke_label = Tex(r"\frac{1}{2}mv^2", color="#F4A460", font_size=32).move_to([-0.1, chart_base_y - 0.35, 0])
        total_label = Tex(r"E", color="#E77471", font_size=32).move_to([2.1, chart_base_y - 0.35, 0])
        self.add(pe_label, ke_label, total_label)

        def get_pe_ratio():
            th = get_theta()
            return (1 - np.cos(th)) / (1 - np.cos(theta_max))

        pe_bar = always_redraw(lambda: Rectangle(
            width=bar_width,
            height=max(0.01, get_pe_ratio() * max_bar_height),
            fill_color="#7B68EE",
            fill_opacity=0.9,
            stroke_width=0
        ).move_to([-2.1, chart_base_y + (get_pe_ratio() * max_bar_height) / 2, 0]))

        ke_bar = always_redraw(lambda: Rectangle(
            width=bar_width,
            height=max(0.01, (1 - get_pe_ratio()) * max_bar_height),
            fill_color="#F4A460",
            fill_opacity=0.9,
            stroke_width=0
        ).move_to([-0.1, chart_base_y + ((1 - get_pe_ratio()) * max_bar_height) / 2, 0]))

        total_bar = Rectangle(
            width=bar_width,
            height=max_bar_height,
            fill_color="#E77471",
            fill_opacity=0.9,
            stroke_width=0
        ).move_to([2.1, chart_base_y + max_bar_height / 2, 0])
        self.add(pe_bar, ke_bar, total_bar)

        # 4. Formula at bottom
        formula = Tex(
            r"mgh", r" + ", r"\frac{1}{2}mv^2", r" = ", r"E",
            font_size=38
        )
        formula[0].set_color("#7B68EE")
        formula[2].set_color("#F4A460")
        formula[4].set_color("#E77471")
        formula.move_to([0, -2.4, 0])
        self.add(formula)

        # 5. Play Animation (approx 6 seconds)
        self.play(
            time_tracker.animate.set_value(6),
            run_time=6,
            rate_func=linear
        )
        self.wait(1)
