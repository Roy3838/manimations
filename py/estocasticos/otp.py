from manim import *
import numpy as np
import random as rd
from hashlib import sha256
import itertools as it
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

def sha256_tex(message, n_forced_start_zeros = 0):
    true_bit_string = sha256_bit_string(message)
    n = n_forced_start_zeros
    bit_string = "0"*n + "1" + true_bit_string[n:]
    
    return bit_string

def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m

class OTP(Scene):
    def construct(self):
        # set background color

        self.camera.background_color = "#E2E2E2"
        def intro():
            # Funcion encripcion
            message = MathTex("Mensaje").set_color(BLACK).shift(2*UP)
            encryption_f_x= MathTex("Encripcion(","Mensaje",", ","Llave",") = ", "Cypher").set_color(BLACK)
            decryption_f_x= MathTex("Decripcion(","Cypher",", ","Llave",") = ","Mensaje").set_color(BLACK)

            # encryption and decryption equations
            enc_eq = MathTex("Cypher = Texto \\oplus Llave").scale(1.5)
            dec_eq = MathTex("Texto = Cypher \\oplus Llave").scale(1.5)

            # box en la llave
            key_box = SurroundingRectangle(encryption_f_x[3], buff = 0.1).set_color(GOLD)

            self.play(Write(message))
            self.play(
                message.animate.move_to(encryption_f_x[1].get_center()),
                Write(encryption_f_x[0]),
                Write(encryption_f_x[2:])
                )
            self.play(Write(key_box))
            self.wait(1)
            self.play(FadeOut(encryption_f_x), FadeOut(message), FadeOut(key_box))



        def xor_is_reversible_animation():

            # xor operation equations LaTeX

            texto1=Text("operacion XOR").scale(0.7).to_edge(UL).set_color(BLACK)
            bits=MathTex('0 \\oplus 0 = 0').scale(0.7).shift(UP).set_color(BLACK)
            bits2=MathTex("0 \\oplus 1 = 1").scale(0.7).next_to(bits,DOWN).set_color(BLACK)
            bits3=MathTex("1 \\oplus 0 = 1").scale(0.7).next_to(bits2,DOWN).set_color(BLACK)
            bits4=MathTex("1 \\oplus 1 = 0").scale(0.7).next_to(bits3,DOWN).set_color(BLACK)

            # boxes around xor operations
            boxbits=SurroundingRectangle(bits, buff=0.1).set_color(GOLD)
            boxbits2=SurroundingRectangle(bits2, buff=0.1).set_color(GOLD)
            boxbits3=SurroundingRectangle(bits3, buff=0.1).set_color(GOLD)
            boxbits4=SurroundingRectangle(bits4, buff=0.1).set_color(GOLD)

            # show that it is like a sum
            sum1=MathTex("0 + 0 = 0").scale(0.7).next_to(bits,2*RIGHT).set_color(BLACK)
            sum2=MathTex("0 + 1 = 1").scale(0.7).next_to(bits2,2*RIGHT).set_color(BLACK)
            sum3=MathTex("1 + 0 = 1").scale(0.7).next_to(bits3,2*RIGHT).set_color(BLACK)
            sum4=MathTex("1 + 1 = 2").scale(0.7).next_to(bits4,2*RIGHT).set_color(BLACK)

            #boxes around the sum
            box1=SurroundingRectangle(sum1, buff=0.1).set_color(GOLD)
            box2=SurroundingRectangle(sum2, buff=0.1).set_color(GOLD)
            box3=SurroundingRectangle(sum3, buff=0.1).set_color(GOLD)
            box4=SurroundingRectangle(sum4, buff=0.1).set_color(GOLD)

            # xor operation equation general
            xor=MathTex("a \\oplus b = c").scale(0.7).shift(UP).set_color(BLACK)

            # xor operation equation with mod
            xor2=MathTex("(a+b)\\mod 2 \\equiv c ").scale(0.7).shift(UP).set_color(BLACK)

            # xor operation showing 2 mod 2 = 0
            xor3=MathTex("2\\mod 2 = 0").scale(0.7).shift(UP).set_color(BLACK)





            # self.play(Write(texto1))
            # self.play(Write(bits),Write(bits2),Write(bits3),Write(bits4))
            # self.wait(1)
            # self.play(Write(sum1),Write(sum2),Write(sum3),Write(sum4))
            # self.wait(1)
            # self.play(Write(boxbits),Write(boxbits2),Write(boxbits3),Write(boxbits4))
            # self.wait(1)
            # self.play(
            #     ReplacementTransform(boxbits,box1),
            #     ReplacementTransform(boxbits2,box2),
            #     ReplacementTransform(boxbits3,box3),
            #     ReplacementTransform(boxbits4,box4)
            # )
            # self.play(box4.animate.set_color(RED))

            # self.wait(1)











        def message_send_animation():

            # OTP es un hash de un numero random 
            rd.seed(1) # para que siempre sea el mismo numero random
            salt = str(rd.randint(1,99))
            digest_text_OTP=sha256_tex(salt)
            OTP_text=sha256_tex_mob(salt).set_color(BLACK)
            OTP_text.scale(0.65)
            OTP_copy=OTP_text.copy()

            mensajestring="Faty"
            mensaje=Text("Mensaje: \"" + mensajestring + "\"").set_color(BLACK).shift(UP+LEFT*2).scale(0.6)
            

            # convertir Texto de mensaje a binario
            binstring=' '.join(format(ord(x), 'b') for x in mensajestring)
            text_mensaje=Text(binstring).set_color(BLACK).scale(0.5)
            mensaje_copy=text_mensaje.copy().shift(UP*2+RIGHT*3)

            # XOR combinacion de mensajestring y texto1
            #mensajebin=mensajestring.encode('utf-8')
            #hexdigest = sha256(OTP_text.get_text().encode('utf-8')).hexdigest()
            #otpbin=bin(int(hexdigest, 16))[2:]

            # YA ES MENSAJE DE OTP STRING
            v1 = digest_text_OTP
            v2 = binstring
            v2 = v2.replace(" ", "")
            # XOR
            new = [(ord(a) ^ ord(b)) for a,b in zip(v1, v2)]
            # change from list of strings to string
            new = ''.join(map(str, new))

            #Mobject with the XOR result
            key_string_bit=Text(new).set_color(BLACK).scale(0.45).shift(LEFT*3)
            key_string_bit_copy=key_string_bit.copy().shift(RIGHT*3)
            
            

            self.play(Write(mensaje))
            self.play(Create(text_mensaje))
            self.play(mensaje.animate.shift(UP*2+LEFT*3), text_mensaje.animate.shift(UP*2+LEFT*3))

            self.play(Write(OTP_text))
            self.play(OTP_text.animate.shift(DOWN*2+LEFT*3))


            """  SE VA A HACER LA ANIMACION DE LA COMBINACION XOR DEL MENSAJE Y LA LLAVE  """    
            animationlenght=len(new)   # change to make rendering quicker  
            for i in range(animationlenght):
                time=0.4
                if i>10:
                    time=0.2
                self.play(ReplacementTransform(
                    OTP_text[i], key_string_bit[i]
                ),
                ReplacementTransform(
                    text_mensaje[i], key_string_bit[i]
                )
                ,run_time=time)
            OTP_copy.shift(DOWN*2+RIGHT*3)
            self.play(Create(OTP_copy))
            self.remove(key_string_bit, OTP_text[:len(new)])
            self.play(key_string_bit.animate.shift(RIGHT*6))
            self.add(key_string_bit_copy.shift(RIGHT*3))
            #self.play(Create(mensaje_copy))


            for k in range(animationlenght):
                time=0.4
                if k>10:
                    time=0.2
                self.remove(key_string_bit[k])
                self.play(ReplacementTransform(
                    key_string_bit_copy[k],mensaje_copy[k] 
                ),
                ReplacementTransform(
                    OTP_copy[k],mensaje_copy[k] 
                )
                ,run_time=time)
                



            self.wait()
            self.play(mensaje.animate.shift(RIGHT*7))

            self.wait()

        intro()
        #xor_is_reversible_animation()
        #message_send_animation()
