label lmainforrouteiv:

    $ bgi_load_base()
    $ bgi_push_dword(4)
    $ bgi_add()
    $ bgi_store_base()
    $ bgi_push_offset('lmainforrouteiv_000c4')
    $ bgi_reg_exception_handler()
    $ bgi_line('MainForRouteIV.bss', '15')
    $ bgi_push_dword(1)
    call bgi_f_122
    $ bgi_line('MainForRouteIV.bss', '16')
    $ bgi_push_dword(1)
    call bgi_f_123
    $ bgi_line('MainForRouteIV.bss', '18')
    $ bgi_push_string('04_What_is_mind？_01')
    $ bgi_f_0f0()
    $ bgi_line('MainForRouteIV.bss', '19')
    $ bgi_push_string('04_What_is_mind？_02')
    $ bgi_f_0f0()
    $ bgi_line('MainForRouteIV.bss', '22')
    $ bgi_push_string('ED05')
    $ bgi_f_0f0()
    $ bgi_line('MainForRouteIV.bss', '25')
    $ bgi_push_dword(1)
    $ bgi_push_dword(60)
    $ bgi_f_0e6()
    $ bgi_line('MainForRouteIV.bss', '28')

label lmainforrouteiv_000c4:
    $ bgi_unreg_exception_handler()
    $ bgi_load_base()
    $ bgi_push_dword(4)
    $ bgi_sub()
    $ bgi_store_base()
    return
