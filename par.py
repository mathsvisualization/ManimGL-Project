from manimlib import *
import numpy as np

class WaveExtrapolation(Scene):
    def construct(self):
        # 1. Mathematical curves
        curves_data = [
            {
                "name": "Circle",
                "color": BLUE,
                "func": lambda t: np.array([np.cos(t), np.sin(t), 0]),
                "pos": UP * 1.5,
            },
            {
                "name": "Astroid",
                "color": TEAL,
                "func": lambda t: np.array([np.cos(t)**3, np.sin(t)**3, 0]),
                "pos": DOWN * 1.5,
            }
        ]

        time_tracker = ValueTracker(0)

        # FIX: Ek helper function banaya taaki variables ka scope alag rahe
        def create_shape_and_wave(data):
            func = data["func"]
            base_pos = data["pos"]
            color = data["color"]

            # Main closed shape outline
            shape = ParametricCurve(
                func,
                t_range=[0, TAU, 0.02],
                color=color,
                stroke_width=3
            ).scale(0.8).shift(base_pos + LEFT * 3.5)

            # Dot jo curve ke upar run karega
            dot = Dot(color=WHITE, radius=0.06)
            dot.add_updater(lambda m: m.move_to(
                shape.point_from_proportion((time_tracker.get_value() / TAU) % 1)
            ))

            # Extrapolated wave
            wave = VMobject(color=color, stroke_width=3)

            def get_wave_points():
                t_current = time_tracker.get_value()
                t_samples = np.linspace(max(0, t_current - TAU), t_current, 150)
                points = []
                for t in t_samples:
                    y_val = func(t % TAU)[1] * 0.8 + base_pos[1]
                    x_val = (base_pos[0] - 1.5) + (t_current - t) * 0.9
                    points.append([x_val, y_val, 0])
                return points

            wave.add_updater(lambda w: w.set_points_as_corners(get_wave_points()) if time_tracker.get_value() > 0.05 else w)

            # Connecting dashed line
            conn_line = DashedLine(stroke_width=1.5, color=GREY_A)
            conn_line.add_updater(lambda l: l.put_start_and_end_on(
                dot.get_center(),
                [base_pos[0] - 1.5, dot.get_center()[1], 0]
            ))

            # Label
            label = Text(data["name"], font_size=20, color=color)
            label.next_to(base_pos + RIGHT * 2.5, UP, buff=0.1)

            # In sabko return kar diya
            return [shape, dot, conn_line, wave, label]

        # 2. Loop ke zariye function call karke objects screen par add karna
        for data in curves_data:
            mobjects = create_shape_and_wave(data)
            self.add(*mobjects)

        # 3. Animation loop (2 cycles)
        self.play(
            time_tracker.animate.set_value(2 * TAU),
            run_time=8,
            rate_func=linear
        )
        self.wait()
