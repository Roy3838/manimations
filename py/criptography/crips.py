from manim import *
from hashlib import sha256
import itertools as it
import binascii
import random
import time

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
 
class cripto(MovingCameraScene):
    def construct(self):
        
        #a method that creates a blockchain block of random transactions
        def Create_block_list(lista_transactions,testing):
            if testing:
                lista_transactions=6
            #classic names of criptographic example persons
            names = ["Alice", "Bob", "Charlie", "Carol", "Carlos", "Craig", "David", "Eve", "Yves", "Faythe", "Frank", "Grace",
                     "Heidi", "Ivan", "Judy", "Mallory", "Mike", "Michael", "Niaj", "Olivia", "Oscar"]
            
            
            line = Text("0")
            pre_result = VGroup(*[
                line.copy() for row in range(lista_transactions)
            ])
            pre_result.arrange(DOWN, buff = SMALL_BUFF)
            result = VGroup(*it.chain(*pre_result))
            
            #remove randomness, cached Mobjects reduce testing time
            for i in range(lista_transactions):
                #remove randomness, cached Mobjects reduce testing time
                if testing == True:
                    person1 = "test"
                    person2 = "test"
                    cantidad = 0
                else:
                    person1=random.choice(names)
                    person2=random.choice(names)
                    cantidad = random.randint(1,99)
                result.submobjects[i]=Text(
                    person1+" transfiere a "+person2+" "+str(cantidad)+" BTC"
                    ).shift(0.25*DOWN*(i+1) + 1.1*UP).scale([0.15,0.2,1])
                
            block_color = BLACK
            text_color = BLACK
            heightb=result.submobjects[0].get_top()[1]-result.submobjects[lista_transactions-1].get_bottom()[1]
            block = Rectangle(height=(heightb + 0.7), width=2, color=block_color).move_to([0,-heightb*0.5 + 0.8,0])
            blocktop = Rectangle(height=0.5, width=2, color=block_color).move_to([0,(block.get_top()[1]+0.25),0])
            blockbottom = Rectangle(height=0.5, width=2, color=block_color).move_to([0,(block.get_bottom()[1]-0.25),0])
            
            result.set_color(text_color)
            return [VGroup(block,blocktop,blockbottom,result),result,heightb]
        

        
        #create blockchain
        
        
        #create arrow between blocks


        """
        Settings of the scene, affects directly, unindented block starts here 
        ----------------------------------------------------------------------------------------------
        
        """
        
        self.camera.frame.save_state()
        self.camera.background_color = "#E2E2E2"
        
        
        
        
        
        
        l=8
        testing=False
        for i in range(l):
            tic = time.perf_counter()
            #COLORS
            header_color = BLACK
            salt_color = BLACK
            arrow1_color = BLACK
            arrow2_color = BLACK
            hash_color = BLACK
            hashbrace_color = GOLD
            proof_of_work_color = BLACK
            
            
            
            print("Block creation = " + str(i+1) + "/" + str(l))
            #create block
            [block,result,alt]=Create_block_list(random.randint(6,9),testing)#nice
            block.move_to(i*3*RIGHT + 5*LEFT+ UP*2.3 + DOWN*0.5*alt)
            #create salt
            salt=random.randint(100000000000000,999999999999999)
            salt=Text(str(salt), color = salt_color).scale(0.3)
            salt.move_to(block.get_bottom()+0.23*UP)
            header=random.randint(100000000000000,999999999999999)
            header=Text(str(header), color = header_color).scale(0.3)
            header.move_to(block.get_top()+0.23*DOWN + 3*RIGHT)

            #arrow to hash
            #arrow vieja
            arrow=Arrow(0.5*UP,0.5*DOWN, color = arrow1_color).move_to([block.get_bottom()[0],-1.8,0])
            #arrow nueva
            

            #arrow from hash to header
            arc1=ArcBetweenPoints(DOWN*2+LEFT*2, DOWN+LEFT)
            line=Line(DOWN+LEFT, UP+LEFT)
            arc2=ArcBetweenPoints(UP*2, UP+LEFT).rotate(2*PI)
            tip=Arrow(UP*2+LEFT*2,UP*2+RIGHT*0.6,max_stroke_width_to_length_ratio=0)
            
            #components of brace ^^^
            brace=VGroup(arc1, line, arc2, tip)
            brace.move_to(block.get_right()+0.5*RIGHT)
            brace.scale([0.4,0.6,1])
            brace.set_color(arrow2_color)

            #hash
            hash=sha256_tex_mob(str(random.randint(1,99)))
            hash.move_to(arrow.get_bottom()+DOWN*0.8).scale(0.5)
            hash.scale([0.6,1,1])
            hash.set_color(hash_color)
            
            newarrow=Arrow(block.get_bottom(), hash.get_top() + UP*0.2, color = arrow1_color)
            temporary_brace_for_text=BraceBetweenPoints(block.get_bottom() + RIGHT*1.4 + 0.1*UP,
                                                        hash.get_top() + UP*0.2 + RIGHT*1.4 + 0.1*UP,)
            arrowtext=temporary_brace_for_text.get_text("SHA256").rotate(PI/2)
            arrowtext.set_color(arrow1_color)
            arrowtext.scale(0.4)

            
            #proof of work (hash) brace
            
            hashbrace=BraceBetweenPoints(hash.submobjects[20].get_bottom() + DOWN*0.07,
                                            hash.submobjects[0].get_bottom() + DOWN*0.07)
            hashbrace.set_color(hashbrace_color)
            #proof of work text
            
            texto=MathTex("\\text{Proof of work}").move_to(hashbrace.get_top()+UP*0.1).scale(0.4)
            texto.set_color(proof_of_work_color)
            

            arrow2=Arrow(block.get_right(),block.get_right()+RIGHT)
            
            #nueva arrow
            #arrow=Arrow(block.get_bottom(),hash.get_top(),max_tip_length_to_length_ratio=1)

            hashbox=SurroundingRectangle(arrowtext, buff = 0.1, color=GOLD)
            hashbox2=SurroundingRectangle(hash, buff = .1, color=GOLD)
            self.play(Create(block),run_time=1)
            self.play(Create(salt),run_time=0.3)
            self.play(Create(newarrow),Create(arrowtext),run_time=0.3)
            self.play(Create(hash),run_time=0.3)
            if i==0:
                self.play(Create(hashbox))
                self.wait()
                self.play(ReplacementTransform(hashbox,hashbox2),run_time=1)
            
            hashrate=random.randint(5,40)
            if testing:
                hashrate=0
            if i>=1:
                self.play(self.camera.frame.animate.move_to([block.get_center()[0] + 5,0,0]))
            #hashing proof of work 
            for x in range(hashrate):
                self.remove(hash,salt)
                if hashrate ==0:
                    hash=sha256_tex_mob(str("patata"))
                salt=random.randint(100000000000000,999999999999999)
                salt=Text(str(salt)).scale(0.3)
                salt.move_to(block.get_bottom()+0.23*UP)
                if x>=hashrate-1:
                    hash=sha256_tex_mob(str(random.randint(1,99)), 20)
                else:
                    hash=sha256_tex_mob(str(random.randint(1,99)))
                hash.move_to(arrow.get_bottom()+DOWN*0.8).scale(0.5)
                hash.scale([0.6,1,1])
                hash.set_color(hash_color)
                salt.set_color(salt_color)
                self.add(hash, salt)
                self.wait(0.1)
            
            if i!=l-1:
                if i==0:
                    self.play(FadeOut(hashbox2))
                self.play(Create(hashbrace))
                self.play(Write(texto))
                self.wait(0.5)
                self.play(Transform(hash,header),Transform(newarrow,brace),FadeOut(hashbrace,texto,arrowtext))
                

            
            self.wait(0.3)
            
            toc = time.perf_counter()
            print(f"Time to render block = {toc - tic:0.4f} seconds")

        #self.play(FadeIn(texto))
        #self.play(Transform(texto,sha256_tex_mob("text")))
        self.wait()
        #self.play(FadeOut(texto))
        
        self.wait()
        
        