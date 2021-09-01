label lmain:

    $ bgi_load_base()
    $ bgi_push_dword(4)
    $ bgi_add()
    $ bgi_store_base()
    $ bgi_push_offset('lmain_000d4')
    $ bgi_reg_exception_handler()
    $ bgi_line('main.bss', '13')
    $ bgi_push_dword(1)
    call bgi_f_122
    $ bgi_line('main.bss', '14')
    $ bgi_push_dword(1)
    call bgi_f_123
    $ bgi_line('main.bss', '21')
    $ bgi_push_dword(0)
    $ bgi_push_dword(28)
    $ bgi_push_dword(0)
    call bgi_f_14c
    $ bgi_line('main.bss', '22')
    $ bgi_push_dword(0)
    $ bgi_push_dword(0)
    $ bgi_push_dword(0)
    call bgi_f_14e
    $ bgi_line('main.bss', '23')
    $ bgi_push_string('00_op_master')
    $ bgi_f_0f0()
    $ bgi_line('main.bss', '35')
    call bgi_f_0f4
    $ bgi_line('main.bss', '37')

label lmain_000d4:
    $ bgi_unreg_exception_handler()
    $ bgi_load_base()
    $ bgi_push_dword(4)
    $ bgi_sub()
    $ bgi_store_base()
    return
