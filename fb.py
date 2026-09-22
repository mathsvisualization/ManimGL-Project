from manimlib import *
import numpy as np

class WaveExtrapolation(Scene):
    def construct(self):
        # 1. Main Title
        title = Text("Wave Extrapolation", font_size=56)
        title.set_color("#F5E5C0")  # Soft yellowish cream
        title.to_edge(UP, buff=0.3)
        self.add(title)

        # 2. Bottom Equation
        formula = Tex(r"y_N(t) = \sum_{k=0}^{N-1} \text{y-pos}(\text{Shape}_k(t))", font_size=40)
        formula.to_edge(DOWN, buff=0.3)
        self.add(formula)

        # 3. Setup Variables & Tracker
        time_tracker = ValueTracker(0)
        max_time = 4 * TAU  # 4 full cycles

        # Colors and Names matching the visuals
        colors = ["#E57373", "#64B5F6", "#FFF176", "#4DB6AC", "#E0E0E0"]
        names = ["Heart", "Circle", "Astroid", "Star", "Lemniscate"]
        y_positions = [2.4, 1.2, 0.0, -1.2, -2.4]

        # 4. Parametric Functions for Shapes (Returning 3D vectors)
        def heart(t):
            x = 16 * np.sin(t)**3
            y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
            return np.array([x, y, 0]) * 0.035

        def circle(t):
            return np.array([0.5 * np.cos(t), 0.5 * np.sin(t), 0])

        def astroid(t):
            return np.array([0.5 * np.cos(t)**3, 0.5 * np.sin(t)**3, 0])

        def star(t):
            # Perimeter tracing of a 5-pointed star via linear interpolation
            R_out = 0.55
            R_in = R_out * 0.4
            segment_angle = TAU / 10
            t_mod = t % TAU
            i = int(t_mod / segment_angle)
            local_t = (t_mod % segment_angle) / segment_angle

            def get_vert(idx):
                r = R_out if idx % 2 == 0 else R_in
                angle = PI / 2 - idx * segment_angle
                return np.array([r * np.cos(angle), r * np.sin(angle), 0])

            v1 = get_vert(i)
            v2 = get_vert(i + 1)
            return v1 + local_t * (v2 - v1)

        def lemniscate(t):
            # Bernoulli Lemniscate
            scale = 0.6
            denom = 1 + np.sin(t)**2
            x = scale * np.cos(t) / denom
            y = scale * np.cos(t) * np.sin(t) / denom
            return np.array([x, y, 0])

        funcs = [heart, circle, astroid, star, lemniscate]

        # Coordinate boundaries
        shape_center_x = -4.5
        wave_start_x = -2.5
        x_scale = 0.45  # Controls how fast the wave stretches horizontally

        # 5. Build Each Row Dynamically
        for i in range(5):
            shape_origin = np.array([shape_center_x, y_positions[i], 0])

            # Base shape outline (faded)
            shape_path = ParametricCurve(
                funcs[i], t_range=[0, TAU, 0.05],
                color=colors[i], stroke_width=2, stroke_opacity=0.6
            )
            shape_path.shift(shape_origin)
            self.add(shape_path)

            # Text Label
            label = Text(names[i], font_size=26, color=colors[i])
            label.move_to([wave_start_x + 0.8, y_positions[i] + 0.45, 0])
            self.add(label)

            # Horizontal baseline
            baseline = Line(
                np.array([shape_center_x, y_positions[i], 0]),
                np.array([6, y_positions[i], 0]),
                color=GREY, stroke_width=1, stroke_opacity=0.5
            )
            self.add(baseline)

            # Moving dot on the shape
            dot = Dot(color=WHITE, radius=0.06)
            
            # Python closure factory to bind variables for updaters correctly
            def get_dot_updater(func, origin):
                return lambda d: d.move_to(func(time_tracker.get_value()) + origin)
            
            dot.add_updater(get_dot_updater(funcs[i], shape_origin))
            self.add(dot)

            # Invisible dot tracing the leading tip of the wave
            wave_edge = Dot(radius=0)
            def get_wave_edge_updater(d_obj):
                return lambda w: w.move_to(
                    np.array([wave_start_x + time_tracker.get_value() * x_scale, d_obj.get_center()[1], 0])
                )
                
            wave_edge.add_updater(get_wave_edge_updater(dot))
            self.add(wave_edge)

            # Traced path that leaves a trail behind wave_edge
            wave_trail = TracedPath(wave_edge.get_center, stroke_color=colors[i], stroke_width=3)
            self.add(wave_trail)

            # Connecting dashed line
            dashed_line = DashedLine(color=WHITE, stroke_width=2)
            def get_line_updater(d_obj, w_obj):
                return lambda l: l.put_start_and_end_on(d_obj.get_center(), w_obj.get_center())
                
            dashed_line.add_updater(get_line_updater(dot, wave_edge))
            self.add(dashed_line)

        # 6. Play the Animation
        self.play(
            time_tracker.animate.set_value(max_time),
            run_time=12,
            rate_func=linear
        )
        self.wait(1)
