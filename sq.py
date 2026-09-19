from manimlib import *

class CascadingFunctionGrowth(Scene):
    def construct(self):
        # Title ko ek baar establish karte hain
        title = Text("How Fast Can a Function Grow?", font_size=36)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))

        # Data for functions: (Name, Math LaTeX, Color)
        # Size aur scale code ke logic se handle hoga
        stages = [
            ("quadratic", "n^2", BLUE_E),
            ("factorial", "n!", TEAL_E),
            ("exponential", "2^n", YELLOW_E),
            ("double exponential", "2^{2^n}", RED_E),
        ]

        # Ye group humare cascade hone wale boxes ko store karega
        receding_stack = VGroup()

        for name, formula_str, color in stages:
            # 1. Create the NEW, largest card at the center
            # Is card ka initial size hum fix rakhte hain (jaise Square ka side 4)
            box = Square(side_length=4, fill_color=color, fill_opacity=0.8)
            box.set_stroke(WHITE, width=2)
            
            # Label elements for the box
            lbl = Text(name, font_size=24).next_to(box.get_top(), DOWN, buff=0.3)
            form = Tex(formula_str, font_size=60)
            form.move_to(box.get_center())
            
            new_card = VGroup(box, lbl, form)
            
            # 2. Logic to shift and scale existing stack
            animations = []
            if len(receding_stack) > 0:
                # Agar koi pichhle cards hain, unhe LEFT move karo aur resize karo
                # 'shift_vector' har card ko kitna door le jana hai, use define karta hai
                shift_vector = LEFT * 3
                
                # Hum pure group ko move karte hain, par cards par cascade effect pane ke liye 
                # har single card ko individual animation provide karni hogi loop me
                for i, card in enumerate(receding_stack):
                    # Kitna pichhe ja raha hai (age ke hisaab se), uske basis par scale aur opacity set karein
                    # Jitna purana card (i index chhota), utna chhota aur dim
                    target_scale = 0.5 ** (len(receding_stack) - i) 
                    target_opacity = 0.6 ** (len(receding_stack) - i)
                    
                    animations.append(
                        card.animate
                        .shift(shift_vector)
                        .scale(0.8) # Cascade shrinking: sabhi card thoda chhote honge
                        .set_opacity(target_opacity)
                    )
            
            # 3. Perform the cascading shift and show the new card
            self.play(
                *animations,
                FadeIn(new_card, scale=0.5),
                run_time=1.5
            )
            
            # Naye card ko stack me add karein agle loop ke liye
            receding_stack.add(new_card)
            
            # Thodi der wait karein har stage par
            self.wait(1.5)

        self.wait(3)

