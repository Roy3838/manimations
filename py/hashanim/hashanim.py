from manim import *
from hashlib import sha256
import itertools as it
import binascii
import random

#imported from cripto 3b1b video
def sha256_bit_string(message):
    hexdigest = sha256(message.encode('utf-8')).hexdigest()
    return bin(int(hexdigest, 16))[2:]

def bit_string_to_mobject(bit_string):
    line = Text("0"*32)
    pre_result = VGroup(*[
        line.copy() for row in range(8)
    ])
    pre_result.arrange(DOWN, buff = SMALL_BUFF)
    result = VGroup(*it.chain(*pre_result))
    result.scale(0.7)
    bit_string = (256 - len(bit_string))*"0" + bit_string

    for i, (bit, part) in enumerate(zip(bit_string, result)):
        if bit == "1":
            one = Tex("1")[0]
            one.replace(part, dim_to_match = 1)
            result.submobjects[i] = one

    return result

def sha256_tex_mob(message, n_forced_start_zeros = 0):
    true_bit_string = sha256_bit_string(message)
    n = n_forced_start_zeros
    bit_string = "0"*n + "1" + true_bit_string[n:]
    
    return bit_string_to_mobject(bit_string)


class hashexplanation(Scene):
    def construct(self):
        self.camera.background_color = "#E2E2E2"
        self.hashfunction()

    def hashfunction(self):
        
        def make_hash_function(message):
            # hash with message
            Inputbefore = Text("Hash( \"").scale(0.6).move_to(3 * LEFT).set_color(BLACK)

            messagehash = sha256_tex_mob(message).scale([0.4, 0.6, 1]).set_color(BLACK)
            messagemob = Text(message, color=BLUE).scale(0.6)

            # centering and aligning
            widthofmessage = messagemob.get_width()

            # messagemob moved to inputright with buffer messagewidth --> |-----.-----|
            messagemob.move_to(Inputbefore.get_right() + widthofmessage / 2 * RIGHT + 0.05 * RIGHT)
            # Input after moved to messageright with buffer widthInput  |-----.-----| <---

            Inputafter = Text("\" ) = ").scale(0.6).set_color(BLACK)
            Inputwidth = Inputafter.get_width()
            Inputafter.move_to(messagemob.get_right() + Inputwidth / 2 * RIGHT + 0.05 * RIGHT)
            Input = VGroup(Inputbefore, messagemob, Inputafter)
        
            # offset both mobjects to center equal sign 
            Input.shift(widthofmessage*LEFT + RIGHT)

            # Find the position of the equal sign and align messagehash to it
            equals_sign = Inputafter[1]  # Assuming the equal sign is the second character in Inputafter
            messagehash.next_to(equals_sign, RIGHT, buff=0.5)

            return [Input, messagehash]

        [Input,messagehash]=make_hash_function("Mensaje")
        [SecondImput,Secondmessagehash]=make_hash_function("mensaje")
        [ThirdImput,Thirdmessagehash]=make_hash_function("mensaje1")
        [FourthImput,Fourthmessagehash]=make_hash_function("mensaje2")

        pos = Input.get_center() + LEFT*0.22
        arrow = Arrow(pos + UP*1.5, pos, buff=0.3, color=BLACK)
        poshash = messagehash.get_center()
        hashbrace = Brace(messagehash, direction=UP, color=BLACK)
        texto_completamente_diferente = hashbrace.get_tex("Completamente\ diferente!").scale(0.6).set_color(BLACK)

        self.play(Write(Input))
        self.play(Write(messagehash))
        self.play(Write(arrow))
        self.play(ReplacementTransform(Input,SecondImput),
                ReplacementTransform(messagehash,Secondmessagehash))
        self.play(Write(hashbrace))

        self.wait()
        self.play(Write(texto_completamente_diferente))
        
        self.play(ReplacementTransform(SecondImput,ThirdImput),
                ReplacementTransform(Secondmessagehash,Thirdmessagehash))
        self.play(ReplacementTransform(ThirdImput,FourthImput),
                ReplacementTransform(Thirdmessagehash,Fourthmessagehash))
        
        self.wait()
    