from manimlib import *
import numpy as np

class DopplerEffect(Scene):
    def construct(self):
        # Physics Parameters (reverse-engineered from your frequencies)
        v_sound = 5.0
        v_car = 2.2
        f_src = 1213
        emit_rate = 7.0  # Number of waves emitted per second
        
        # 1. Main Title
        title = Text("The Doppler Effect", font_size=56, font="Times New Roman")
        title.set_color("#F5E5C0")
        title.to_edge(UP, buff=0.6)
        self.add(title)

        # 2. Road Setup
        road_group = VGroup()
        road_dashed = DashedLine(LEFT * 8, RIGHT * 8, stroke_width=4, color=GREY, dash_length=0.2)
        road_solid = Line(LEFT * 8, RIGHT * 8, stroke_width=4, color="#5C5C5C")
        road_solid.shift(DOWN * 0.05) 
        road_group.add(road_solid, road_dashed)
        road_group.shift(DOWN * 1.5)
        
        # 3. Observer (Stick Figure)
        observer = VGroup()
        head = Circle(radius=0.15, stroke_color=WHITE, stroke_width=3)
        body = Line(DOWN*0.15, DOWN*0.8, stroke_width=3)
        arms = Line(LEFT*0.3, RIGHT*0.3, stroke_width=3).shift(DOWN*0.3)
        leg1 = Line(DOWN*0.8, DOWN*1.3 + LEFT*0.2, stroke_width=3)
        leg2 = Line(DOWN*0.8, DOWN*1.3 + RIGHT*0.2, stroke_width=3)
        
        # Smile and Eyes
        smile = Arc(start_angle=PI, angle=PI, radius=0.06, stroke_color=WHITE, stroke_width=2)
        smile.move_to(head.get_center() + DOWN*0.03)
        eye1 = Dot(head.get_center() + UL*0.05, radius=0.02)
        eye2 = Dot(head.get_center() + UR*0.05, radius=0.02)
        
        observer.add(head, body, arms, leg1, leg2, smile, eye1, eye2)
        observer.move_to(ORIGIN).shift(DOWN * 0.18)
        
        obs_label = Text("Observer", font_size=18).next_to(observer, UP, buff=0.1)
        self.add(road_group, observer, obs_label)

        # 4. Car Setup
        car = VGroup()
        car_body = Polygon(
            [-0.8, -0.2, 0], [0.8, -0.2, 0], [0.8, 0.1, 0], 
            [0.4, 0.1, 0], [0.2, 0.4, 0], [-0.4, 0.4, 0], 
            [-0.6, 0.1, 0], [-0.8, 0.1, 0],
            fill_color=RED, fill_opacity=1, stroke_width=1, stroke_color=WHITE
        )
        w1 = Circle(radius=0.15, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
        w1.move_to([-0.5, -0.2, 0])
        w2 = Circle(radius=0.15, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE, stroke_width=1)
        w2.move_to([0.5, -0.2, 0])
        spoiler = Line([-0.7, 0.1, 0], [-0.9, 0.3, 0], stroke_width=5, stroke_color=RED)
        exhaust = Line([-0.8, -0.1, 0], [-1.2, -0.1, 0], stroke_width=4, stroke_color=YELLOW)
        car.add(car_body, w1, w2, spoiler, exhaust)
        
        car.move_to(LEFT * 7 + DOWN * 1.3) # Start off-screen left
        
        # 5. Math Formula Box
        formula = Tex(r"f_{obs} = f_{src} \frac{v_{sound}}{v_{sound} - v_{radial}}", font_size=40)
        formula_box = SurroundingRectangle(formula, color="#64B5F6", buff=0.25, stroke_width=2, corner_radius=0.1)
        formula_group = VGroup(formula, formula_box).to_edge(DOWN, buff=0.5)
        self.add(formula_group)

        # 6. Dynamic Frequency Text
        f_text = Tex(r"f \approx", font_size=48).shift(DOWN * 2 + LEFT * 0.8)
        f_num = DecimalNumber(0, num_decimal_places=0, font_size=48)
        f_num.next_to(f_text, RIGHT, buff=0.15)
        hz_text = Tex(r"\text{ Hz}", font_size=48).next_to(f_num, RIGHT, buff=0.15)
        
        # Frequency Updater Logic
        def update_freq(mob):
            diff = observer.get_center() - car.get_center()
            dist = np.linalg.norm(diff)
            # Radial velocity is the component of the car's velocity moving directly towards the observer
            v_rad = (v_car * diff[0] / dist) if dist != 0 else 0
            
            # Doppler Equation
            f_obs = f_src * v_sound / (v_sound - v_rad)
            mob.set_value(f_obs)
            
            # Realign dynamically as number width changes
            mob.next_to(f_text, RIGHT, buff=0.15)
            hz_text.next_to(mob, RIGHT, buff=0.15)
            
        f_num.add_updater(update_freq)
        self.add(f_text, f_num, hz_text)

        # 7. Concentric Sound Waves Engine
        waves = VGroup()
        self.add(waves) # Add behind everything else
        self.bring_to_front(road_group, car, observer, obs_label) 

        self.time_since_last_wave = 0
        def update_waves(mob, dt):
            # Grow and fade existing waves
            for wave in list(mob):
                wave.set_width(wave.get_width() + 2 * v_sound * dt)
                w = wave.get_width()
                opacity = max(0, 1 - (w / 14.0)) # Fade out threshold
                wave.set_stroke(opacity=opacity)
                if w > 14.0:
                    mob.remove(wave)
            
            # Emit new waves based on emit_rate
            self.time_since_last_wave += dt
            if self.time_since_last_wave >= 1.0 / emit_rate:
                new_wave = Circle(radius=0.01, stroke_color="#64B5F6", stroke_width=2)
                # Emit from the front of the car
                new_wave.move_to(car.get_center() + RIGHT * 0.4) 
                mob.add(new_wave)
                self.time_since_last_wave = 0
                
        waves.add_updater(update_waves)

        # 8. Car Movement Updater
        car.add_updater(lambda m, dt: m.shift(RIGHT * v_car * dt))
        self.add(car)

        # 9. Play Scene
        self.wait(7) 
