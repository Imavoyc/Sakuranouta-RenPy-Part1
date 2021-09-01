label lmakerlogo:

    $ bgi_load_base()
    $ bgi_push_dword(4)
    $ bgi_add()
    $ bgi_store_base()
    $ bgi_push_offset('lmakerlogo_00238')
    $ bgi_reg_exception_handler()
    $ bgi_line('MakerLogo.bss', '15')
    $ bgi_push_dword(1)
    call bgi_f_124
    $ bgi_line('MakerLogo.bss', '17')
    call bgi_f_119
    $ bgi_line('MakerLogo.bss', '20')
    $ bgi_push_dword(200)
    $ bgi_f_0e7()
    $ bgi_push_dword(0)
    $ bgi_eq()
    $ bgi_push_offset('lmakerlogo_000ac')
    $ bgi_jc(0)
    $ bgi_line('MakerLogo.bss', '22')
    $ bgi_push_dword(0)
    call bgi_f_120
    $ bgi_line('MakerLogo.bss', '23')
    $ bgi_push_offset('lmakerlogo_000ac')
    $ bgi_jmp()

label lmakerlogo_000ac:
    $ bgi_line('MakerLogo.bss', '25')
    $ bgi_push_dword(3000)
    $ bgi_push_string('white')
    call bgi_f_280
    $ bgi_line('MakerLogo.bss', '27')
    $ bgi_push_dword(3000)
    $ bgi_push_string('Makuralogo')
    call bgi_f_280
    $ bgi_line('MakerLogo.bss', '29')
    call bgi_f_119
    $ bgi_line('MakerLogo.bss', '31')
    $ bgi_push_dword(5000)
    call bgi_f_110
    $ bgi_line('MakerLogo.bss', '33')
    $ bgi_push_dword(3000)
    $ bgi_push_string('white')
    call bgi_f_280
    $ bgi_line('MakerLogo.bss', '35')
    $ bgi_push_dword(2500)
    $ bgi_push_string('Att01')
    call bgi_f_280
    $ bgi_line('MakerLogo.bss', '37')
    call bgi_f_119
    $ bgi_line('MakerLogo.bss', '39')
    $ bgi_push_dword(5000)
    call bgi_f_110
    $ bgi_line('MakerLogo.bss', '41')
    $ bgi_push_dword(2500)
    $ bgi_push_string('Att02')
    call bgi_f_280
    $ bgi_line('MakerLogo.bss', '43')
    call bgi_f_119
    $ bgi_line('MakerLogo.bss', '51')
    $ bgi_push_dword(5000)
    call bgi_f_110
    $ bgi_line('MakerLogo.bss', '53')
    $ bgi_push_dword(1500)
    call bgi_f_288
    $ bgi_line('MakerLogo.bss', '55')
    $ bgi_push_dword(1)
    call bgi_f_120
    $ bgi_line('MakerLogo.bss', '57')
    $ bgi_push_dword(0)
    call bgi_f_124
    $ bgi_line('MakerLogo.bss', '61')
    $ bgi_push_dword(1)
    $ bgi_push_dword(200)
    $ bgi_f_0e6()
    $ bgi_line('MakerLogo.bss', '66')

label lmakerlogo_00238:
    $ bgi_unreg_exception_handler()
    $ bgi_load_base()
    $ bgi_push_dword(4)
    $ bgi_sub()
    $ bgi_store_base()
    return
