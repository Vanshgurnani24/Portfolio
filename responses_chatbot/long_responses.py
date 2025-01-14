import random

R_EAT="I don't like to eat anything because i'm a bot obviously"
R_ABOUT="I’m currently pursuing my bachelor's degree and I’m a computer enthusiast."
R_COMPINQ="I love anything related to computers! Whether it's coding, hardware, or exploring new technologies."
R_EDUCATION="I’m pursuing my bachelor's degree, and I’m passionate about computer science and technology."
R_FUTUREQUESTION="In the future, I want to dive deeper into technology and contribute to innovations in the computer science field."
R_CURRENTSTATE="Everything’s going well! Staying focused on my studies and keeping up with my tech interests."
R_INTEREST="Computers have always fascinated me. The endless possibilities for problem-solving and creating new things is what excites me the most."
R_PURSUING="I’m pursuing my bachelor’s because I want to expand my knowledge and skills to build a career in the tech industry."
R_WHATSNEW="Just busy with my studies, but I’m always looking for new tech-related projects to work on!"
R_GOALS="In five years, I hope to be working in the tech industry, possibly in software development or a related field, constantly learning and evolving."

def unknown():
    response=['Could you please rephrase that?',
              "...",
              "Sounds about right",
              "What does that mean?"][random.randrange(4)]
    return response