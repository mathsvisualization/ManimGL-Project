from manimlib import *

class PaidTemplate(InteractiveScene):
    pgno = "1"
    title_0 = "Ultimate Learning Bundle (200+GB)"

    def setup(self):
        super().setup()
        self.logo = logo = Tex(R"\langle \psi \rangle")
        logo.scale(0.8)
        logo.set_color(PURPLE_A)
        logo.to_edge(UL, buff=MED_SMALL_BUFF)
        self.add(logo)

        self.v_line = v_line = Line(UP, DOWN)
        v_line.set_height(logo.get_height() * 1.5)
        v_line.next_to(logo, RIGHT, buff=MED_SMALL_BUFF)
        v_line.insert_n_curves(10)
        v_line.set_stroke(width=[0.5, 1.5, 1.5, 0.5])
        self.add(v_line)

        self.h_line = h_line = Line(LEFT, RIGHT)
        h_line.set_width(FRAME_WIDTH - 1)
        h_line.to_edge(DOWN, buff=MED_LARGE_BUFF * 0.75 + SMALL_BUFF)
        h_line.insert_n_curves(10)
        h_line.set_stroke(width=[0.5, 2, 2, 0.5])
        self.add(h_line)

        pg = TexText(str(self.pgno))
        cir = Circle(radius=0.1)
        cir.set_stroke(width=1, color=WHITE)
        cir.set_fill("#191919", 1.0)
        pg.move_to(cir)
        pg.set_height(cir.get_height() * 0.5)
        vg = VGroup(cir, pg)
        vg.next_to(h_line, DOWN, buff=SMALL_BUFF)
        self.add(vg)

        self.title = title = TexText(str(self.title_0), font_size=30)
        title.next_to(self.v_line, RIGHT)
        self.add(title)

class Paid(PaidTemplate):
    pgno = "1"

    def construct(self):
        cont = TexText(R"The Knowledge Vault")
        cont.next_to(self.logo, DOWN, buff=LARGE_BUFF * 0.5, aligned_edge=LEFT)
        cont.shift(RIGHT * 0.35)
        cont_underline = Underline(cont, stroke_width=[0.5, 2, 2, 0.5])
        self.add(cont, cont_underline)

        cont1 = TexText("200GB+ Curated Educational Library", font_size=30)
        cont1.next_to(cont, DOWN, buff=MED_LARGE_BUFF * 0.45)
        # cont1.to_edge(RIGHT)
        self.add(cont1)

        itm = BulletedList(
            "7000+ PDFs",
            "Books",
            "Lecture Notes",
            "Research Papers",
            "Beginners to Advanced Resources",
            buff=SMALL_BUFF,
            font_size=26
        )
        itm.next_to(cont1, DOWN, buff=MED_LARGE_BUFF * 0.45, aligned_edge=LEFT)
        self.add(itm)

        cont2 = TexText(
            R"""
            \begin{minipage}{0.85\textwidth}
            Whether you're a student, self-learner, programmer,
            researcher, or simply curious about science, this
            collection brings thousands of carefully organized
            educational resources together in one place.
            \end{minipage}
            """,
            font_size=20,
        )
        cont2.next_to(itm, DOWN, buff=MED_LARGE_BUFF * 0.45, aligned_edge=LEFT)
        self.add(cont2)

        inside = VGroup(
            TexText("Inside you'll find:", font_size=26),
            BulletedList(
                "Mathematics",
                "Physics",
                "Chemistry",
                "Quantum Mechanics",
                "Astronomy",
                "Computer Science",
                R"Artificial Intelligence \& Machine Learning",
                buff=SMALL_BUFF,
                font_size=20
            )
        )
        inside.arrange(DOWN, buff=SMALL_BUFF, aligned_edge=LEFT)
        inside[0].shift(LEFT * 0.5)
        inside.next_to(cont2, DOWN, aligned_edge=LEFT)
        self.add(inside)


class Paid2(PaidTemplate):
    pgno = "2"

    def construct(self):
        why = TexText("Why This Collection?", font_size=40)
        why.next_to(self.logo, DOWN, buff=MED_LARGE_BUFF, aligned_edge=DL)
        why.shift(0.1 * DR)
        self.add(why)

        why_body = TexText(
            r"""
            $\checkmark$ Save hundreds of hours searching for\\
            \hspace*{0.45cm}quality resources.\\[0.25cm]
            $\checkmark$ Beginner to Advanced learning materials.\\[0.25cm]
            $\checkmark$ Books, Lecture Notes, and Research Papers.\\[0.25cm]
            $\checkmark$ Carefully organized folders for easy navigation.\\[0.25cm]
            $\checkmark$ Covers Mathematics, Physics, Chemistry,\\
            \hspace*{0.45cm}Computer Science, AI, Astronomy, and more.\\[0.25cm]
            $\checkmark$ Suitable for students, self-learners,\\
            \hspace*{0.45cm}educators, and enthusiasts.
            """, alignment=r"\flushleft", font_size=28,
        )
        why_body.next_to(why, DOWN, aligned_edge=LEFT).shift(0.05*LEFT)
        self.add(why_body)

