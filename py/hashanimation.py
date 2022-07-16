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
        self.generalfunction()
        self.hashfunction()
    
    
    def generalfunction(self):
        function=MathTex(f"f(x)=x^{2}")
        self.play(Write(function))
        self.play(FadeOut(function))
        
        
        """
        
        """
        
        
    def hashfunction(self):
        #make scene to explain the identifying caracteristics that a hash function has
        
        def make_two_hash_function(message):
            Inputbefore=Text("Hash( \"").scale(0.6).move_to(3*LEFT)

            messagehash=sha256_tex_mob(message).scale([0.4,0.6,1])

            messagemob1 = Text(message.split(",")[0],color=BLUE).scale(0.6)
            messagemob1.align_to(Inputbefore,DOWN)
            messagemob2 = Text(", ",color=WHITE).scale(0.6)
            messagemob2.move_to(messagemob1.get_corner(DR)+RIGHT*0.1)
            messagemob3 = Text(message.split(",")[1],color=BLUE).scale(0.6)
            messagemob3.move_to(messagemob1.get_right()+RIGHT*0.6)
            messagemob1.shift(0.1*DOWN)
            
            messagemob3.align_to(Inputbefore,DOWN)
            messagemob1.align_to(Inputbefore,DOWN)
            messagemob = VGroup(messagemob1,messagemob2,messagemob3)
            
            widthofmessage=messagemob.get_width()
            
            # messagemob moved to inputright with buffer messagewidth--> |-----.-----|
            messagemob.move_to(Inputbefore.get_right()+widthofmessage/2*RIGHT + 0.05*RIGHT)
            # Input after moved to messageright with buffer widthInput |-----.-----| <---
            
            Inputafter=Text("\" ) = ").scale(0.6)
            Inputwidth=Inputafter.get_width()
            Inputafter.move_to(messagemob.get_right() + Inputwidth/2*RIGHT + 0.05*RIGHT)
            
            #align 
            
            Input=VGroup(Inputbefore,messagemob1,messagemob2,messagemob3,Inputafter)
            
            messagehash.move_to(Inputafter.get_right() + 2*RIGHT)
            
            
            return [Input,messagehash]
        
        
        def make_hash_function(message):
            #hash with message
            Inputbefore=Text("Hash( \"").scale(0.6).move_to(3*LEFT)
            
            
            messagehash=sha256_tex_mob(message).scale([0.4,0.6,1])
            messagemob = Text(message,color=BLUE).scale(0.6)
                
            
            
            #centering and aligning
            widthofmessage=messagemob.get_width()
            
            # messagemob moved to inputright with buffer messagewidth--> |-----.-----|
            messagemob.move_to(Inputbefore.get_right()+widthofmessage/2*RIGHT + 0.05*RIGHT)
            # Input after moved to messageright with buffer widthInput |-----.-----| <---
            
            Inputafter=Text("\" ) = ").scale(0.6)
            Inputwidth=Inputafter.get_width()
            Inputafter.move_to(messagemob.get_right() + Inputwidth/2*RIGHT + 0.05*RIGHT)
            Input=VGroup(Inputbefore,messagemob,Inputafter)
            
            messagehash.move_to(Inputafter.get_right() + 2*RIGHT)
            return [Input,messagehash]
        
        
        [Input,messagehash]=make_hash_function("Message")
        self.play(Write(Input))
        
        
        self.wait()
        
        