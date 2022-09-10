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
        #self.generalfunction()
        self.hashfunction()
    
    
    def generalfunction(self):
        function=MathTex(f"f(x)=x^{2}")
        self.play(Write(function))
        self.play(FadeOut(function))
        
        
        """
        
        """
        
        
    def hashfunction(self):
        #make scene to explain the identifying caracteristics that a hash function has
        
        def make_two_hash_function(message1, message2):
            Inputbefore=Text("Hash( \"").scale(0.6).move_to(3*LEFT)

            messagehash=sha256_tex_mob(message1+message2).scale([0.4,0.6,1])
            messagemob1 = Text(message1).scale(0.6)
            comma=Text(", ").scale(0.6)
            messagemob2 = Text(message2).scale(0.6)
            Inputafter=Text("\" ) = ").scale(0.6)

            # Align
            messagemob1.move_to(Inputbefore.get_right() + 0.95*RIGHT + 0.05*DOWN)
            comma.move_to(messagemob1.get_right()       + 0.1*RIGHT + 0.1*DOWN)
            messagemob2.align_on_border(messagemob1.get_right(), RIGHT)
            Inputafter.move_to(messagemob2.get_right()  + 0.45*RIGHT + 0.05*UP)

            # Color
            messagemob1.set_color(BLUE)
            messagemob2.set_color(BLUE)
            Inputbefore.set_color(BLACK)
            comma.set_color(BLACK)
            Inputafter.set_color(BLACK)
            messagehash.set_color(BLACK)
                        
            Input=VGroup(Inputbefore,messagemob1,messagemob2,comma,Inputafter)
            
            messagehash.move_to(Inputafter.get_right() + 2*RIGHT)
            
            
            return [Input,messagehash]
        
        
        def make_hash_function(message):
            #hash with message
            Inputbefore=Text("Hash( \"").scale(0.6).move_to(3*LEFT).set_color(BLACK)
            
            
            messagehash=sha256_tex_mob(message).scale([0.4,0.6,1]).set_color(BLACK)
            messagemob = Text(message,color=BLUE).scale(0.6)
                
            
            
            #centering and aligning
            widthofmessage=messagemob.get_width()
            
            # messagemob moved to inputright with buffer messagewidth --> |-----.-----|
            messagemob.move_to(Inputbefore.get_right()+widthofmessage/2*RIGHT + 0.05*RIGHT)
            # Input after moved to messageright with buffer widthInput  |-----.-----| <---
            
            Inputafter=Text("\" ) = ").scale(0.6).set_color(BLACK)
            Inputwidth=Inputafter.get_width()
            Inputafter.move_to(messagemob.get_right() + Inputwidth/2*RIGHT + 0.05*RIGHT)
            Input=VGroup(Inputbefore,messagemob,Inputafter)
            
            messagehash.move_to(Inputafter.get_right() + 2*RIGHT)
            return [Input,messagehash]
        
        
        [Input,messagehash]=make_hash_function("Message")
        [SecondImput,Secondmessagehash]=make_hash_function("Message1")
        [ThirdImput,Thirdmessagehash]=make_hash_function("Message2")
        [FourthImput,Fourthmessagehash]=make_hash_function("Message3")
        [two,hash2]=make_two_hash_function("Message","Salt")
        [three,hash3]=make_two_hash_function("Message","Salt2")
        self.play(Write(Input))
        self.play(Write(messagehash))
        self.play(ReplacementTransform(Input,SecondImput),ReplacementTransform(messagehash,Secondmessagehash))
        self.play(ReplacementTransform(SecondImput,ThirdImput),ReplacementTransform(Secondmessagehash,Thirdmessagehash))
        self.play(ReplacementTransform(ThirdImput,FourthImput),ReplacementTransform(Thirdmessagehash,Fourthmessagehash))
        self.play(ReplacementTransform(FourthImput,two),ReplacementTransform(Fourthmessagehash,hash2))
        self.play(ReplacementTransform(two,three),ReplacementTransform(hash2,hash3))
        
        self.wait()
        
        