from fpdf import FPDF


class Shirtificate(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 10, "CS50 Shirtificate", align="C", ln=True)
        self.ln(20)

    def create_shirtificate(self, name):
        self.add_page()
        self.set_font("Arial", "B", 40)
        self.image("shirtificate.png", x=0, y=60, w=210)
        self.set_text_color(255, 255, 255)  # White text
        self.cell(0, 190, f"{name}", align="C", ln=True)


def main():
    name = input("Enter your name: ")

    pdf = Shirtificate()
    pdf.set_auto_page_break(auto=False)
    pdf.create_shirtificate(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
