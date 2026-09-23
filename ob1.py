from manimlib import *
import numpy as np

class EnhancedDopplerEffect(Scene):
    def construct(self):
        # Physics Parameters
        v_sound = 5.0
        v_car = 2.2
        f_src = 1213
        emit_rate = 7.0 
        max_time = 7.0

        # Master Clock
        time_tracker = ValueTracker(0)

        # 1. Main Title
        title = Text("The Doppler Effect", font_size=56, font="Times New Roman")
        title.set_color("#F5E5C0")
        title.to_edge(UP, buff=0.6).shift(LEFT * 2) # Shifted left to make room for graph
        self.add(title)

        # 2. Road & Observer Setup (Same as before)
        road_group = VGroup()
        road_dashed = DashedLine(LEFT * 8, RIGHT * 8, stroke_width=4, color=GREY, dash_length=0.2)
        road_solid = Line(LEFT * 8, RIGHT * 8, stroke_width=4, color="#5C5C5C").shift(DOWN * 0.05) 
        road_group.add(road_solid, road_dashed).shift(DOWN * 1.5)
        
        observer = VGroup()
        head = Circle(radius=0.15, stroke_color=WHITE, stroke_width=3)
        body = Line(DOWN*0.15, DOWN*0.8, stroke_width=3)
        arms = Line(LEFT*0.3, RIGHT*0.3, stroke_width=3).shift(DOWN*0.3)
        leg1 = Line(DOWN*0.8, DOWN*1.3 + LEFT*0.2, stroke_width=3)
        leg2 = Line(DOWN*0.8, DOWN*1.3 + RIGHT*0.2, stroke_width=3)
        smile = Arc(start_angle=PI, angle=PI, radius=0.06, stroke_color=WHITE, stroke_width=2).move_to(head.get_center() + DOWN*0.03)
        eye1 = Dot(head.get_center() + UL*0.05, radius=0.02)
        eye2 = Dot(head.get_center() + UR*0.05, radius=0.02)
        observer.add(head, body, arms, leg1, leg2, smile, eye1, eye2)
        observer.move_to(ORIGIN).shift(DOWN * 0.18)
        
        obs_label = Text("Observer", font_size=18).next_to(observer, UP, buff=0.1)
        self.add(road_group, observer, obs_label)

        # 3. Car Setup
        car = VGroup()
        car_body = Polygon(
            [-0.8, -0.2, 0], [0.8, -0.2, 0], [0.8, 0.1, 0], 
            [0.4, 0.1, 0], [0.2, 0.4, 0], [-0.4, 0.4, 0], 
            [-0.6, 0.1, 0], [-0.8, 0.1, 0],
            fill_color=RED, fill_opacity=1, stroke_width=1, stroke_color=WHITE
        )
        w1 = Circle(radius=0.15, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=1).move_to([-0.5, -0.2, 0])
        w2 = Circle(radius=0.15, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=1).move_to([0.5, -0.2, 0])
        spoiler = Line([-0.7, 0.1, 0], [-0.9, 0.3, 0], stroke_width=5, stroke_color=RED)
        exhaust = Line([-0.8, -0.1, 0], [-1.2, -0.1, 0], stroke_width=4, stroke_color=YELLOW)
        car.add(car_body, w1, w2, spoiler, exhaust)
        
        car_start_pos = LEFT * 7 + DOWN * 1.3
        
        # New Updater: Sync car strictly to time_tracker
        car.add_updater(lambda m: m.move_to(car_start_pos + RIGHT * v_car * time_tracker.get_value()))
        self.add(car)

        # 4. EXTRA FEATURE: Live Frequency Graph
        axes = Axes(
            x_range=[0, max_time, 1],
            y_range=[500, 2500, 500],
            width=3.5,
            height=2,
            axis_config={"color": GREY_A, "include_tip": False}
        ).to_corner(UR, buff=0.5)
        
        # Add labels to axes
        axes.add_coordinate_labels(x_values=[], y_values=[1000, 2000], font_size=18)
        graph_label = Text("Frequency (Hz) vs Time", font_size=18, color=YELLOW).next_to(axes, UP, buff=0.2)
        
        # Invisible dot that traces the graph
        graph_dot = Dot(color=YELLOW, radius=0.04)
        graph_line = TracedPath(graph_dot.get_center, stroke_color=YELLOW, stroke_width=3)
        self.add(axes, graph_label, graph_line, graph_dot)

        # 5. Formula & Live Text
        formula = Tex(r"f_{obs} = f_{src} \frac{v_{sound}}{v_{sound} - v_{radial}}", font_size=40)
        formula_box = SurroundingRectangle(formula, color="#64B5F6", buff=0.25, stroke_width=2)
        formula_box.round_corners(0.1) # Fixed corner error
        formula_group = VGroup(formula, formula_box).to_edge(DOWN, buff=0.5)
        self.add(formula_group)

        f_text = Tex(r"f \approx", font_size=48).shift(DOWN * 2 + LEFT * 0.8)
        f_num = DecimalNumber(0, num_decimal_places=0, font_size=48)
        f_num.next_to(f_text, RIGHT, buff=0.15)
        hz_text = Tex(r"\text{ Hz}", font_size=48).next_to(f_num, RIGHT, buff=0.15)
        
        # Super Updater for Text and Graph
        def update_data(mob):
            t = time_tracker.get_value()
            diff = observer.get_center() - car.get_center()
            dist = np.linalg.norm(diff)
            v_rad = (v_car * diff[0] / dist) if dist != 0 else 0
            
            f_obs = f_src * v_sound / (v_sound - v_rad)
            
            # Update Text
            mob.set_value(f_obs)
            mob.next_to(f_text, RIGHT, buff=0.15)
            hz_text.next_to(mob, RIGHT, buff=0.15)
            
            # Update Graph Dot
            graph_dot.move_to(axes.c2p(t, f_obs))
            
        f_num.add_updater(update_data)
        self.add(f_text, f_num, hz_text)

        # 6. Wave Engine (Same as before)
        waves = VGroup()
        self.add(waves)
        self.bring_to_front(road_group, car, observer, obs_label) 

        self.time_since_last_wave = 0
        def update_waves(mob, dt):
            for wave in list(mob):
                wave.set_width(wave.get_width() + 2 * v_sound * dt)
                w = wave.get_width()
                opacity = max(0, 1 - (w / 14.0)) 
                wave.set_stroke(opacity=opacity)
                if w > 14.0:
                    mob.remove(wave)
            
            self.time_since_last_wave += dt
            if self.time_since_last_wave >= 1.0 / emit_rate:
                new_wave = Circle(radius=0.01, stroke_color="#64B5F6", stroke_width=2)
                new_wave.move_to(car.get_center() + RIGHT * 0.4) 
                mob.add(new_wave)
                self.time_since_last_wave = 0
                
        waves.add_updater(update_waves)

        # 7. Add Sync Audio (If generated)
        self.add_sound("doppler_sound.wav", fade_in=1.0, fade_out=1.0)

        # 8. Animate Everything via the Master Clock
        self.play(
            time_tracker.animate.set_value(max_time),
            run_time=max_time,
            rate_func=linear
        )
        self.wait(1)
