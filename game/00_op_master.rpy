label l00_op_master:

    $ bgi_load_base()
    $ bgi_push_dword(4)
    $ bgi_add()
    $ bgi_store_base()
    $ bgi_push_offset('l00_op_master_00134')
    $ bgi_reg_exception_handler()
    $ bgi_line('00_op_master.bss', '16')
    $ bgi_push_string('00_op_01')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '17')
    $ bgi_push_string('00_op_02')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '18')
    $ bgi_push_string('00_op_03')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '19')
    $ bgi_push_string('00_op_04')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '20')
    $ bgi_push_string('01_Fruhlingsbeginn_01')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '21')
    $ bgi_push_string('01_Fruhlingsbeginn_02')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '22')
    $ bgi_push_string('01_Fruhlingsbeginn_03')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '23')
    $ bgi_push_string('01_Fruhlingsbeginn_04')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '24')
    $ bgi_push_string('01_Fruhlingsbeginn_05')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '25')
    $ bgi_push_string('01_Fruhlingsbeginn_06')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '26')
    $ bgi_push_string('01_Fruhlingsbeginn_end')
    $ bgi_f_0f0()
    $ bgi_line('00_op_master.bss', '28')

label l00_op_master_00134:
    $ bgi_unreg_exception_handler()
    $ bgi_load_base()
    $ bgi_push_dword(4)
    $ bgi_sub()
    $ bgi_store_base()
    return
