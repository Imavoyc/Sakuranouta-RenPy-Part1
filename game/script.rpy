image black = "#000"
image white = "#fff"
image red = "#f00"

style ruby_style is default:
    size 12
    yoffset -20

style say_dialogue:
    line_leading 12
    ruby_style style.ruby_style

init python:
    bgi_sakura = 1

    def main_choice():
        #renpy.show('sgscslct990000',tag='30',zorder=0)
        #renpy.music.play('audio/bgm019.ogg', channel="music", fadein=1.0,relative_volume=1.0)
        
        bgi_choices.clear()
        bgi_choices.append(("共通线",0))
        
        if persistent.global_var[50]:
            bgi_choices.append(("IV",1))
        if persistent.global_var[60]:
            bgi_choices.append(("V",2))
        if persistent.global_var[70]:
            bgi_choices.append(("Ⅵ",3))

        user_choice = renpy.display_menu(bgi_choices)
        #renpy.music.stop(channel="music",fadeout=1.0)
        #renpy.scene()
        #renpy.scene(layer='f30x')
        #renpy.show('black',tag='30',zorder=0)
        #renpy.with_statement(Dissolve(p1/1000.0))
        #bgi_stack.append(user_choice)
        if user_choice == 0:
            bgi_push_string('main')
            bgi_f_0f0()
        if user_choice == 1:
            bgi_push_string('mainforrouteiv')
            bgi_f_0f0()
        if user_choice == 2:
            bgi_push_string('mainforroutev')
            bgi_f_0f0()
        if user_choice == 3:
            bgi_push_string('mainforroutevi')
            bgi_f_0f0()

label splashscreen:
    $ bgi_stack = []
    $ bgi_stack_base = 0
    $ bgi_char_pos = [0] * 32
    $ bgi_f30x_pos = [0] * 32

    $ bgi_push_string('makerlogo')
    $ bgi_f_0f0()
    return


        
label start:
    $ bgi_local_var = [0] * 256
    $ bgi_local_var1 = [0] * 256

    $ bgi_char_pos = [0] * 32
    $ bgi_f30x_pos = [0] * 32
    
    $ bgi_stack = []
    $ bgi_stack_base = 0
    
    $ bgi_font_size = 34
    $ bgi_text_cps = 0

    stop music fadeout 1.0
    scene black with Dissolve(1.0)

    $ main_choice()
    #$ bgi_push_string('main')
    #$ bgi_f_0f0()
    return