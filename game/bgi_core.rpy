init python:
    import time

    renpy.music.register_channel("music1","music")
    renpy.music.register_channel("music2","music")
    renpy.music.register_channel("music3","music")
    renpy.music.register_channel("loop_se","sfx")

    if persistent.global_var is None:
        persistent.global_var = [0] * 256

    bgi_f14b_dict = {}
    bgi_base_var = {}
    
    bgi_choices = []
    bgi_nvl_mode = 0
    bgi_timer = 0
    
    def bgi_push_dword(num):
        bgi_stack.append(num)
        
    def bgi_push_offset(num):
        bgi_stack.append(num)
        
    def bgi_push_base_offset(num):
        bgi_stack.append(bgi_stack_base - num)
       
    def bgi_push_string(str):
        bgi_stack.append(str)
        
    def bgi_load(num):
        p1 = bgi_stack.pop()
        if p1 not in bgi_base_var.keys():
            bgi_base_var[p1] = 0
        bgi_stack.append(bgi_base_var[p1])
        
    def bgi_move(num):
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_base_var[p2] = p1
        
    def bgi_move_arg(num):
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_base_var[p1] = p2
        
    def bgi_load_base():
        bgi_stack.append(bgi_stack_base)
        
    def bgi_store_base():
        bgi_stack_base = bgi_stack.pop()
    
    def bgi_jmp():
        p1 = bgi_stack.pop()
        renpy.jump(p1)
    
    def bgi_jc(num):
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        if p2 == 0:
            renpy.jump(p1)

    def bgi_reg_exception_handler():
        p1 = bgi_stack.pop()
    
    def bgi_unreg_exception_handler():
        pass

    def bgi_add():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p1 + p2)

    def bgi_sub():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 - p1)
        
    def bgi_mul():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 * p1)
        
    def bgi_div():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 / p1)
        
    def bgi_sar():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 >> (p1&0x1f))  
        
    def bgi_eq():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 == p1)

    def bgi_neq():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 != p1)

    def bgi_leq():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 <= p1)

    def bgi_geq():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 >= p1)
        
    def bgi_lt():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 < p1) 

    def bgi_gt():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 > p1)
        
    def bgi_bool_and():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 and p1)
        
    def bgi_bool_or():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_stack.append(p2 or p1)

    def bgi_bool_zero():
        p1 = bgi_stack.pop()
        bgi_stack.append(p1 == 0)

    def bgi_line(file,line):
        pass

    def bgi_f_0e0():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_local_var[p1] = p2

    def bgi_f_0e1():
        p1 = bgi_stack.pop()
        bgi_stack.append(bgi_local_var[p1])

    def bgi_f_0e2():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_local_var[p1] = p2

    def bgi_f_0e3():
        p1 = bgi_stack.pop()
        bgi_stack.append(bgi_local_var[p1])
        
    def bgi_f_0e4():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        bgi_local_var1[p1] = p2

    def bgi_f_0e5():
        p1 = bgi_stack.pop()
        bgi_stack.append(bgi_local_var1[p1])
        
    def bgi_f_0e6():
        p1 = bgi_stack.pop()
        p2 = bgi_stack.pop()
        persistent.global_var[p1] = p2

    def bgi_f_0e7():
        p1 = bgi_stack.pop()
        bgi_stack.append(persistent.global_var[p1])
        
    def bgi_f_0f0():
        _window_hide(trans=0, auto=False)
        p1 = bgi_stack.pop()
        if p1 == '02_Abend_rn_master':
            renpy.say(None,"恭喜您解锁了 稟线 !")
            renpy.say(None,"请从 稟线 开始游戏，通关后重玩共通线!")

            bgi_push_dword(1)
            bgi_push_dword(0)
            bgi_f_0e6()

            bgi_push_dword(1)
            bgi_push_dword(10)
            bgi_f_0e6()
            MainMenu(confirm=False)()
            return

        if p1 == '02_Abend_pi_master':
            renpy.say(None,"恭喜您解锁了 真琴线 !")
            renpy.say(None,"请从 真琴线 开始游戏，通关后重玩共通线!")

            bgi_push_dword(1)
            bgi_push_dword(1)
            bgi_f_0e6()

            bgi_push_dword(1)
            bgi_push_dword(10)
            bgi_f_0e6()
            MainMenu(confirm=False)()
            return

        if p1 == '02_Abend_ze_master':
            renpy.say(None,"恭喜您解锁了 里奈线 !")
            renpy.say(None,"请从 里奈线 开始游戏，通关后重玩共通线!")

            bgi_push_dword(1)
            bgi_push_dword(2)
            bgi_f_0e6()
            MainMenu(confirm=False)()
            return
            
        if p1 == '02_Abend_an_master':
            renpy.say(None,"恭喜您解锁了 雫线 !")
            renpy.say(None,"请从 雫线 开始游戏，通关后重玩共通线!")

            bgi_push_dword(1)
            bgi_push_dword(50)
            bgi_f_0e6()
            MainMenu(confirm=False)()
            return

        p1 = p1.lower()
        p1 = p1.replace('-', '_')
        renpy.call('l' + p1)

    def bgi_f_101():
        bgi_stack.append(int(time.time() * 1000))
        
    def bgi_f_12c():
        bgi_stack.append(0)

    def bgi_renpy_text_refine(text):
        text = text.replace('{', '{{')
        text = text.replace('}', '}}')
        text = text.replace('[', '[[')
        text = text.replace(']', ']]')
        text = text.replace('%', '%%')
        return text

    def bgi_renpy_text_f14b(text):
        for key,value in bgi_f14b_dict.items():
            text = text.replace(key, "{rb}%s{/rb}{rt}%s{/rt}" %(key,value))
        bgi_f14b_dict.clear()
        return text
        
    def bgi_f_140():
        bgi_clean_cache()

        p5 = bgi_stack.pop()    
        p4 = bgi_stack.pop()
        p3 = bgi_stack.pop()
        p2 = bgi_stack.pop()    #wait after show
        p1 = bgi_stack.pop()    #clean after show
        
        p5 = bgi_renpy_text_f14b(p5)
        p5 = bgi_renpy_text_refine(p5)

        if bgi_nvl_mode == 0:
            if p4 is not 0:
                renpy.say(p4,p5)
            else:
                renpy.say(None,p5)
        else:
            p5 = '{cps=%d}%s{/cps}' %(bgi_text_cps,p5)
            if p2 == 0:    
                p5 = p5 + '{nw}'
                
            if p4 is not 0:
                renpy.say(nvl_narrator,"{color=#00314fff}{size=+6}%s{/size}{/color} %s" %(p4,p5))
            else:
                renpy.say(nvl_narrator,"%s" % p5)
            
            

            
    def bgi_f_164():
        bgi_choices.clear()

    def bgi_f_168():
        global bgi_choices
        x = 0
        y = 0
        pic = ''
        txt = ''
        
        p2 = bgi_stack.pop()
        p1 = bgi_stack.pop()

        for c in range(p2):
            pic = bgi_base_var[p1 + 16*c + 0]
            x = bgi_base_var[p1 + 16*c + 4]
            y = bgi_base_var[p1 + 16*c + 8]
            txt = bgi_base_var[p1 + 16*c + 12]
            bgi_choices.append((txt,c))
        user_choice = renpy.display_menu(bgi_choices)
        bgi_stack.append(user_choice)
        bgi_choices.clear()
        
        
    def bgi_f_01c():
        global bgi_stack
        p1 = bgi_stack.pop()
        if p1 == 'RandomNumberReturn':
            bgi_stack.pop()
            bgi_stack.pop()
            bgi_stack.append(0)
            
        elif p1 == 'BSPosX' or p1 == 'BSPosY' or p1 == 'SPPosY' or p1 == 'SPPosX':
            bgi_stack.pop()
            bgi_stack.append(0)
        else:
            bgi_stack = []