class Pricing(PaidTemplate):
    pgno = "3"
    
    def construct(self):
        price = TexText(R"\$ Pricing").scale(1.2)
        price.next_to(self.title, DOWN, buff=LARGE_BUFF * 0.8).shift(0.5 * LEFT)
        under = Underline(price, stroke_width=[0.5, 1.5, 1.5, 0.5])
        self.add(price, under)
        pricing = TexText(r"""
            \begin{tabular}{lr}
            Mathematics & \$8.99\\
            Physics & \$6.99\\
            Chemistry & \$4.99\\
            Quantum Mechanics & \$7.99\\
            Astronomy & \$4.99\\
            Ai \& ML & \$9.99\\
            Computer Science & \$8.99\\[0.3cm]
            \textbf{Full Bundle (200GB+)} & \textbf{\$29.99}
            \end{tabular}
            """, font_size=30)
        pricing.next_to(price, DOWN, buff=MED_LARGE_BUFF)
        self.add(pricing)

class Payment(PaidTemplate):
    pgno = "4"

    def construct(self):
        title = TexText(R"Interested?").scale(0.7)
        title.next_to(self.logo, DOWN, buff=LARGE_BUFF * 0.85, aligned_edge=LEFT).shift(RIGHT * 0.1)
        under = Underline(title, stroke_width=[0.5, 1.5, 1.5, 0.5])
        self.add(title, under)

        body = TexText(
            r"""
            DM or Comment with:\\[0.25cm]
            \textbf{MATH}\\[0.25cm]
            \textbf{PHYSICS}\\[0.25cm]
            \textbf{CHEMISTRY}\\[0.25cm]
            \textbf{QUANTUM}\\[0.25cm]
            \textbf{ASTRONOMY}\\[0.25cm]
            \textbf{AI \& ML}\\[0.25cm]
            \textbf{COMPUTER SCIENCE}\\[0.25cm]
            \textbf{FULL (Recommended)}
            """, isolate=['FULL (Recommended)'], alignment=R"\flushleft", font_size=20,
        )
        body['FULL (Recommended)'].set_color(YELLOW)
        body.next_to(title, DOWN, buff=MED_LARGE_BUFF * 0.67, aligned_edge=LEFT)
        self.add(body)

        payment = TexText(R"Payment Methods $\checkmark$").scale(0.7)
        payment[-1].set_color(GREEN)

        payment_un = Line(LEFT, RIGHT)
        payment_un.set_width(payment.get_width() * 1.2)
        payment_un.insert_n_curves(10)
        payment_un.set_stroke(width=[0.5, 1.5, 1.5, 0.5])
        payment_un.next_to(under, RIGHT, buff=LARGE_BUFF * 0.85)
        payment.next_to(payment_un, UP, buff=SMALL_BUFF).shift(0.15 * LEFT)
        self.add(payment, payment_un)

        svgs = VGroup(
            SVGMobject("./lmao/paypal.svg"),
            SVGMobject("./lmao/upi.svg"),
            SVGMobject("./lmao/debit.svg").set_color(WHITE)
        )
        svgs.scale(0.4)
        svgs.arrange(DOWN, buff=MED_LARGE_BUFF * 0.8, aligned_edge=LEFT)
        svgs.next_to(payment, DOWN, aligned_edge=LEFT)
        svgs[1][0].set_color(WHITE)
        svgs[1][1].set_color(WHITE)
        self.add(svgs)

        info = TexText(
            r"""
            $\checkmark$ Instant delivery after payment.\\[0.25cm]
            $\checkmark$ Secure cloud download link.\\[0.25cm]
            $\checkmark$ Lifetime access to purchased content.\\[0.25cm]
            $\checkmark$ Free future updates (where applicable).
            """, alignment=R"\flushleft",
            font_size=22,
        )
        info.next_to(body, DOWN, aligned_edge=LEFT)
        self.add(info)

        dis = TexText("For educational purposes only.")
        dis.scale(0.20)
        dis.next_to(self.h_line.get_start(), DOWN, buff=MED_SMALL_BUFF * 0.67, aligned_edge=DL)
        self.add(dis)

        dis2 = TexText(R"Digital product $\cdot$ No physical shipping.")
        dis2.scale(0.20)
        dis2.next_to(self.h_line.get_end(), DOWN, buff=MED_SMALL_BUFF * 0.67, aligned_edge=DR)
        self.add(dis2)

class Dis(PaidTemplate):
    pgno = "5"

    def construct(self):
        t = TexText("Disclaimer:")
        t.next_to(self.logo, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        t.shift(0.25 * RIGHT)
        under = Underline(t, stroke_width=[0.5, 1.5, 1.5, 0.5])
        self.add(t, under)
        dis = TexText(
            R"""
            \begin{minipage}{0.33\textwidth}
            This collection contains educational resources gathered and organized
            for convenience. I do not claim ownership of any third-party copyrighted
            content. All rights remain with their respective authors, publishers,
            and copyright holders.
            \end{minipage}
            """, alignment=R"\flushleft"
        )
        dis.set_width(FRAME_WIDTH - 1)
        dis.next_to(t, DOWN, buff=MED_LARGE_BUFF, aligned_edge=LEFT)
        self.add(dis)